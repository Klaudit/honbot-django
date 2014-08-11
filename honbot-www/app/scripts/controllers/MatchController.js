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

angular.module('hb-www-app')
    .controller('MatchController', function($scope, $routeParams, BaseUrl, $http) {
        $scope.match_id = $routeParams.match;
        var url = BaseUrl + '/match/' + $scope.match_id + '/';
        $http({
            method: 'GET',
            url: url
        })
        .success(function(res) {
            $scope.match = res;
            console.log(res);
            var t1 = 0,
                t2 = 0;
            angular.forEach($scope.match.players, function(p) {
                if(p.team === 1){
                    t1 += p.win;
                } else {
                    t2 += p.win;
                }
            });
            $scope.len = secondsToTime($scope.match.length);
            if(t1 > t2){
                $scope.winner = 'Legion';
            } else {
                $scope.winner = 'Hellbourne';
            }
        })
        .error(function(res) {
            console.log(res);
            console.log('ERORROROROR');
        });
        
        
        

    });
