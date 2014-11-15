/* jshint ignore:start */
'use strict';

angular.module('www').directive('gpm', function(d3) {
    return {
        restrict: 'EA',
        scope: {
            data: '=',
            label: '@'
        },
        link: function(scope, element, iAttrs) {

            var width = element.width();

            var height = 350;

            var x = d3.scale.ordinal().rangeRoundBands([0, width], 0.1);

            var y = d3.scale.linear().range([height, 0]);

            var svg = d3.select(element[0]).append("svg")
                .attr("width", width)
                .attr("height", height);

            var tip = d3.tip()
                .attr('class', 'd3-tip')
                .html(function(d) {
                    return "<strong>" + d.nickname + ":</strong><span class='gold'> " + Math.floor(d.gpm) + "</span>";
                })

            // watch for data changes and re-render
            scope.$watch('data', function(newVals, oldVals) {
                return scope.render(newVals);
            }, true);

            // define render function
            scope.render = function(data) {
                // remove all previous items before render
                svg.selectAll('*').remove();
                svg.call(tip);
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
                    .attr("originalfill", function(d) {
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
                    .on('mouseover', function(d) {
                        tip.show(d);
                        d3.select(this).style("fill", d3.rgb(this.attributes.fill.value).brighter());
                    })
                    .on("mouseout", function(d) {
                        tip.hide(d);
                        d3.select(this).style("fill", this.attributes.originialfill);
                    });

            };
        }
    };
});

/* jshint ignore:end */
