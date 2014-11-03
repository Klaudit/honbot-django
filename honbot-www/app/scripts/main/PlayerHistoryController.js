'use strict';

angular.module('hbwww').controller('PlayerHistoryController', function($scope, $http, BaseUrl, $location, $timeout, $log) {
    $scope.currentcount = 0;
    $scope.history = [];
    $scope.more = function(){
        if(!$scope.s.id){return;}
        $scope.currentcount += 1;
        // TODO: disable additional calls of more here
        $scope.url = BaseUrl + '/history/' + $scope.s.id + '/' + $scope.currentcount + '/' + $scope.m + '/';
        $http({
            method: 'GET',
            url: $scope.url,
            cache: true
        })
        .success(function(res) {
            $log.debug(res);
            $scope.history = $scope.history.concat(res.result);
            if(res.length < 25){
                $scope.nomore = true;
            }
            // TODO: enable more() again
        });
    };
    $scope.goMatch = function(match_id){
        $location.path('/match/' + match_id + '/');
    };
    $scope.$on('playerLoaded', function(){
        $scope.more();
    });
    $scope.more();
});
