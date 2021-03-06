'use strict';

angular.module('www', [
        'ngAnimate',
        'ngRoute',
        'percentage',
        'angular-loading-bar',
        'angularMoment',
        'ngRaven',
        'mgcrea.ngStrap'
    ])
    .config(function($routeProvider, $locationProvider, $sceDelegateProvider) {
        $locationProvider.html5Mode(true).hashPrefix('!');
        $sceDelegateProvider.resourceUrlWhitelist([
            'self',
            '**'
        ]);
        $routeProvider
            .when('/', {
                templateUrl: 'app/main/main.html',
                controller: 'MainCtrl'
            })
            .when('/match/:match/', {
                templateUrl: 'app/match/match.html',
                controller: 'MatchCtrl'
            })
            .when('/items/', {
                templateUrl: 'partials/items.html',
                controller: 'ItemsCtrl'
            })
            .when('/player/:player/', {
                templateUrl: 'app/player/player.html',
                controller: 'PlayerCtrl',
                resolve: {
                    view: function(){return 'stats';}
                }
            })
            .when('/player/:player/:mode/', {
                templateUrl: 'app/player/player.html',
                controller: 'PlayerCtrl',
                resolve: {
                    view: function(){return 'stats';}
                }
            })
            .when('/chart/:player/', {
                templateUrl: 'app/player/player.html',
                controller: 'PlayerCtrl',
                resolve: {
                    view: function(){return 'chart';}
                }
            })
            .when('/chart/:player/:mode/', {
                templateUrl: 'app/player/player.html',
                controller: 'PlayerCtrl',
                resolve: {
                    view: function(){return 'chart';}
                }
            })
            .otherwise({
                redirectTo: '/'
            });
    })
    .factory('BaseUrl', function($location) {
        if ($location.host().split(':')[0] === 'localhost') {
            return '//localhost:5000';
        } else {
            return '//api.honbot.com';
        }
    })
    .run(function($route, $rootScope, $location, BaseUrl) {
            // this lets the path change without reloading route
            var original = $location.path;
            $rootScope.BaseUrl = BaseUrl;
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
    );
