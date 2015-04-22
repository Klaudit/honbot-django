var https = require('https');
var concat = require('concat-stream');
var config = require('./config');

module.exports = function api(path) {
    return new Promise(function(resolve, reject) {
        https.get({
            host: 'api.heroesofnewerth.com',
            path: `${path}?token=${config.token}`
        }, function(response) {
            // console.log(response)
            console.log(response.req.path)
            if (response.statusCode === 200) {
                response.pipe(concat(function(body) {
                    var parsed = JSON.parse(body);
                    // console.log(parsed);
                    resolve(parsed);
                }));
            } else {
                reject(Error("Bad status code"));
            }
        });
    })
}