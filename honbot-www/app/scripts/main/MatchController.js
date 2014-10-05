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

angular.module('hbwww').controller('MatchController', function($scope, $routeParams, BaseUrl, $http, $timeout, $rootScope, $log, _) {

    // init
    $scope.match_id = $routeParams.match;
    
    var url = BaseUrl + '/match/' + $scope.match_id + '/';
    $log.log(url);
    $http({
        method: 'GET',
        url: url
    })
    .success(function(res) {
        $scope.match = res;
        var t1 = 0,
            t2 = 0,
        d = {
            l: [],
            h: [],
            hcolor: [],
            lcolor: [],
            lkills: 0,
            hkills: 0,
            lassists: 0,
            hassists: 0,
            lxpm: 0,
            hxpm: 0,
            lcreeps: 0,
            hcreeps: 0,
            lgpm: 0,
            hgpm: 0,
            lapm: 0,
            hapm: 0
        },
        tgpm = [];
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
            // setup data for the silly graphs
            if(p.team === 1){
                d.l.push([p.nickname, p.herodmg]);
                d.lcolor.push($rootScope.pos_colors[p.position]);
                d.lkills += p.kills;
                d.lassists += p.assists;
                d.lxpm += p.xpm;
                d.lcreeps += p.cs;
                d.lgpm += p.gpm;
                d.lapm += p.apm;
            }
            if(p.team === 2){
                d.h.push([p.nickname, p.herodmg]);
                d.hcolor.push($rootScope.pos_colors[p.position]);
                d.hkills += p.kills;
                d.hassists += p.assists;
                d.hxpm += p.xpm;
                d.hcreeps += p.cs;
                d.hgpm += p.gpm;
                d.hapm += p.apm;
            }
            tgpm.push({name: p.nickname, data: [Math.floor(p.gpm)], color: $rootScope.pos_colors[p.position]});
        });

        // set winning team
        $scope.len = secondsToTime($scope.match.length);
        if(t1 > t2){
            $scope.winner = 'Legion';
        } else {
            $scope.winner = 'Hellbourne';
        }
        

        // tooltips
        url = BaseUrl + '/ptip/';
        $scope.ptips = {};
        angular.forEach($scope.match.players, function(v) {
            url += v.player_id + '/';
            $scope.ptips[v.player_id] = {
                'title': '<h4 class="ptiphead">' + v.nickname + '</h4>',
                'content': '<span class="ptip-warning">Stats not loaded</span><br>'
            };
        });
        $http({method: 'GET', url: url}).success(function(res){
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
