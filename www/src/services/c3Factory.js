'use strict';

angular.module('www').service('c3SimpleService', function() {
    return {};
}).directive('c3Chart', ['c3SimpleService', function(c3SimpleService) {
    return {
        // this directive can be used as an Element or an Attribute
        restrict: 'EA',
        scope: {
            // setting config attribute to isolated scope
            // config object is 1:1 configuration C3.js object, for avaiable options see: http://c3js.org/examples.html
            config: '='
        },
        template: '<div></div>',
        replace: true,
        link: function(scope, element, attrs) {

            // binding chart to element with provided ID
            var bindto = '#' + attrs.id;
            var config = scope.config;

            //Generating the chart on every data change
            scope.$watch('config.data.columns', function(newSeries, oldSeries) {
                if(newSeries === undefined || config.data.columns.length === 0){return;}
                config.data.columns = newSeries;

                // adding (or overwriting) chart to service c3SimpleService
                // we are regenerating chart on each change - this might seem slow and unefficient
                // but works pretty well and allows us to have more controll
                config.bindto = bindto;
                c3SimpleService[bindto] = c3.generate(config);

                // if there is no size specified, we are assuming, that chart will have width
                // of its container (proportional of course) - great for responsive design
                if (!config.size) {
                    c3SimpleService[bindto].resize();
                }
            });
        }
    };
}]);