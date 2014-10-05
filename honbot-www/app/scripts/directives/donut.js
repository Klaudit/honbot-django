/* jshint ignore:start */
'use strict';

angular.module('hbwww').directive('donut', function(d3) {

    return {
        restrict: 'EA',
        scope: {
            data: '=',
            label: '@',
            focus: '='
        },
        link: function(scope, element, iAttrs) {

            var width = d3.select(element[0])[0][0].parentElement.clientWidth;
            var height = 135,
                radius = Math.min(width, height) / 2;

            var color = ['#27ae60', '#c0392b'];

            var arc = d3.svg.arc()
                .outerRadius(radius - 10)
                .innerRadius(radius - 40);

            var pie = d3.layout.pie()
                .sort(null)
                .value(function(d) {
                    return d.total;
                });

            var svg = d3.select(element[0]).append("svg")
                .attr("width", width)
                .attr("height", height)
                .append("g")
                .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

            var tip = d3.tip()
                .attr('class', 'd3-tip')
                .html(function(d) {
                    return "<strong>" + d.nickname + ":</strong><span class='gold'> " + Math.floor(d.gpm) + "</span>";
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
                angular.forEach(data, function(d){
                    if(d.team===1){
                        t1 += d[scope.focus];
                    } else {
                        t2 += d[scope.focus];
                    }
                });
                data = [
                    {
                        team: 0,
                        name: 'L',
                        total: t1
                    }, {
                        team: 1,
                        name: 'H',
                        total: t2
                    }
                ]

                var g = svg.selectAll(".arc")
                    .data(pie(data))
                    .enter().append("g")
                    .attr("class", "arc");

                g.append("path")
                    .attr("d", arc)
                    .style("fill", function(d) {
                        return color[d.data.team];
                    });

            };
        }
    };
});

/* jshint ignore:end */
