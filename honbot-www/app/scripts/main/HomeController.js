'use strict';

angular.module('hbwww').controller('HomeController', function($scope, $routeParams, $http, BaseUrl, $location) {
    var number = 1 + Math.floor(Math.random() * 548);
    $scope.image = 'images/largehero/hero_' + number + '.png';
    $scope.search = function() {
        $scope.status = {};
        if ($scope.nickname) {
            $location.path('/player/' + $scope.nickname + '/');
        }
    };
});
