'use strict';

angular.module('hbwww', [
    'ngAnimate',
    'ngCookies',
    'ngTouch',
    'ngSanitize',
    'ngRoute',
    'percentage',
    'angular-loading-bar',
    'mgcrea.ngStrap',
    'angularMoment'])
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
            .otherwise({
                redirectTo: '/'
            });
    })
    .factory('BaseUrl', function($location, $rootScope) {
        if ($location.host().split(':')[0] === 'localhost') {
            $rootScope.BaseUrl = 'http://localhost:8000';
            return 'http://localhost:8000';
        } else {
            $rootScope.BaseUrl = 'http://api.honbot.com';
            return 'http://api.honbot.com';
        }
    })
    .run(['$route', '$rootScope', '$location', '$http', 'BaseUrl', '$sce',
        function($route, $rootScope, $location, $http, BaseUrl) {
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

            // load in some default hon stuff
            $rootScope.pos_colors = ['#002c9f', '#00c19e', '#770092', '#f2d500', '#ff7d29', '#ff44ab', '#727272', '#00a0da', '#006448', '#562507'];
            $http({
                method: 'GET',
                url: BaseUrl + '/item/',
                cache: true
            })
            .success(function(res) {
                $rootScope.item_names = {};
                angular.forEach(res, function(value) {
                    $rootScope.item_names[value.id] = {
                        'name': value.name,
                        'cli_name': value.cli_name,
                        'cost': value.cost,
                        'description': value.description
                    };
                });
            });
            $http({
                method: 'GET',
                url: 'scripts/data/heroes.json'
            })
            .success(function(res) {
                $rootScope.hero_names = res;
            });
        }
    ]);


