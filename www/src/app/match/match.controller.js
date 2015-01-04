'use strict';

function secondsToTime(secs) {
    var hours = Math.floor(secs / (60 * 60));

    var divisor_for_minutes = secs % (60 * 60);
    var minutes = Math.floor(divisor_for_minutes / 60);

    var divisor_for_seconds = divisor_for_minutes % 60;
    var seconds = Math.ceil(divisor_for_seconds);

    var obj = {
        'h': hours,
        'm': minutes,
        's': seconds
    };
    return obj;
}

angular.module('www').controller('MatchCtrl', function($scope, $routeParams, BaseUrl, $http, $rootScope, heroes, items, $filter, $log) {

    $scope.item_names = items;
    $scope.hero_names = heroes;
    $scope.ptips = {};
    $scope.pmmr = {};
    var matchmode = {
        1: ['rnk', 'Ranked'],
        2: ['cs', 'Casual'],
        3: ['acc', 'Public']
    };
    angular.forEach(['ldmg', 'hdmg'], function(i){
        $scope[i] = {
            color: {},
            data: {
                type: 'pie',
                columns: []
            },
            legend: {show: false},
            tooltip: {
                format: {
                    value: function(value) {
                        return value;
                    }
                }
            }
        };
    });
    $scope.totals = {};
    angular.forEach(['kills', 'deaths', 'xpm', 'cs', 'apm', 'gpm'], function(i){
        $scope.totals[i] = {
            color: {
                pattern: ['#27ae60', '#c0392b']
            },
            data: {
                type: 'donut',
                columns: []
            },
            donut: {label: {show: false}},
            size: {height: 135},
            legend: {show: false},
            tooltip: {
                format: {
                    value: function(value) {
                        return Math.floor(value);
                    }
                }
            }
        };
    });
    $scope.gpm = {
        color: {},
        data: {
            type: 'bar',
            columns: []
        },
        bar: {
            width: {
                ratio: 1
            }
        },
        padding: {left: 10},
        legend: {show: false},
        tooltip: {grouped: false},
        axis: {
            y: {show: false},
            x: {show: false}
        }
    };

    var t1 = 0,
        t2 = 0,
        lkills = 0,
        hkills = 0,
        ldeaths = 0,
        hdeaths = 0,
        lcs = 0,
        hcs = 0,
        lxpm = 0,
        hxpm = 0,
        lgpm = 0,
        hgpm = 0,
        lapm = 0,
        hapm = 0,
        tgpm = [],
        ldmg = [],
        hdmg = [],
        lcolors = [],
        hcolors = [],
        gpm = [],
        colors = [];

    var url = BaseUrl + '/match/' + $routeParams.match + '/';
    console.log(url);
    $http.get(url).success(function(res) {
        $scope.match = res;
        $scope.mode = matchmode[res.mode];
        $scope.len = secondsToTime($scope.match.length);

        if (t1 > t2) {
            $scope.winner = 'Legion';
        } else {
            $scope.winner = 'Hellbourne';
        }

        url = BaseUrl + '/ptip/?players=';

        $scope.match.players = $filter('orderBy')($scope.match.players, 'position');

        angular.forEach(res.players, function(p) {
            // calculate winning team
            if (p.discos !== 1) {
                if (p.team === 1) {
                    t1 += p.win;
                    ldmg.push([p.nickname, p.herodmg]);
                    lcolors.push($rootScope.pos_colors[p.position]);
                    lkills += p.kills;
                    ldeaths += p.deaths;
                    lapm += p.apm;
                    lcs += p.cs;
                    lgpm += p.gpm;
                    lxpm += p.xpm;
                } else {
                    t2 += p.win;
                    hdmg.push([p.nickname, p.herodmg]);
                    hcolors.push($rootScope.pos_colors[p.position]);
                    hkills += p.kills;
                    hdeaths += p.deaths;
                    hapm += p.apm;
                    hcs += p.cs;
                    hgpm += p.gpm;
                    hxpm += p.xpm;
                }
            }
            colors.push($rootScope.pos_colors[p.position]);
            gpm.push([p.nickname, p.gpm]);
            tgpm.push({
                name: p.nickname,
                data: [Math.floor(p.gpm)],
                color: $rootScope.pos_colors[p.position]
            });

            url += p.player_id + ',';
            $scope.ptips[p.player_id] = {
                'title': '<h4 class="ptiphead">' + p.nickname + '</h4>',
                'content': '<span class="ptip-warning">Stats not loaded</span><br>'
            };
            $scope.pmmr[p.player_id] = '';
        });
        $scope.ldmg.color.pattern = lcolors;
        $scope.hdmg.color.pattern = hcolors;
        $scope.gpm.color.pattern = colors;
        $scope.ldmg.data.columns = ldmg;
        $scope.hdmg.data.columns = hdmg;
        $scope.gpm.data.columns = gpm;
        $scope.totals.kills.data.columns = [['Legion', lkills],['Hellbourne', hkills]];
        $scope.totals.deaths.data.columns = [['Legion', ldeaths],['Hellbourne', hdeaths]];
        $scope.totals.xpm.data.columns = [['Legion', lxpm],['Hellbourne', hxpm]];
        $scope.totals.gpm.data.columns = [['Legion', lgpm],['Hellbourne', hgpm]];
        $scope.totals.apm.data.columns = [['Legion', lapm],['Hellbourne', hapm]];
        $scope.totals.cs.data.columns = [['Legion', lcs],['Hellbourne', hcs]];
        $log.debug(url);


        // get tooltips
        $http.get(url).success(function(res) {
            angular.forEach(res.result, function(player, key) {
                $scope.pmmr[player.id] = Math.floor(player[$scope.mode[0] + '_mmr']);
                $scope.ptips[player.id] = {
                    'title': '<h4 class="ptiphead"><img src="' + player.avatar + '" width=30> ' + player.nickname + '</h4>',
                    'content': '<h4 class="ptiphead"><span class="ptip-success">' + player[$scope.mode[0] + '_wins'] + ' </span> - <span class="ptip-warning"> ' + player[$scope.mode[0] + '_losses'] + '</span></h4>' +
                        '<strong>MMR</strong>: <span class="ptip-blue">' + Math.floor(player[$scope.mode[0] + '_mmr']) + '</span><br>' +
                        '<strong>KDR</strong>: ' + Math.round(player[$scope.mode[0] + '_kdr'] * 100) / 100 + '</span><br>' +
                        '<strong>APM</strong>: ' + Math.floor(player[$scope.mode[0] + '_avg_apm'])
                };
            });
        });
    });
});