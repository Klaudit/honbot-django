class BaseUrl {
    constructor($location) {
        if ($location.host() === 'localhost') {
            this.host = '//localhost:5000';
        } else {
            this.host = '//api.honbot.com';
        }
    }
}

BaseUrl.$inject = ['$location'];

export default BaseUrl;