$(function(){
    refresh();
});

function refresh(){
    var chartData = {};
    $.ajax({
        url: '/get-server-logs',
        dataType: 'application/json',
        complete: function(data){
            chartData = JSON.parse(data.responseText)[0].fields;

            var date = new Date(0);
            date.setUTCSeconds(chartData.timestamp);

            var ss = date.getSeconds();
            var min = date.getMinutes();
            var hh = date.getHours();
        }
    });
    setTimeout(refresh,5000);
}