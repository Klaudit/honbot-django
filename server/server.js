/**
 * Koa Module dependencies.
 */
var koa = require('koa.io');
var logger = require('koa-logger');
var router = require('koa-router');
var responseTime = require('koa-response-time');
var compress = require('koa-compress');
var cors = require('koa-cors');

var moment = require('moment');
var JSONStream = require('JSONStream');

/**
 * Environment.
 */
var env = process.env.NODE_ENV || 'dev';

var config = require('./config');
var player = require('./player');
var mongo = require('./mongo');

var app = koa();

if ('dev' == env) app.use(logger());

app.use(responseTime());
app.use(compress());
app.use(cors());
app.use(mongo({
  url: config.db,
  max: 100,
  min: 1
}));
app.use(router(app));

// json middleware
app.use(function*(next) {
    this.type = 'json';
    yield next;
});
app.get('/player/:player', player);


app.listen(5000);