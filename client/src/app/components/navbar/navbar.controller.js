class NavbarCtrl {
    constructor($location) {
        let vm = this;

        vm.search = function() {
            if (vm.nick) {
                $location.path(`/player/${vm.nick}/`);
            }
        };
    }
}

NavbarCtrl.$inject = ['$location'];

export default NavbarCtrl;