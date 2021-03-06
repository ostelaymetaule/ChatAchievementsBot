window.onload = function() {
    Highcharts.chart('dailyMessages', {
        chart: {
            type: 'area'
        },
        title: {
            text: 'Daily'
        },
        xAxis: {
            allowDecimals: false,
            labels: {
                formatter: function () {
                    return this.value;
                }
            },
            tickPositioner: function() {
                var result = [];
                for(i = 0; i < dailyMessages.length; i++)
                    result.push(i);
                return result;
            },
            title: {
                text: 'Hour'
            },
            max: 23,
            min: 0
        },
        yAxis: {
            title: {
                text: 'Messages'
            },
            labels: {
                formatter: function () {
                    return this.value;
                }
            }
        },
        tooltip: {
            pointFormat: 'Messages: {point.y}'
        },
        plotOptions: {
            area: {
                marker: {
                    enabled: false,
                    symbol: 'circle',
                    radius: 2,
                    states: {
                        hover: {
                            enabled: true
                        }
                    }
                }
            }
        },
        series: [{
            showInLegend: false,
            data: dailyMessages
        }]
    });

     Highcharts.chart('monthlyMessages', {
        chart: {
            type: 'area'
        },
        title: {
            text: 'Monthly'
        },
        xAxis: {
            allowDecimals: false,
            labels: {
                formatter: function () {
                    return this.value;
                }
            },
            tickPositioner: function() {
                var result = [];
                for(i = 1; i <= monthlyMessages.length; i++)
                    result.push(i);
                return result;
            },
            title: {
                text: 'Day'
            },
            max: lastDay
        },
        yAxis: {
            title: {
                text: 'Messages'
            },
            labels: {
                formatter: function () {
                    return this.value;
                }
            }
        },
        tooltip: {
            pointFormat: 'Messages: {point.y}'
        },
        plotOptions: {
            series: {
                pointStart: 1
            },
            area: {
                marker: {
                    enabled: false,
                    symbol: 'circle',
                    radius: 2,
                    states: {
                        hover: {
                            enabled: true
                        }
                    }
                }
            }
        },
        series: [{
            showInLegend: false,
            data: monthlyMessages
        }]
    });

    Highcharts.chart('dailyUsers', {
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie'
        },
        title: {
            text: ''
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.y}</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                    style: {
                        color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                    }
                }
            }
        },
        series: [{
            name: 'Messages',
            colorByPoint: true,
            data: dailyUsers
        }]
    });

    Highcharts.chart('monthlyUsers', {
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie'
        },
        title: {
            text: ''
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.y}</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                    style: {
                        color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                    }
                }
            }
        },
        series: [{
            name: 'Messages',
            colorByPoint: true,
            data: monthlyUsers
        }]
    });
}