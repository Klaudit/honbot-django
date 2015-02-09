'use strict';

angular.module('www').controller('MainCtrl', function($scope, $routeParams, $http, BaseUrl, $location, _) {
    $scope.image = 'assets/images/largehero/hero_' + _.random(1, 548) + '.png';

    $http.get(BaseUrl + '/stats/').success(function(res){
        $scope.stats = res;
        if(res.success >= res.failure){
            $scope.status = true;
        } else {
            $scope.status = false;
        }
    });

    $scope.search = function() {
        if ($scope.nickname) {
            $location.path('/player/' + $scope.nickname + '/');
        }
    };
});
