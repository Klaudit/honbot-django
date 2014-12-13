'use strict';

angular.module('www').controller('ChartCtrl', function($scope, $http, BaseUrl, _) {
    $scope.$watchGroup(['s', 'm'], function(){
        $scope.url = BaseUrl + '/cache/' + $scope.s._id + '/' + $scope.m;
        $http.get($scope.url).success(function(res){
            if(res.matches !== 0){
                $scope.a = res.result;
                $scope.run();
            }
        });
    });

    $scope.run = function(){
        $scope.playermatches = [];
        angular.forEach($scope.a, function(val){
            $scope.playermatches.push(_.findWhere(val.players, {id: $scope.s._id}));
        });
        $scope.avg = _.reduce($scope.playermatches, function(memo, val){ return memo + val.apm; }, 0);
    };
});
