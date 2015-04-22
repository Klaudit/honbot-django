// from https://github.com/MangroveTech/koa-mongo
var MongoClient = require('mongodb').MongoClient;
var poolModule = require('generic-pool');

module.exports = mongo;

function mongo(options) {
    options = options || {};
    var max = options.max || 100;
    var min = options.min || 1;
    var timeout = options.timeout || 30000;
    var log = options.log || false;
    var mongoUrl = options.url;

    var mongoPool = poolModule.Pool({
        name: 'koa-mongo',
        create: function(callback) {
            MongoClient.connect(mongoUrl, {
                server: {
                    poolSize: 1
                },
                native_parser: true
            }, function(err, client) {
                if (err) throw err;
                callback(err, client);
            });
        },
        destroy: function(client) {
            client.close();
        },
        max: max,
        min: min,
        idleTimeoutMillis: timeout,
        log: log
    });

    return function* mongo(next) {
        this.mongo = yield mongoPool.acquire;
        yield *next;
    }
}