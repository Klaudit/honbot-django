'use strict';

angular.module('hbwww').controller('HomeController', function($scope, $routeParams, $http, BaseUrl, $location) {
    $scope.search = function() {
        $scope.status = {};
        if ($scope.nickname) {
            $location.path('/player/' + $scope.nickname + '/');
        }
    };
});
