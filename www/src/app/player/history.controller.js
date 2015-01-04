'use strict';

angular.module('www').controller('PlayerHistoryCtrl', function($scope, $http, BaseUrl, $location, $timeout, $log, _) {
    $scope.currentcount = 0;
    $scope.history = [];
    $scope.more = function(){
        if($scope.s.id === undefined){return;}
        $scope.currentcount += 1;
        $scope.url = BaseUrl + '/history/' + $scope.s.id + '/' + $scope.currentcount + '/' + $scope.m + '/';
        $http({
            method: 'GET',
            url: $scope.url,
            cache: true
        })
        .success(function(res) {
            $log.debug(res);
            if(res.matches === 0){$scope.nomore = true; return;}
            var hist = [];
            angular.forEach(res.result, function(value, key) {
                var t = _.find(value.players, function(p){return p.player_id === $scope.s.id;});
                t.date = value.date;
                this.push(t);
            }, hist);
            $scope.history = $scope.history.concat(hist.reverse());
            if(res.length < 25){
                $scope.nomore = true;
            }
        });
    };

    $scope.goMatch = function(id){
        $location.path('/match/' + id + '/');
    };
    $scope.$watch('s', function() {
        $scope.more();
    });
    $scope.$watch('m', function() {
        $scope.currentcount = 0;
        $scope.history = [];
        $scope.more();
    });
});
