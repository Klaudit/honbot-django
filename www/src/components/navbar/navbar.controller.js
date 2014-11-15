'use strict';

angular.module('www')
    .controller('NavController', function($scope, $location) {
        $scope.navbarCollapsed = true;
        $scope.search = function() {
            if ($scope.nick) {
                $location.path('/player/' + $scope.nick + '/');
            }
        };

    });
