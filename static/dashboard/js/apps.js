function queryLogs(){
    $.ajax({
        url: '/get-logs/',
        dataType: 'json',
        method: 'POST',
        data: {
            "app": "TestAppA", "from": "12"
        },
        success: function(data){
            if(data == null || data.length === 0) return;

            data.forEach(function(item){
                if(item.fields.code) $('.http').append("<p>" + renderHttp(item.fields) + "</p>");
                else $('.log').append("<p>" + renderLog(item.fields) + "</p>");
            });
        }
    });
}

function renderHttp(item) {
    return "timestamp: " + item.timestamp  + ", code: " + item.code + " , app: " + item.app;
}

function renderLog(item) {
    return "timestamp: " + item.timestamp  + ", method: " + item.method + ", description: " + item.description + " , app: " + item.app;
}

setInterval(queryLogs, 1000);