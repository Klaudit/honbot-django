'use strict';

function secondsToTime(secs)
{
    var hours = Math.floor(secs / (60 * 60));
   
    var divisor_for_minutes = secs % (60 * 60);
    var minutes = Math.floor(divisor_for_minutes / 60);
 
    var divisor_for_seconds = divisor_for_minutes % 60;
    var seconds = Math.ceil(divisor_for_seconds);
   
    var obj = {
        'h': hours,
        'm': minutes,
        's': seconds
    };
    return obj;
}

angular.module('hbwww').controller('MatchController', function($scope, $routeParams, BaseUrl, $http, $timeout, $rootScope, $log, _, items, heroes) {

    // init
    $scope.match_id = $routeParams.match;
    $scope.item_names = _.indexBy(items, 'id');
    $scope.hero_names = heroes;
    
    var url = BaseUrl + '/match/' + $scope.match_id + '/';
    $log.log(url);
    $http({
        method: 'GET',
        url: url
    })
    .success(function(res) {
        $log.debug(res);
        $scope.match = res;
        $scope.len = secondsToTime($scope.match.length);
        var t1 = 0,
            t2 = 0,
            tgpm = [];

        if(t1 > t2){
            $scope.winner = 'Legion';
        } else {
            $scope.winner = 'Hellbourne';
        }

        // tooltips init
        url = BaseUrl + '/ptip/';
        $scope.ptips = {};

        angular.forEach($scope.match.players, function(p) {
            // load item arrays
            if(p.items !== ''){
                p.items = angular.fromJson(p.items);
            }
            // calculate winning team
            if(p.discos !== 1){
                if(p.team === 1){
                    t1 += p.win;
                } else {
                    t2 += p.win;
                }
            }
            tgpm.push({name: p.nickname, data: [Math.floor(p.gpm)], color: $rootScope.pos_colors[p.position]});

            url += p.player_id + '/';
            $scope.ptips[p.player_id] = {
                'title': '<h4 class="ptiphead">' + p.nickname + '</h4>',
                'content': '<span class="ptip-warning">Stats not loaded</span><br>'
            };
        });
        // player tooltips
        $http({method: 'GET', url: url}).success(function(res){
            $log.debug(res);
            angular.forEach(res, function(v){
                $scope.ptips[v.player_id] = {
                    'title': '<h4 class="ptiphead"><img src="' + v.avatar + '" width=30> ' + v.nickname + '</h4>',
                    'content': '<h4 class="ptiphead"><span class="ptip-success">' + v[$scope.match.mode + '_wins'] + ' </span> - <span class="ptip-warning"> ' + v[$scope.match.mode + '_losses'] + '</span></h4>' +
                               '<strong>MMR</strong>: <span class="ptip-blue">' + Math.floor(v[$scope.match.mode + '_mmr']) + '</span><br>' +
                               '<strong>KDR</strong>: ' + Math.round(v[$scope.match.mode + '_kdr'] * 100) / 100 + '</span><br>' +
                               '<strong>APM</strong>: ' + Math.floor(v[$scope.match.mode + '_avg_apm'])
                };
            });
        });
    }); 
});
