'use strict';

angular.module('www').controller('ChartCtrl', function($scope, $http, BaseUrl, _, $alert, $log) {
    $scope.mmr = {
        color: {},
        data: {
            x: 'x',
            type: 'line',
            columns: []
        },
        legend: {show: false},
        tooltip: {
            format: {
                value: function(value) {
                    return value;
                }
            }
        },
        axis: {
            x: {
                type: 'category',
                show: false
            }
        }
    };

    $scope.$watchGroup(['s', 'm'], function() {
        $scope.url = BaseUrl + '/cache/' + $scope.s._id + '/' + $scope.m;
        $http.get($scope.url).success(function(res) {
            $log.debug(res);
            if (res.matches !== 0) {
                $scope.a = res.result;
                $scope.run();
            } else {
                $alert({
                    title: 'No Matches!',
                    content: 'The database returned zero (0) matches. Go back to the player stats page and try to load new matches.',
                    container: '#alerts-container',
                    type: 'danger'
                });
            }
        });
    });

    $scope.run = function() {
        $scope.playermatches = [];
        var mmr = ['matches', $scope.s[$scope.m + '_mmr']],
            mid = ['x'],
            current = $scope.s[$scope.m + '_mmr'];
        angular.forEach($scope.a, function(val) {
            mid.push(val._id);
            $scope.playermatches.push(_.findWhere(val.players, {id: $scope.s._id}));
        });
        angular.forEach($scope.playermatches, function(val) {
            mmr.push(current - val.mmr_change);
            current = current - val.mmr_change;
        });
        $scope.mmr.data.columns = [mid, mmr];
        $scope.avg = _.reduce($scope.playermatches, function(memo, val) {return memo + val.apm;}, 0) / $scope.a.length;
    };
});