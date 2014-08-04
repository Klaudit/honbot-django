'use strict';

angular.module('hb-www-app')
    .controller('PlayerHistoryController', function($scope, $http, BaseUrl) {
        $scope.currentcount = 1;
        $scope.more = function(){
            if($scope.s){
                $scope.currentcount += 1;
                $scope.url = BaseUrl + '/player_history/' + $scope.s.player_id + '/' + $scope.currentcount + '/' + $scope.m;
                $http({
                    method: 'GET',
                    url: $scope.url
                }).
                success(function(res) {
                    $scope.s = res;
                    $scope.s.rnk_mmr = Math.floor($scope.s.rnk_mmr);
                    $scope.s.cs_mmr = Math.floor($scope.s.cs_mmr);
                    $scope.s.acc_mmr = Math.floor($scope.s.acc_mmr);
                }).
                error(function(res) {
                    console.log(res);
                    console.log('ERORROROROR');
                });
            }
        };
        
        

    });
