// damage graph render
//             angular.forEach(['l', 'h'], function(c){
//                 angular.element(document).find(c +'dmg')[0].highcharts({
//                     chart: {
//                         backgroundColor: null,
//                         plotBackgroundColor: null,
//                         plotBorderWidth: null,
//                         plotShadow: false
//                     },
//                     plotOptions: {
//                         pie: {
//                             allowPointSelect: true,
//                             cursor: 'pointer',
//                             animation: false,
//                             borderColor: '#303030',
//                             dataLabels: {
//                                 enabled: true,
//                                 style: {color: '#eeeeee'},
//                                 formatter: function() {
//                                     return '<strong>'+ this.point.name +'</strong>: '+ Math.round(this.percentage) + '%';
//                                 }
//                             }
//                         }
//                     },
//                     title: {
//                         text: ''
//                     },
//                     colors: d[c + 'color'],
//                     credits: {
//                         enabled: false
//                     },
//                     exporting: {
//                         enabled: false
//                     },
//                     series: [{
//                         type: 'pie',
//                         name: 'Damage',
//                         data: d[c]
//                     }]
//                 });
//             });


//             gpm bar graph
//             angular.element($document.getElementById('tgpm')).highcharts({
//                 chart: {
//                     type: 'column',
//                     backgroundColor: null
//                 },
//                 title: {
//                     text: ''
//                 },
//                 xAxis: {
//                     categories: ['']
//                 },
//                 yAxis: {
//                     min: 0,
//                     title: {
//                         enabled: false
//                     },
//                     gridLineColor: '#4f4c50'
//                 },
//                 tooltip: {
//                     followPointer: true,
//                     hideDelay: 50,
//                     formatter: function() {
//                         return this.y;
//                     }
//                 },
//                 legend: {
//                     borderWidth: 0,
//                     itemStyle: {
//                         color: '#64656d'
//                     },
//                     itemHoverStyle: {
//                         color: '#FFF'
//                     }
//                 },
//                 plotOptions: {
//                     column: {
//                         pointPadding: 0.1,
//                         borderWidth: 0,
//                         groupPadding: 0,
//                         animation: false
//                     }
//                 },
//                 exporting: {
//                     enabled: false
//                 },
//                 credits: {
//                     enabled: false
//                 },
//                 series: tgpm
//             });

//             // donut charts
//             angular.forEach(['kills', 'assists', 'xpm', 'creeps', 'gpm', 'apm'], function(c){
//                 var e = $document.getElementById(c);
//                 angular.element(e).highcharts({
//                     chart: {
//                         type: 'pie',
//                         backgroundColor: null,
//                         plotBackgroundColor: null,
//                         plotBorderWidth: null,
//                         plotShadow: false
//                     },
//                     title: {
//                         text: c,
//                         style: {
//                             color: '#c8c4cb',
//                             font: 'bold 16px "Helvetica Neue", Helvetica, sans-serif'
//                         }
//                     },
//                     plotOptions: {
//                         pie: {
//                             borderColor: '#303030',
//                             innerSize: '99%',
//                             animation: false,
//                             dataLabels: {
//                                 enabled: false
//                             }
//                         }
//                     },
//                     credits: {
//                         enabled: false
//                     },
//                     exporting: {
//                         enabled: false
//                     },
//                     tooltip: {
//                         pointFormat: '{series.name}: <b>{point.y}</b>'
//                     },
//                     colors: ['#c0392b', '#27ae60'],
//                     series: [{
//                         name: c,
//                         data: [
//                             ['Hellbourne', Math.floor(d['h' + c])],
//                             ['Legion', Math.floor(d['l' + c])]
//                         ]
//                     }]
//                 });
//             });


// // items
// $http({
//         method: 'GET',
//         url: BaseUrl + '/item/',
//         cache: true
//     })
//     .success(function(res) {
//         $rootScope.item_names = {};
//         angular.forEach(res, function(value) {
//             $rootScope.item_names[value.id] = {
//                 'name': value.name,
//                 'cli_name': value.cli_name,
//                 'cost': value.cost,
//                 'description': value.description
//             };
//         });
//     });


// // heroes
//     $http({
//         method: 'GET',
//         url: 'scripts/data/heroes.json',
//         cache: true
//     })
//     .success(function(res) {
//         $rootScope.hero_names = res;
//     });