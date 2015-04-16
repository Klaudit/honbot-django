class ApiService {

    constructor($http, BaseUrl) {


        this.host = BaseUrl.host;
        this.$http = $http;
        this.players = {};

    }
    get serverStats() {
        return this.$http.get(`${this.host}/stats/`).success(res => {
            if (res.success >= res.failure) {
                res.status = true;
            } else {
                res.status = false;
            }
        });
    }
    singlePlayer(nickname) {
        if (!this.players[nickname]) {
            this.players[nickname] = this.$http.get(`${this.host}/player/${nickname}/`);
        }
        return this.players[nickname];
    }
    history(pid, mode) {
        if(this.currentHistory && this.currentHistory === this.mostRecent){
            this.currentPage += 1;
        } else {
            this.currentPage = 1;
            this.currentHistory = pid;
        }
        return this.$http.get(`${this.host}/history/${pid}/${this.currentPage}/${mode}/`);
    }
}

ApiService.$inject = ['$http', 'BaseUrl'];

export default ApiService;