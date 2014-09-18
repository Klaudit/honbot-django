'use strict';

angular.module('hbwww')
.directive('adsense', function() {

    return {
        restrict: 'A',
        scope: {
            slot: '='
        },
        templateUrl: 'partials/ad-big.html',
        controller: function(){
            (adsbygoogle = window.adsbygoogle || []).push({});
        }
    };
});
