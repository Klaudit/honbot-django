import MainCtrl from './main/main.controller';
import NavbarCtrl from './components/navbar/navbar.controller';
import PlayerCtrl from './player/player.controller';
import BaseUrl from './services/baseurl';
import ApiService from './services/api.service';
import largeHero from './largeHero';

angular.module('client', ['ngRoute', 'mgcrea.ngStrap', 'angularMoment'])
    .controller('MainCtrl', MainCtrl)
    .controller('NavbarCtrl', NavbarCtrl)
    .controller('PlayerCtrl', PlayerCtrl)
    .service('BaseUrl', BaseUrl)
    .service('ApiService', ApiService)
    .constant('largeHero', largeHero)
    .config(['$routeProvider', '$locationProvider', AppController]);


function AppController($routeProvider, $locationProvider) {
    $locationProvider.html5Mode(true).hashPrefix('!');
    $routeProvider
        .when('/', {
            templateUrl: 'app/main/main.html',
            controller: 'MainCtrl',
            controllerAs: 'main',
        })
        .when('/player/:player/', {
            templateUrl: 'app/player/player.html',
            controller: 'PlayerCtrl',
            controllerAs: 'ctrl',
            resolve: {
                mode: () => {
                    return 'rnk';
                },
            }
        })
        .when('/c/player/:player/', {
            templateUrl: 'app/player/player.html',
            controller: 'PlayerCtrl',
            controllerAs: 'ctrl',
            resolve: {
                mode: () => {
                    return 'cs';
                },
            }
        })
        .when('/p/player/:player/', {
            templateUrl: 'app/player/player.html',
            controller: 'PlayerCtrl',
            controllerAs: 'ctrl',
            resolve: {
                mode: () => {
                    return 'acc';
                },
            }
        })
        .otherwise({
            redirectTo: '/'
        });
}