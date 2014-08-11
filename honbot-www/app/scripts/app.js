'use strict';

angular
    .module('hb-www-app', [
        'ngCookies',
        'ngResource',
        'ngSanitize',
        'ngRoute',
        'percentage',
        'ui.bootstrap',
        'angular-loading-bar'
    ])
    .config(function($routeProvider, $locationProvider) {
        $locationProvider.html5Mode(true);
        $locationProvider.hashPrefix('!');
        $routeProvider
            .when('/', {
                templateUrl: '/views/home.html',
                controller: 'HomeController'
            })
            .when('/player/:player/', {
                templateUrl: '/views/player.html',
                controller: 'PlayerController'
            })
            .when('/:mode/player/:player/', {
                templateUrl: '/views/player.html',
                controller: 'PlayerController'
            })
            .when('/match/:match/', {
                templateUrl: '/views/match.html',
                controller: 'MatchController'
            })
            .otherwise({
                redirectTo: '/'
            });
    }).factory('BaseUrl', function() {
        if (document.location.host.split(':')[0] === '127.0.0.1') {
            return 'http://localhost:8000';
        } else {
            return 'http://api.honbot.com';
        }
    }).run(['$route', '$rootScope', '$location',
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
        }
    ]);
