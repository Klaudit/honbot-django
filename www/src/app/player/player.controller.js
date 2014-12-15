'use strict';

angular.module('www').controller('PlayerCtrl', function($scope, $routeParams, $http, BaseUrl, $location, $modal, $timeout, $window, $log, $alert) {
    if ($routeParams.view === undefined) {
        $scope.view = 'stats';
    } else if ($routeParams.view === 'chart') {
        $scope.view = 'chart';
    } else if ($routeParams.view === 'hero') {
        $scope.view = 'hero';
    }
    $scope.nickname = $routeParams.player;
    if ($routeParams.mode === undefined) {
        $scope.m = 'rnk';
        $scope.modefull = 'Ranked';
        $scope.mode_url = '';
    } else if ($routeParams.mode === 'c') {
        $scope.m = 'cs';
        $scope.modefull = 'Casual';
        $scope.mode_url = '/c';
    } else if ($routeParams.mode === 'p') {
        $scope.m = 'acc';
        $scope.modefull = 'Public';
        $scope.mode_url = '/p';
    }
    $scope.player = $routeParams.player;
    var url = BaseUrl + '/player/' + $routeParams.player + '/';
    $http.get(url).success(function(res) {
        $log.debug(res);
        $scope.s = res;
        $scope.Math = $window.Math;
        if(res.fallback){
            $alert({
                title: 'Fallback:',
                content: 'Stats were not updated as the API is unreachable or something.',
                container: '#alerts-container',
                type: 'info'
            });
        }
    }).error(function(res) {
        $log.debug(res);
        $alert({
            title: 'ERROR!',
            content: 'The API may be down, the player was banned, or never existed.',
            container: '#alerts-container',
            type: 'danger'
        });
    });
    $scope.mode = function(mode) {
        $scope.m = mode;
        if (mode === 'cs') {
            $scope.mode_url = '/c';
            $scope.modefull = 'Casual';
        } else if (mode === 'acc') {
            $scope.modefull = 'Public';
            $scope.mode_url = '/p';
        } else {
            $scope.mode_url = '';
            $scope.modefull = 'Ranked';
        }
        if ($scope.view !== 'stats') {
            $location.path($scope.mode_url + '/player/' + $scope.nickname + '/' + $scope.view + '/', false);
        } else {
            $location.path($scope.mode_url + '/player/' + $scope.nickname + '/', false);
        }
    };
    $scope.goplayer = function() {
        $scope.view = 'stats';
        $location.path($scope.mode_url + '/player/' + $scope.nickname + '/', false);
    };
    $scope.gochart = function() {
        $scope.view = 'chart';
        $location.path($scope.mode_url + '/player/' + $scope.nickname + '/chart/', false);
    };
    $scope.gohero = function() {
        $scope.view = 'hero';
        $location.path($scope.mode_url + '/player/' + $scope.nickname + '/hero/', false);
    };
    $scope.banner = function() {
        $scope.modalInstance = $modal.open({
            templateUrl: '/partials/banner_modal.html',
            scope: $scope
        });
    };
    $scope.close = function() {
        $scope.modelInstance.dismiss('cancel');
    };

});