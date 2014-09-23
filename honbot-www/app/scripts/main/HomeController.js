'use strict';

angular.module('hbwww').controller('HomeController', function($scope, $routeParams, $http, BaseUrl, $location) {
    $scope.image = 'images/heroes/10/ability1_128.jpg';
    $scope.search = function() {
        $scope.status = {};
        if ($scope.nickname) {
            $location.path('/player/' + $scope.nickname + '/');
        }
    };
});
