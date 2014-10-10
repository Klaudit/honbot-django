'use strict';

angular.module('hbwww').controller('ChartController', function($scope, BaseUrl, $http) {
    $scope.view = 'chart';
    $scope.title = 'DemoCtrl';

    $scope.chart = function(){
        if(!$scope.s.player_id){return;}
        var url = BaseUrl + '/player_cache/' + $scope.s.player_id + '/' + $scope.m + '/';
        $http({
            method: 'GET',
            url: url,
            cache: true
        })
        .success(function(res) {
            $scope.c = res;
        });
    };
    $scope.$on('playerLoaded', function(){
        $scope.chart();
    });

    $scope.chart();
});
