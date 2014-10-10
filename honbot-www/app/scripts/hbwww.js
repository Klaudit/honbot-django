'use strict';

angular.module('hbwww', [
    'ngAnimate',
    'ngRoute',
    'ngSanitize',
    'percentage',
    'angular-loading-bar',
    'angularMoment',
    'mgcrea.ngStrap'])
    .config(function($routeProvider, $locationProvider) {
        $locationProvider.html5Mode(true).hashPrefix('!');
        $routeProvider
            .when('/', {
                templateUrl: 'partials/home.html',
                controller: 'HomeController'
            })
            .when('/player/:player/', {
                templateUrl: 'partials/player.html',
                controller: 'PlayerController'
            })
            .when('/:mode/player/:player/', {
                templateUrl: 'partials/player.html',
                controller: 'PlayerController'
            })
            .when('/match/:match/', {
                templateUrl: 'partials/match.html',
                controller: 'MatchController'
            })
            .when('/items/', {
                templateUrl: 'partials/items.html',
                controller: 'ItemsController'
            })
            .when('/player/:player/:view/', {
                templateUrl: 'partials/player.html',
                controller: 'PlayerController'
            })
            .when('/:mode/player/:player/:view/', {
                templateUrl: 'partials/player.html',
                controller: 'PlayerController'
            })
            .otherwise({
                redirectTo: '/'
            });
    })
    .factory('BaseUrl', function($location, $rootScope) {
        if ($location.host().split(':')[0] === 'localhost') {
            $rootScope.BaseUrl = '//localhost:8000';
            return '//localhost:8000';
        } else {
            $rootScope.BaseUrl = '//api.honbot.com';
            return '//api.honbot.com';
        }
    })
    .run(['$route', '$rootScope', '$location',
        function($route, $rootScope, $location) {
            // this lets the path change without reloading route
            var original = $location.path;
            $location.path = function(path, reload) {
                if (reload === false) {
                    var lastRoute = $route.current;
                    var un = $rootScope.$on('$locationChangeSuccess', function() {
                        $route.current = lastRoute;
                        un();
                    });
                }
                return original.apply($location, [path]);
            };

            $rootScope.pos_colors = ['#002c9f', '#00c19e', '#770092', '#f2d500', '#ff7d29', '#ff44ab', '#727272', '#00a0da', '#006448', '#562507'];
        }
    ]);


