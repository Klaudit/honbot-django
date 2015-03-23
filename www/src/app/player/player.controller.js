'use strict';

angular.module('www').controller('PlayerCtrl', function($scope, $routeParams, $http, BaseUrl, $location, $modal, $timeout, $window, $log, $alert, view) {
    $scope.s = {};
    if (view === 'chart' || view === 'hero') {
        $scope.view = view;
    } else {
        $scope.view = 'stats';
    }
    var modetranslate = {
        'undefined': 'rnk',
        'ranked': 'rnk',
        'casual': 'cs',
        'public': 'acc'
    };
    $scope.nickname = $routeParams.player;
    $scope.mode = $routeParams.mode || 'ranked';
    $scope.m = modetranslate[$scope.mode];
    $scope.player = $routeParams.player;
    var url = BaseUrl + '/player/' + $routeParams.player + '/';
    $http.get(url).success(function(res) {
        $log.debug(res);
        $scope.s = res;
        $scope.Math = $window.Math;
        if (res.fallback) {
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
    $scope.changelocation = function(mode) {
        $scope.mode = mode;
        $scope.m = modetranslate[$scope.mode];
        var view;
        if ($scope.view === 'stats') {
            view = '/player/';
        } else {
            view = '/' + $scope.view + '/';
        }
        if (mode !== 'ranked') {
            $location.path(view + $scope.nickname + '/' + mode + '/', false);
        } else {
            $location.path(view + $scope.nickname + '/', false);
        }
    };
    $scope.changeview = function(view) {
        $scope.view = view;
        $scope.changelocation($scope.mode);
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