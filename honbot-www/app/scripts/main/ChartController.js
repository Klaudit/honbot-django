'use strict';

angular.module('hbwww').controller('ChartController', function($scope, BaseUrl, $http) {
    $scope.view = 'chart';

    $scope.chart = function(){
        var url = BaseUrl + '/player_cache/' + $scope.s.player_id + '/' + $scope.m + '/';
        $http({
            method: 'GET',
            url: url
        })
        .success(function(res) {
            $scope.c = res;
        });
    };
    $scope.$on('playerLoaded', function(event){
        $scope.chart();
    });
    if($scope.s !== undefined){
        $scope.chart();
    }
});
