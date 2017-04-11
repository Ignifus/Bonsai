function queryLogs(){
    console.log("get");
    $.ajax({
        url: '/get-logs/',
        dataType: 'json',
        method: 'POST',
        data: {
          "app": "TestAppA", "from": "20"
        },
        success: function(data){
            var obj = JSON.parse(data.responseText)[0].fields;

            $('.i-content').html('<pre>'+ obj.method +'</pre>')
        }
    });
}

setInterval(queryLogs, 2000);