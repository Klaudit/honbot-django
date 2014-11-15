'use strict';

angular.module('www').controller('PlayerHistoryCtrl', function($scope, $http, BaseUrl, $location, $timeout, $log, _) {
    $scope.currentcount = 0;
    $scope.history = [];
    $scope.more = function(){
        if(!$scope.s._id){return;}
        $scope.currentcount += 1;
        // TODO: disable additional calls of more here
        $scope.url = BaseUrl + '/history/' + $scope.s._id + '/' + $scope.currentcount + '/' + $scope.m + '/';
        $http({
            method: 'GET',
            url: $scope.url,
            cache: true
        })
        .success(function(res) {
            $log.debug(res);
            if(res.matches === 0){$scope.nomore = true; return;}
            var hist = [];
            angular.forEach(res.result, function(value) {
                var t = _.find(value.players, function(p){return p.id === $scope.s._id;});
                t._id = value._id;
                t.date = value.date;
                this.push(t);
            }, hist);
            $scope.history = $scope.history.concat(hist.reverse());
            if(res.length < 25){
                $scope.nomore = true;
            }
            // TODO: enable more() again
        });
    };
    $scope.goMatch = function(_id){
        $location.path('/match/' + _id + '/');
    };
    $scope.$on('playerLoaded', function(){
        $scope.more();
    });
    $scope.more();
});
