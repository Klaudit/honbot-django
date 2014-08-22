'use strict';

angular.module('hbwww')
    .controller('NavController', function($scope, $location) {
        $scope.search = function() {
            if ($scope.nick) {
                $location.path('/player/' + $scope.nick + '/');
            }
        };

    });
