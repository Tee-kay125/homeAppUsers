$.ajax({
    type: 'GET',
    url: '/getLog',
    async: true,
    success: function(data){
        logFunc(data);
    },
    error: function(msg){
        console.log('error getting log (5) requestedFile: getLog.json, script:MsgLog.js');
    }
});

function logFunc(data){
    $('#LogMsgs').empty();
    $('#LogMsgs').append(data);
}

// $(document).on('click', '#downloadLog', function(){
//     msgLog = {'log':$('#LogMsgs').html()};
    
//     $.ajax({
//         type: 'POST',
//         url : '/getLog.txt',
//         data: msgLog
//     })
//     .done(function(msg){
//         console.log("saved");
//     });
// });