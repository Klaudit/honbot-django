'use strict';

angular.module('hb-www-app')
    .controller('PlayerController', function($scope, $routeParams, $http, BaseUrl, $location) {
        $scope.view = 'player';
        $scope.s = {};
        $scope.s.avatar = 'images/default_avatar.png';
        $scope.nickname = $routeParams.player;
        $scope.url = '';
        if ($routeParams.mode === undefined) {
            $scope.m = 'rnk';
            $scope.modefull = 'Ranked';
        } else if ($routeParams.mode === 'c') {
            $scope.m = 'cs';
            $scope.modefull = 'Casual';
            $scope.url = '/c';
        } else if ($routeParams.mode === 'p') {
            $scope.m = 'acc';
            $scope.modefull = 'Public';
            $scope.url = '/p';
        }
        $scope.player = $routeParams.player;
        var url = BaseUrl + '/player/' + $routeParams.player + '/';
        console.log(url);
        $http({
            method: 'GET',
            url: url
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
        $scope.mode = function(mode) {
            $scope.m = mode;
            if (mode === 'cs') {
                $location.path('/c/player/' + $scope.nickname + '/', false);
            } else if (mode === 'acc') {
                $location.path('/p/player/' + $scope.nickname + '/', false);
            } else {
                $location.path('/player/' + $scope.nickname + '/', false);
            }

        };

    });
