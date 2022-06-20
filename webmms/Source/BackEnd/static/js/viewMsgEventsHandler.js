/*"""-----------------------------------------------------------------------------

Company  : Reutech Radar Systems
Designer : T Ramukosi
Mentor   : J Taylor
Generated: 2018-08-30
-----------------------------------------------------------------------------*/
// "use strict";

function event_message_clicked(){
    $('.messageLink').click(function(){

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
        var isRole = false;
        var msgIDWithRole;
        var msgIDWithoutRole;
        var msgRespID;
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


        /*
            this ajax get data from server and pass data to viewMsg function which read msgHeader and creates field, label and input
            wit passes payload fields to recursive_getPayloadValues function that has a recursive function that loops through
            the structure deep to n^th level, it checks if its enumtype, and perform enum operation, structure and recurse or
            basic input and perform the basic operation.
        */
        
        //clear number of received messages for this message
        var lstMsgIDWithRole = this.id.split("_"); //get msgID and split it
        // check if msgID has role and create msgID with and without role depending on the message.
        if(lstMsgIDWithRole.length > 3){
            isRole = true;
            msgIDWithoutRole = lstMsgIDWithRole[0]+"_"+lstMsgIDWithRole[1]+"_"+lstMsgIDWithRole[2];
            msgIDWithRole = msgIDWithoutRole;
            for(x = 3; x<lstMsgIDWithRole.length; x++){
                msgIDWithRole = msgIDWithRole+"_"+lstMsgIDWithRole[x];
            }
            
        }else{
            isRole = false;
            msgIDWithRole = lstMsgIDWithRole[0]+"_"+lstMsgIDWithRole[1]+"_"+lstMsgIDWithRole[2];
            msgIDWithoutRole = lstMsgIDWithRole[0]+"_"+lstMsgIDWithRole[1]+"_"+lstMsgIDWithRole[2];
        }

        msgResp = msgIDWithRole; //if the message is CmdRsp, ReqRsp, or Unsol, the response will contain the same message key
        numberOfMsgReceived = 'receivedMsg'+msgIDWithRole;

        $('#msgNameResp').append('<div id="newTab"><a href="/newTab?msgID='+msgIDWithRole+'&msgResp='+msgResp+'" target="_blank" ><i class="fa fa-external-link"></i></a></div>');
        $.ajax({
            type: 'GET',
            url: '/output.json',
            dataType: 'json',
            async: true,
            success: function(data){
                viewMsg(data[0], msgResp);
                viewMsgResponse(data[1], msgResp);
                $('.structField').parent().next('div').toggle();
                $('.'+numberOfMsgReceived).empty();      
                
                document.querySelector(".preloader").style.visibility = "hidden";
                document.querySelector("body").style.visibility = "visible";

            },
            error: function(msg){
                console.log('error getting messages (9) requestedFile: output.json, script:viewMsgs.js');
            }
        });

        messageViewed(msgIDWithRole);
        getFieldValues(msgResp); // update field values to current values.
        dctReceivedMessages ();
    });
}

function event_toggle_items(){
    $(".xmlName").parent().children('ul').toggle("fast");
    $(".ListMessages").parent().children('ul').toggle("fast");
    $(".lstMessagesFold").parent().children('li').toggle("fast");

    $(".xmlName").click(function(){
        $(this).parent().children('ul').toggle("fast");
        $(this).children('i').toggleClass('flip');
    });
    $(".ListMessages").click(function(){
        $(this).parent().children('ul').toggle("fast");
        $(this).children('i').toggleClass('flip');
    });
    $(".lstMessagesFold").click(function(){
        $(this).parent().children('li').toggle("fast");
        $(this).children('i').toggleClass('flip');
    });
}

function event_sendValues(){
    $(document).on('click', '.sendValues', function(){

        var dctValues = {};
        var sysName   = $('.conSystemName').val()
        var dest      = $('.conDestination').val()
        var msgName   = $('#MessageName').text()
        var acMsgRoleName = "";

        //get the roles for the message and append to make a key
        lstMsgName = msgName.split("_");
        if(lstMsgName.length > 1){
            acMsgRoleName = msgName.split("_").slice(1).join("_");
        }else{
            acMsgRoleName = "NoRole"
        }
        
        var topic = sysName+'/'+dest+'/'+msgName;
        $("#MsgForm :input").each(function(){
            if($(this).val() != 'Submit'){
                dctValues[this.name] = $(this).val()
            }
        });
        dctValues["Roles"] = acMsgRoleName

        var acPub_topic = $(".pub_topic").val();
        if(acPub_topic){
            $.ajax({
                type: 'POST',
                url : '/sendMessage',
                data: dctValues
            })
            .done(function(msg){
                if(msg != "error"){
                    $("#status").html("Message Sent");
                    $("#status").css("color","green");
                }else{
                    $("#status").html("Failed to send a Message");
                    $("#status").css("color","red");
                }
                
            })
            .fail(function(msg){
                $("#status").html("Failed to send a Message");
                $("#status").css("color","red");
            });
        }else{
            alert("Message does not have publish protocol");
        }

    });
}

function event_toggleWhenClicked(){
    $(document).on('click', '#viewPipe', function(){
        $("#connections").toggle('fast');
        $('#viewPipe > b > .fa-angle-double-right').toggleClass('flip')
    });
}

function event_record(){
    $(document).on('click', '.record', function(){
        var butValue  = $(".record").val();
        var butKey    = this.id;
        var data = {"key":butKey};

        $.ajax({
            type: 'POST',
            url : '/record',
            data: data
        })
            .done(function(msg){
                if( butValue == "Start"){
                    $(".record").val("Stop");
                    $(".recording_"+butKey).append('<img src="/static/images/Record.png" class="msgRecording" />');
                }else{
                    $(".record").val("Start");
                    $(".recording_"+butKey).children("img").remove();
                    $('.record_status'+msgID+' img').fadeTo( "slow", 0.2);
                }
            });
    });
}