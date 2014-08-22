'use strict';

angular.module('hbwww')
    .controller('PlayerHistoryController', function($scope, $http, BaseUrl, $location) {
        $scope.currentcount = 1;
        $scope.more = function(){
            if($scope.s){
                $scope.url = BaseUrl + '/player_history/' + $scope.s.player_id + '/' + $scope.currentcount + '/' + $scope.m + '/';
                $http({
                    method: 'GET',
                    url: $scope.url
                }).
                success(function(res) {
                    $scope.history = res;
                    console.log(res);
                }).
                error(function(res) {
                    console.log(res);
                    console.log('ERORROROROR');
                });
            }
        };
        $scope.next = function(){
            $scope.currentcount += 1;
            $scope.more();
        };
        $scope.previous = function(){
            if($scope.currentcount > 1){
                $scope.currentcount = $scope.currentcount - 1;
            }
            $scope.more();
        };
        $scope.goMatch = function(match_id){
            $location.path('/match/' + match_id + '/');
        };
        $scope.$on('playerLoaded', function(event, data){
            $scope.more(data);
        });
        
        

    });
