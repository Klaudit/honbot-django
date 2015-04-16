import _ from 'lodash';

class PlayerCtrl {
    constructor($routeParams, ApiService, mode) {
        let vm = this;
        vm.m = mode;
        vm.s = {};
        vm.nickname = $routeParams.player;

        var filterMatches = function(matches) {
            var filtered = []
            console.log(matches)
            angular.forEach(matches, (value, key) => {
                filtered.push(_.find(value.players, 'player_id', vm.s.id))
            })
            console.log(filtered)
            vm.history = filtered;
        }

        ApiService.singlePlayer($routeParams.player).success(res => {
            vm.s = res;
            ApiService.history(res.id, mode).success(data => {
                filterMatches(data.result)

            });
        });
    }
}

PlayerCtrl.$inject = ['$routeParams', 'ApiService', 'mode'];

export default PlayerCtrl;