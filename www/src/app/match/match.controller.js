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

angular.module('www').controller('MatchCtrl', function($scope, $routeParams, BaseUrl, $http, $rootScope, heroes, items, $filter) {

    $scope.item_names = items;
    $scope.hero_names = heroes;
    $scope.ptips = {};
    $scope.pmmr = {};

    var t1 = 0,
        t2 = 0,
        tgpm = [];
    
    var url = BaseUrl + '/match/' + $routeParams.match + '/';
    console.log(url);
    $http.get(url)
    .success(function(res) {
        $scope.match = res;
        $scope.len = secondsToTime($scope.match.length);
        
        if(t1 > t2){
            $scope.winner = 'Legion';
        } else {
            $scope.winner = 'Hellbourne';
        }

        url = BaseUrl + '/ptip/?players=';

        $scope.match.players = $filter('orderBy')($scope.match.players, 'position');

        angular.forEach(res.players, function(p) {
            // calculate winning team
            if(p.discos !== 1){
                if(p.team === 1){
                    t1 += p.win;
                } else {
                    t2 += p.win;
                }
            }
            tgpm.push({name: p.nickname, data: [Math.floor(p.gpm)], color: $rootScope.pos_colors[p.position]});

            url += p.id + ',';
            console.log(url);
            $scope.ptips[p.id] = {
                'title': '<h4 class="ptiphead">' + p.nickname + '</h4>',
                'content': '<span class="ptip-warning">Stats not loaded</span><br>'
            };
            $scope.pmmr[p.id] = '';
        });
        $http.get(url).success(function(res){
            angular.forEach(res.result, function(v){
                $scope.pmmr[v._id] = Math.floor(v[$scope.match.mode + '_mmr']);
                $scope.ptips[v._id] = {
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
