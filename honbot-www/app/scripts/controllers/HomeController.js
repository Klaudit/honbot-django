'use strict';

angular.module('hb-www-app')
  .controller('HomeController', function ($scope, $routeParams, $http, BaseUrl, $location) {
    $scope.search = function(){
        if ($scope.nickname) {
            $location.path('/player/'+$scope.nickname+'/');
        }
    };
  });
