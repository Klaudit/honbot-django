'use strict';

angular.module('www').controller('MainCtrl', function($scope, $routeParams, $http, BaseUrl, $location, _) {
    $scope.image = 'assets/images/largehero/hero_' + _.random(1, 548) + '.png';

    $http.get(BaseUrl + '/collection_count/')
        .success(function(res){
            $scope.collection = res;
        });

    $scope.search = function() {
        $scope.status = {};
        if ($scope.nickname) {
            $location.path('/player/' + $scope.nickname + '/');
        }
    };
});
