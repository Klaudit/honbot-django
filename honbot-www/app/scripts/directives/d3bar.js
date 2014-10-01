/* jshint ignore:start */
'use strict';

angular.module('hbwww').directive('d3Bars', ['d3',
    function(d3) {
        return {
            restrict: 'EA',
            scope: {
                data: '=',
                label: '@'
            },
            link: function(scope, iElement, iAttrs) {

                var margin = {
                        top: 0,
                        right: 80,
                        bottom: 0,
                        left: 90
                    };
                var width = d3.select(iElement[0])[0][0].parentElement.clientWidth - margin.left - margin.right;
                var height = 350 - margin.top - margin.bottom;

                var x = d3.scale.ordinal().rangeRoundBands([0, width], 0.1);

                var y = d3.scale.linear().range([height, 0]);

                var svg = d3.select(iElement[0]).append("svg")
                    .attr("width", width + margin.left + margin.right)
                    .attr("height", height + margin.top + margin.bottom)
                    .append("g");

                var tip = d3.tip()
                  .attr('class', 'd3-tip')
                  .html(function(d) {
                    return "<strong>" + d.nickname + ":</strong> " + Math.floor(d.gpm);
                  })

                // on window resize, re-render d3 canvas
                window.onresize = function() {
                    return scope.$apply();
                };
                scope.$watch(function() {
                    return angular.element(window)[0].innerWidth;
                }, function() {
                    width = d3.select(iElement[0])[0][0].parentElement.clientWidth;
                    d3.select(iElement[0]).selectAll("svg").attr("width", width);
                    x = d3.scale.ordinal().rangeRoundBands([0, width], 0.15);
                    return scope.render(scope.data);
                });

                // watch for data changes and re-render
                scope.$watch('data', function(newVals, oldVals) {
                    return scope.render(newVals);
                }, true);

                // define render function
                scope.render = function(data) {
                    // remove all previous items before render
                    svg.selectAll('*').remove();
                    svg.call(tip)
                    if (!data) return;
                    x.domain(data.map(function(d) {
                        return d.nickname;
                    }));
                    y.domain([0, d3.max(data, function(d) {
                        return d.gpm;
                    })]);

                    svg.selectAll(".bar")
                        .data(data)
                        .enter().append("rect")
                        .attr("class", "bar")
                        .attr("fill", function(d) {
                            return scope.$root.pos_colors[d.position];
                        })
                        .attr("x", function(d) {
                            return x(d.nickname);
                        })
                        .attr("width", x.rangeBand())
                        .attr("y", function(d) {
                            return y(d.gpm);
                        })
                        .attr("height", function(d) {
                            return height - y(d.gpm);
                        })
                        .on('mouseover', tip.show)
                        .on('mouseout', tip.hide);

                };
            }
        };
    }
]);

/* jshint ignore:end */
