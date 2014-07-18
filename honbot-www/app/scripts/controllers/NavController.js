'use strict';

angular.module('hb-www-app')
  .controller('NavController', function ($scope, $location) {
    $scope.search = function(){
        if ($scope.nick) {
            $location.path('/player/'+encodeURIComponent($scope.nick)+'/');
        }
     };
 
  });
