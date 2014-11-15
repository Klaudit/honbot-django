/* jshint ignore:start */
'use strict';

angular.module('www').directive('pie', function(d3, _) {

    return {
        restrict: 'EA',
        scope: {
            data: '=',
            label: '@',
            team: '='
        },
        link: function(scope, element, iAttrs) {

            var width = d3.select(element[0])[0][0].parentElement.clientWidth;
            var height = 250,
                radius = Math.min(width, height) / 2;

            var color = scope.$root.pos_colors;

            var arc = d3.svg.arc()
                .outerRadius(radius - 10);

            var pie = d3.layout.pie()
                .sort(null)
                .value(function(d) {
                    return d.herodmg;
                });

            var svg = d3.select(element[0]).append("svg")
                .attr("width", width)
                .attr("height", height)
                .append("g")
                .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

            var tip = d3.tip()
                .attr('class', 'd3-tip')
                .offset([18, 0])
                .html(function(d, total) {
                    return "<strong>" + d.data.nickname + ":</strong><span class='gold'> " + d.value + "</span> " + Math.floor((d.value / total) * 100) + '%';
                })

            // watch for data changes and re-render
            scope.$watch('data', function(newVals, oldVals) {
                return scope.render(newVals);
            }, true);

            scope.render = function(data) {

                svg.selectAll('*').remove();
                svg.call(tip);
                if (!data) return;
                var t1 = 0, t2 = 0;
                data = _.groupBy(data, function(d){ return d.team })[scope.team];
                var total = d3.sum(data, function(d) { return d.herodmg; });

                var g = svg.selectAll(".arc")
                    .data(pie(data))
                    .enter().append("g")
                    .attr("class", "arc");

                g.append("path")
                    .attr("d", arc)
                    .attr("fill", function(d) {
                        return color[d.data.position];
                    })
                    .attr("originalfill", function(d) {
                        return color[d.data.position];
                    })
                    .on('mouseover', function(d) {
                        tip.show(d, total);
                        d3.select(this).style("fill", d3.rgb(this.attributes.fill.value).brighter());
                    })
                    .on("mouseout", function(d) {
                        tip.hide(d, total);
                        d3.select(this).style("fill", this.attributes.originialfill);
                    });

            };
        }
    };
});

/* jshint ignore:end */
