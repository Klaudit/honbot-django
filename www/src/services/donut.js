/* jshint ignore:start */
'use strict';

angular.module('www').directive('donut', function(d3) {

    return {
        restrict: 'EA',
        scope: {
            data: '=',
            label: '@',
            focus: '='
        },
        link: function(scope, element, iAttrs) {

            function outerWidth(el){
              var width = el.offsetWidth;
              var style = getComputedStyle(el);
              width = width - parseInt(style.paddingLeft) - parseInt(style.paddingRight);
              return width;
            }

            var width = outerWidth(element[0].parentElement);
            var height = 135,
                radius = Math.min(width, height) / 2,
                data,
                g,
                arc;

            var color = ['#27ae60', '#c0392b'];

            var pie = d3.layout.pie()
                .sort(null)
                .value(function(d) {
                    return d.total;
                });

            var svg = d3.select(element[0]).append("svg")
                .attr("width", width)
                .attr("height", height)
                .append("g");

            var tip = d3.tip()
                .attr('class', 'd3-tip')
                .html(function(d) {
                    return "<strong>" + d.nickname + ":</strong><span class='gold'> " + Math.floor(d.gpm) + "</span>";
                })

            // watch for data changes and re-render
            scope.$watch('data', function(newVals, oldVals) {
                if (!newVals) return;
                data = newVals;
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
                return scope.render();
            }, true);


            angular.element(window).on('resize', function(){
                if(width === outerWidth(element[0].parentElement)) return;
                scope.render();
            });

            scope.render = function() {
                svg.call(tip);
                width = outerWidth(element[0].parentElement);
                radius = Math.min(width, height) / 2;
                arc = d3.svg.arc()
                        .outerRadius(radius - 10)
                        .innerRadius(radius - 30);
                svg.attr("width", width)
                   .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");


                svg.selectAll(".arc").remove()
                g = svg.selectAll(".arc")
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
