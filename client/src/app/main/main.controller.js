import _ from 'lodash';

class MainCtrl {
    constructor($scope, $http, $location, largeHero, $interval, ApiService) {

        let vm = this;

        // set background image
        var image = largeHero[_.random(1, largeHero.length)];
        vm.jumbostyle = {
            'background-image': `url(${image})`
        };

        vm.search = function() {
            if (vm.nickname) {
                $location.path(`/player/${vm.nickname}/`);
            }
        };

        var getStats = function() {
            ApiService.serverStats.success(res => {vm.stats = res;});
        };
        getStats();
        var statsInterval = $interval(getStats, 2000, 0, false);

        $scope.$on('$destroy', function() {
            $interval.cancel(statsInterval);
        });
    }
}

MainCtrl.$inject = ['$scope', '$http', '$location', 'largeHero', '$interval', 'ApiService'];

export default MainCtrl;