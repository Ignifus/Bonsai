function refreshcpu(){
    $.ajax({
        url: '/get-server-logs',
        dataType: 'application/json',
        complete: function(data){

            var obj = JSON.parse(data.responseText)[0].fields;

            var date = new Date(0);
            date.setUTCSeconds(obj.timestamp);

            var ss = date.getSeconds();
            var min = date.getMinutes();
            var hh = date.getHours();
            obj.timestamp = hh+":"+min+":"+ss;

            if(chart.dataProvider.length>10)
            {
                chart.dataProvider.shift();
                chart3.dataProvider.shift();
            }
            chart.dataProvider.push(obj);
            chart.validateData();
            chart3.dataProvider.push(obj);
            chart3.validateData();
        }
    });
}

var chart = AmCharts.makeChart( "chartcpu", {
    "type": "serial",
    "theme": "light",
    "zoomOutButton": {
        "backgroundColor": '#000000',
        "backgroundAlpha": 0.15
    },
    "dataProvider": [],
    "categoryField": "timestamp",
    "categoryAxis": {
        "parseDates": false,
        "minPeriod": "ss",
        "dashLength": 1,
        "gridAlpha": 0.15,
        "axisColor": "#DADADA"
    },
    "graphs": [ {
        "id": "g1",
        "balloonText": "CPU Usage:[[value]]",
        "valueField": "cpu_usage",
        "type": "smoothedLine",
        "bullet": "round",
        "bulletBorderColor": "#FFFFFF",
        "bulletBorderThickness": 2,
        "lineThickness": 2,
        "lineColor": "#B0DE09",
        "negativeLineColor": "#0352b5",
        "hideBulletsCount": 50
    } ],
    "chartCursor": {
        "cursorPosition": "mouse"
    },
    "chartScrollbar": {
        "graph": "g1",
        "scrollbarHeight": 40,
        "color": "#FFFFFF",
        "autoGridCount": true
    }
} );

setInterval(refreshcpu, 1000);

var chart3 = AmCharts.makeChart( "chartupload", {
    "type": "serial",
    "theme": "light",
    "zoomOutButton": {
        "backgroundColor": '#000000',
        "backgroundAlpha": 0.15
    },
    "dataProvider": [],
    "categoryField": "timestamp",
    "categoryAxis": {
        "parseDates": false,
        "minPeriod": "ss",
        "dashLength": 1,
        "gridAlpha": 0.15,
        "axisColor": "#DADADA"
    },
    "graphs": [ {
        "id": "g1",
        "balloonText": "Net Upload:[[value]]",
        "valueField": "net_upload",
        "title": "HDD Usage",
        "type": "smoothedLine",
        "bullet": "round",
        "bulletBorderColor": "#FFFFFF",
        "bulletBorderThickness": 2,
        "lineThickness": 2,
        "lineColor": "#b5030d",
        "negativeLineColor": "#0352b5",
        "hideBulletsCount": 50
    },
    {
        "id": "g2",
        "balloonText": "Net Download:[[value]]",
        "valueField": "net_download",
        "title": "HDD Usage",
        "type": "smoothedLine",
        "bullet": "round",
        "bulletBorderColor": "#FFFFFF",
        "bulletBorderThickness": 2,
        "lineThickness": 2,
        "lineColor": "#FF6600",
        "negativeLineColor": "#0352b5",
        "hideBulletsCount": 50
    }],
    "chartCursor": {
        "cursorPosition": "mouse"
    },
    "chartScrollbar": {
        "graph": "g1",
        "scrollbarHeight": 40,
        "color": "#FFFFFF",
        "autoGridCount": true
    }
} );

AmCharts.makeChart("charthdd",
               {
                    "type": "pie",
                    "angle": 25,
                    "balloonText": "[[title]]<br><span style='font-size:14px'><b>[[value]]</b> ([[percents]]%)</span>",
                    "depth3D": 28,
                    "titleField": "category",
                    "valueField": "column-1",
                    
                 
                    "titles": [],
                    "dataProvider": [
                        {
                            "category": "HDD Usage",
                            "column-1": 97330.978816
                        },

                        {
                            "category": "HDD Total Free",
                            "column-1": 623921.590272
                        }
                    ]
                }
            );

AmCharts.makeChart("chartram",
               {
                    "type": "pie",
                    "angle": 25,
                    "balloonText": "[[title]]<br><span style='font-size:14px'><b>[[value]]</b> ([[percents]]%)</span>",
                    "depth3D": 28,
                    "titleField": "category",
                    "valueField": "column-1",
                    
                 
                    "titles": [],
                    "dataProvider": [
                        {
                            "category": "RAM Usage",
                            "column-1": 3392.155648
                        },

                        {
                            "category": "RAM Total Free",
                            "column-1": 4139.626496
                        }
                    ]
                }
            );