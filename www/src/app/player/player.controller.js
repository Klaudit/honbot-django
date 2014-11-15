'use strict';

angular.module('www')
    .controller('PlayerCtrl', function($scope, $routeParams, $http, BaseUrl, $location, $modal, $timeout, $window) {
        if ($routeParams.view === undefined) {
            $scope.view = 'stats';
        } else if ($routeParams.view === 'chart'){
            $scope.view = 'chart';
        } else if ($routeParams.view === 'hero'){
            $scope.view = 'hero';
        }
        console.log($routeParams.view);
        $scope.s = {};
        $scope.nickname = $routeParams.player;
        if ($routeParams.mode === undefined) {
            $scope.m = 'rnk';
            $scope.modefull = 'Ranked';
            $scope.mode_url = '';
        } else if ($routeParams.mode === 'c') {
            $scope.m = 'cs';
            $scope.modefull = 'Casual';
            $scope.mode_url = '/cs';
        } else if ($routeParams.mode === 'p') {
            $scope.m = 'acc';
            $scope.modefull = 'Public';
            $scope.mode_url = '/acc';
        }
        $scope.player = $routeParams.player;
        var url = BaseUrl + '/player/' + $routeParams.player + '/';
        $http({
            method: 'GET',
            url: url
        })
        .success(function(res) {
            console.log(res);
            $scope.s = res;
            $scope.$broadcast('playerLoaded', $scope.s.player_id);
            $scope.Math = $window.Math;
        })
        .error(function(res) {
            console.log(res);
            console.log('ERORROROROR');
        });
        $scope.mode = function(mode) {
            $scope.m = mode;
            $scope.$broadcast('playerLoaded', $scope.s.player_id);
            if (mode === 'cs') {
                $scope.modefull = 'Casual';
                $location.path('/c/player/' + $scope.nickname + '/', false);
            } else if (mode === 'acc') {
                $scope.modefull = 'Public';
                $location.path('/p/player/' + $scope.nickname + '/', false);
            } else {
                $scope.modefull = 'Ranked';
                $location.path('/player/' + $scope.nickname + '/', false);
            }
        };
        $scope.goplayer = function(){
            $scope.view = 'stats';
            $location.path($scope.mode_url + '/player/' + $scope.nickname + '/', false);
            $timeout(function(){
                $scope.$broadcast('playerLoaded');
            });
        };
        $scope.gochart = function(){
            $scope.view = 'chart';
            $location.path($scope.mode_url + '/player/' + $scope.nickname + '/chart/', false);
        };
        $scope.gohero = function(){
            $scope.view = 'hero';
            $location.path($scope.mode_url + '/player/' + $scope.nickname + '/hero/', false);
        };
        $scope.banner = function() {
            $scope.modalInstance = $modal.open({
                templateUrl: '/partials/banner_modal.html',
                scope: $scope
            });
        };
        $scope.close = function(){
            $scope.modelInstance.dismiss('cancel');
        };

    });
