/*"""-----------------------------------------------------------------------------

Company  : Reutech Radar Systems
Designer : T Ramukosi
Mentor   : J Taylor
Generated: 2018-08-30
-----------------------------------------------------------------------------*/

$(document).ready(function(){

    function getUrlVars()
    {
        var vars = [], hash;
        var hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
        for(var i = 0; i < hashes.length; i++)
        {
            hash = hashes[i].split('=');
            vars.push(hash[0]);
            vars[hash[0]] = hash[1];
        }
        return vars;
    }
    var msgID = getUrlVars()['msgID'];
    var msgResp = getUrlVars()['msgResp'];

    viewMessageOnNewTab(msgID, msgResp);

});


function viewMessageOnNewTab(msgID, msgResp){

    /*
            Clear the mid and right panel when a message is clicked and populate them with new fields
        */

       clearInterval(G_getFieldValuesAndUpdate);
       clearInterval(G_dctReceivedMessagesInterval);

       G_changedValues.length = 0;
       $('#pipeMidPanel').empty()
       $('#Msg').empty();
       $('#msgName').empty();
       $('.appendedDiv').remove();
       $('.appendedDivResp').remove();
       $('#connections').empty();
       $('#autoScriptSetup').empty();
       $('#viewAutoScript').empty();
       $('#viewPipe').empty();
       $('#connections').fadeOut();
       $('#autoScriptSetup').fadeOut();
       $('#MsgResp').empty();
       $('#msgNameResp').empty();
       $('.appendedDivResp').remove();
       $(".preloader").empty();
       var numberOfMsgReceived;
       
       $(".preloader").append('\
       <div class="preloader__ring">\
       <div class="preloader__sector">L</div>\
       <div class="preloader__sector">o</div>\
       <div class="preloader__sector">a</div>\
       <div class="preloader__sector">d</div>\
       <div class="preloader__sector">i</div>\
       <div class="preloader__sector">n</div>\
       <div class="preloader__sector">g</div>\
       <div class="preloader__sector">.</div>\
       <div class="preloader__sector">.</div>\
       <div class="preloader__sector">.</div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       </div>\
       <div class="preloader__ring">\
       <div class="preloader__sector">L</div>\
       <div class="preloader__sector">o</div>\
       <div class="preloader__sector">a</div>\
       <div class="preloader__sector">d</div>\
       <div class="preloader__sector">i</div>\
       <div class="preloader__sector">n</div>\
       <div class="preloader__sector">g</div>\
       <div class="preloader__sector">.</div>\
       <div class="preloader__sector">.</div>\
       <div class="preloader__sector">.</div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       <div class="preloader__sector"></div>\
       </div>\
   </div>');

   document.querySelector(".preloader").style.visibility = "visible";

    $('#pipeMidPanel').empty()
    $('#Msg').empty();
    $('#msgName').empty();
    $('.appendedDiv').remove();
    $('.appendedDivResp').remove();
    $('#connections').empty();
    $('#autoScriptSetup').empty();
    $('#viewAutoScript').empty();
    $('#viewPipe').empty();
    $('#connections').fadeOut();
    $('#autoScriptSetup').fadeOut();
    $('#MsgResp').empty();
    $('#msgNameResp').empty();
    $('.appendedDivResp').remove();
    clearInterval(G_getFieldValuesAndUpdate);
    clearInterval(G_dctReceivedMessagesInterval);

    /*
        this ajax get data from server and pass data to viewMsg function which read msgHeader and creates field, label and input
        wit passes payload fields to recursive_getPayloadValues function that has a recursive function that loops through
        the structure deep to n^th level, it checks if its enumtype, and perform enum operation, structure and recurse or
        basic input and perform the basic operation.
    */
    numberOfMsgReceived = 'receivedMsg'+msgID;
    $('#msgNameResp').append('<div id="newTab"><a href="/newTab?msgID='+msgID+'&msgResp='+msgResp+'" target="_blank" ><i class="fa fa-external-link"></i></a></div>');
    
    $.ajax({
        type: 'GET',
        url: '/output.json',
        dataType: 'json',
        async: true,
        success: function(data){
            viewMsgNewTab(data[0], msgID);
            viewMsgResponseNewTab(data[1], msgResp);
            $('.structField').parent().next('div').toggle();
            $('.'+numberOfMsgReceived).empty();
            document.querySelector(".preloader").style.visibility = "hidden";           
        },
        error: function(msg){
            console.log('error getting messages (9) requestedFile: output.json, script:viewMsgs.js');
        }
    });
    messageViewed(msgID);
    getFieldValues(msgResp); // update field values to current values.
}