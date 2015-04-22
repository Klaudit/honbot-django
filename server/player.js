var api = require('./api')
var _ = require('lodash');

module.exports = function* player(next) {
    var that = this;
    this.body = yield api(`/player_statistics/all/nickname/${this.params.player}/`).then(
        function(res) {
            processed = processPlayer(res);
            that.mongo.collection('players').insert(processed);
            return processed;
        },
        function(error) {
            return error;
        }
    );
    yield next;
}

function processPlayer(res) {
    var p = {};
    _.forEach(res, function(n, key) {
        p[key] = parseFloat(n);
    });
    _.forEach(['rnk', 'cs', 'acc'], function(n) {
        p[`${n}_mmr`] = p['rnk_amm_team_rating']
        p[`${n}_avg_kills`] = p[`${n}_herokills`] / p[`${n}_games_played`];
        p[`${n}_avg_deaths`] = p[`${n}_deaths`] / p[`${n}_games_played`];
        p[`${n}_avg_assists`] = p[`${n}_heroassists`] / p[`${n}_games_played`];
        p[`${n}_avg_creeps`] = (p[`${n}_neutralcreepkills`] + p[`${n}_teamcreepkills`]) / p[`${n}_games_played`]
        p[`${n}_avg_denies`] = p[`${n}_denies`] / p[`${n}_games_played`];
        var temptime = p[`${n}_secs`] / 60;
        p[`${n}_avg_xpm`] = p[`${n}_exp`] / temptime;
        p[`${n}_avg_apm`] = p[`${n}_actions`] / temptime;
        p[`${n}_avg_gpm`] = p[`${n}_gold`] / temptime;
        p[`${n}_avg_consumables`] = p[`${n}_consumables`] / p[`${n}_games_played`];
        p[`${n}_avg_time`] = temptime / p[`${n}_games_played`];
        p[`${n}_winpercent`] = p[`${n}_wins`] / p[`${n}_games_played`];
        p[`${n}_kdr`] = p[`${n}_herokills`] / p[`${n}_deaths`];
        p[`${n}_avg_wards`] = p[`${n}_wards`] / p[`${n}_games_played`];
        p[`${n}_kadr`] = (p[`${n}_herokills`] + p[`${n}_heroassists`]) / p[`${n}_deaths`];
    });
    _.forEach(p, function(n, key){
        if(n===Number(n) && n%1!==0){
            p[key] = n.toFixed(3);
        }
    });
    return p;
}