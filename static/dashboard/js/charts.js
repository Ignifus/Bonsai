function refresh(){
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

            chart.dataProvider.push(obj);
            chart.validateData();
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
        "valueField": "cpu_usage",
        "bullet": "round",
        "bulletBorderColor": "#FFFFFF",
        "bulletBorderThickness": 2,
        "lineThickness": 2,
        "lineColor": "#b5030d",
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

setInterval(refresh, 1000);