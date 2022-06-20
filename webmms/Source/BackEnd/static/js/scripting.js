function event_filterAutoScriptMsgs(){
    $("#AutoScriptFilterBox").keyup(function(){
        var filter;
        filter = this.value.toUpperCase();
        liToFilter = $(".messageLinkAutoScript");
        $.each(liToFilter, function(key, value){
            element = $("#"+value.id);
            elementText = element.text().toUpperCase();
            if(elementText.indexOf(filter) != -1){
                element.parent().fadeIn();
            }else{
                element.parent().fadeOut();
                element.parent("li").fadeOut();
            }
        });
    });
}


function event_addToScript(){
    /*
        This function loop all the input type from autoScriptSetupForm form and add pass them to a server 
    */
    $(document).on('click', '.addToScript', function(){
        var dctValues = {}; //hold values in dictionary/json format
        var messageID = this.id;
        var scriptName;
        var acPub_topic = $(".pub_topic").val();
        var acDelayInSec = $(".delayInSecNameInput").val();

        //get all values and append to dictionary/json
        $("#autoScriptSetupForm :input").each(function(){
            if($(this).attr("name") != 'Submit'){
                if($(this).attr("name") == 'scriptType'){
                    if(this.checked){
                        dctValues[this.name] = $(this).val();
                    }
                }else if($(this).attr("name") == 'scriptName'){
                    if($(this).parent().attr("style") == "display: block;"){
                        dctValues[this.name] = $(this).val();
                        scriptName = $(this).val();
                    }
                }else if($(this).attr("name") == 'delayInSecName'){
                    if($(this).val()){
                        dctValues[this.name] = $(this).val();
                    }else{
                        dctValues[this.name] = 0;
                    }
                    
                }
            }
        });
        dctValues["messageID"] = messageID;
        
        if(scriptName){
            var iDelayInSec = parseFloat(acDelayInSec);
            if(acPub_topic){
                $.ajax({
                    type: 'POST',
                    url : '/addMessageToScript',
                    data: dctValues
                })
                .done(function(msg){
                    if(msg != "error"){
                        alert("message added");
                        $.ajax({
                            type: 'GET',
                            url: '/output.json',
                            dataType: 'json',
                            async: true,
                            success: function(data){
                                G_dctAutoScriptMessages = data[2];
                                $("#autoScriptSetup").toggle('fast');
                                $('#viewAutoScript > b > .fa-angle-double-right').toggleClass('flip')

                            },
                            error: function(msg){
                                console.log('error getting messages (9) requestedFile: output.json, script:viewMsgs.js');
                            }
                        });
                    }else{
                        alert("error adding a message");
                    }
                })
                .fail(function(msg){
                    alert("failed to add a message");
                });
            }else{
                alert("Message does not have publish topic");
            }
        }else{
            alert("please specify script name");
        }

    });
}
function event_changeScriptType(){
    /*
        change between input type and select box when a radio button is changed
    */
   $(document).on('click', '.radioScriptClass', function(){
        var radioButtonValue = $(this).val();
        if(radioButtonValue == "newScript"){
            $('.newScriptInputBlock').css("display","block");
            $('.existingScriptInputBlock').css("display","none");
        }else if(radioButtonValue == "existingScript"){
            $('.newScriptInputBlock').css("display","none");
            $('.existingScriptInputBlock').css("display","block");
        }
   });
}
function event_toggleAutoScriptWhenClicked(){
    $(document).on('click', '#viewAutoScript', function(){
        $("#autoScriptSetup").toggle('fast');
        $('#viewAutoScript > b > .fa-angle-double-right').toggleClass('flip')
    });
}

function lstAutoScriptMessages(data){
    clearInterval(G_getFieldValuesAndUpdate);
    $.ajax({
        type: 'GET',
        url: '/getBusySendingAutoScripts',
        dataType: 'json',
        async: true,
        success: function(busySendingData){
            $.each(busySendingData, function(key, val){
                G_lstBusySendingAutoScripts.push(val);
            });
        
            $('#AutoScriptMsgs').remove(); //remove all messages before you load new messages
            $('.AutoScriptMenu').append('<div id="AutoScriptMsgs"></div>'); //add Msgs ID for for appending new list of messages

            if(Object.keys(data).length == 0){
                $('#AutoScriptMsgs').append('<div class="startAutoscriptSetUp"> </div>');
                $('.startAutoscriptSetUp').append('<table class="setUpTable"> </table>');
                $('.setUpTable').append('<tr>\
                    <td class="left-td"> Protocol: </td>\
                    <td class="right-td"> <input type="radio" id="MQTTProtocol" name="protocol" value="MQTT"> <label for="MQTT">MQTT</label> <input type="radio" id="ZMQProtocol" name="protocol" value="ZMQ"> <label for="ZMQ">ZMQ</label> <input type="radio" id="prevProtocol" name="protocol" value="previous"> <label for="previous">previous</label> </td>\
                </tr> \
                <tr class="changePassTr">\
                    <td class="left-td"> IP address: </td>\
                    <td class="right-td"> <input type="text" id="conIp" name="conIp" value="" /> </td>\
                </tr>\
                <tr class="changePassTr">\
                    <td class="left-td"> Port: </td>\
                    <td class="right-td"> <input type="text" id="conPort" name="conPort" value="" /> </td>\
                </tr>');

                $('#AutoScriptMsgs').append('<div class="td_loadAutoscript"> <input type="button" class="startAutoscript" value="load autoscript"> </div>'); 
            }
            else{
                $('#AutoScriptMsgs').append('<div class="td_loadAutoscript"> <input type="button" class="restartAutoscript" value="reload autoscript"> </div>'); 
            }
            $.each(data, function(scriptFile, scriptFileInfo){
                if(G_lstBusySendingAutoScripts.includes(scriptFile)){
                    $('#AutoScriptMsgs').append('<ul class="'+scriptFile+'" ><p class="lstMessagesFold"><i class="fa fa-angle-double-right"></i> '+scriptFile+' <span class="messageStatus_'+scriptFile+'" style="color:green;"> Sending message... </span></p></ul>');
                    $.each(scriptFileInfo, function(key, inMsgs){
                        $('.'+scriptFile).append('<li class="listAttr"><input id="checkBoxAttr" type="checkbox" name="checkbox'+key+'" value="'+key+'"><i class="messageLinkAutoScript recording_'+key+'" id="'+ key +'" value="'+scriptFile+'">'+ inMsgs['Name'] +'</i><i class="delayInSec'+key+' delayInSec"> '+ inMsgs['delayInSec'] +' </i></li>');
                    });
                    $('.'+scriptFile).append('\
                        <li>\
                            <table class="repeatSend_'+scriptFile+'">\
                                <tr>\
                                    <td> <input type="button" class="stopSending buttonStyle '+scriptFile+'" value="Stop sending"> </td>\
                                </tr>\
                            </table>\
                        <li>\
                    ');
                }else{
                    $('#AutoScriptMsgs').append('<ul class="'+scriptFile+'" ><p class="lstMessagesFold"><i class="fa fa-angle-double-right"></i> '+scriptFile+' <span class="messageStatus_'+scriptFile+'"></span></p></ul>');
                    $.each(scriptFileInfo, function(key, inMsgs){
                        $('.'+scriptFile).append('<li class="listAttr"><input id="checkBoxAttr" type="checkbox" name="checkbox'+key+'" value="'+key+'"><i class="messageLinkAutoScript recording_'+key+'" id="'+ key +'" value="'+scriptFile+'">'+ inMsgs['Name'] +'</i><i class="delayInSec'+key+' delayInSec"> '+ inMsgs['delayInSec'] +' </i></li>');
                    });
                    $('.'+scriptFile).append('\
                        <li>\
                            <table class="repeatSend_'+scriptFile+'">\
                                <tr>\
                                    <td class="repeatTD"> <p> Repeat </p> </td>\
                                    <td> <label class="switch"> <input type="checkbox" class="repeatAutoscript_'+scriptFile+'"> <span class="slider round"></span> </label></td> \
                                    <td> <input type="button" class="autoSend buttonStyle '+scriptFile+'" value="Send all"> </td>\
                                </tr>\
                            </table>\
                        <li>\
                    ');
                } 
            });

            check_if_recording(data); //check if the message is being recorded and assign a recording png
        },
        error: function(msg){
            console.log('error getting busy sending auto scripts');
        }
    });
}

function event_autoScriptMessage_clicked(){
    $('.messageLinkAutoScript').click(function(){
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
        var msgIDWithRole;
        var msgIDWithoutRole;
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
        var scriptName = $(this).attr("value");
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
                viewAutoScriptMsg(data[2], msgResp, scriptName);
                viewAutoScriptMsgResponse(data[2], msgResp, scriptName);
                G_dctAutoScriptMessages = data[2];
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



async function viewAutoScriptMsg(data, clickedMsgIDPar, scriptNamePar){

    //change the background to black or white on background color switch
    if($("#All-Panels").hasClass('all-panels')){
        $(".fa-external-link").css('color','black');
    }else{
        $(".fa-external-link").css('color','white');
    }


    /*
        get message informetion, header and payload, loop through while appending to documents.
        use message_name/key as ID and Classes for controlling fields.
    */

    var Msg;
    var MsgName;
    var MsgHeader;
    var MsgPayload ;
    var protocolName;
    var pubTopic;
    var subTopc;
    var connection;

   $.each(data, function(scriptFile, scriptFileInfo){
        if(msgResp in scriptFileInfo && scriptNamePar == scriptFile){
            $.each(scriptFileInfo, function(key, inMsgs){
                if(key == clickedMsgIDPar){
                    Msg        = scriptFileInfo[clickedMsgIDPar];
                    MsgName    = Msg['Name'];
                    MsgHeader  = Msg['Header'];
                    MsgPayload = Msg['Payload'];
                    protocolName = Msg['Individual_Message_Protocol'];
                    pubTopic   = Msg['Msg_Topic'];
                    subTopc    = Msg['Msg_Topic_Sub'];
                    connection = Msg['Connection'];
                    delayInSec = Msg['delayInSec'];
                    var selectBoxOptions;

                    $.each(G_dctAutoScriptMessages, function(key, value){
                        selectBoxOptions += '<option value="'+key+'">'+ key +'</option>';
                    });
                    
                    $('#msgName').append('<h5 id="MessageName">'+ MsgName +'</h5>');
                    $('#viewAutoScript').append('<b><i class="fa fa-angle-double-right"></i> Auto script </b>');

                    $('#autoScriptSetup').append('<form id="autoScriptSetupForm"></form>');
                    $('#autoScriptSetupForm').append('<table id="autoScriptSetupTable" style="width:100%"></table>');
                    $('#autoScriptSetupTable').append('<tr>\
                                                        <td class="tableLabels">\
                                                             Script name \
                                                        </td>\
                                                        <td class="newScriptInputBlock" style="display: block;">\
                                                            <input type="text" name="scriptName" value="'+scriptFile+'" disabled/>\
                                                        </td>\
                                                    </tr>');

                    $('#autoScriptSetupTable').append('<tr>\
                                                        <td class="tableLabels">\
                                                             Delay (sec) \
                                                        </td>\
                                                        <td>\
                                                            <input type="number" name="delayInSecName" value="'+delayInSec+'" disabled />\
                                                        </td>\
                                                    </tr>');

                    $('#viewPipe').append('<b><i class="fa fa-angle-double-right"></i> Pipe </b>');
                    $('#connections').append('<table id="midConTable" style="width:100%"></table>');
                    $.each(connection, function(key, value){
                        if(key == "RemoteIP" || key == "Port"){
                        }else{
                            $('#midConTable').append('<tr id="row'+key+'"></tr>');
                            if(key == "Protocol"){
                                $('#row'+key+'').append('<td class="tableConLabels">'+ key +'</td><td><input type="text" name="'+ key +'" value="'+ protocolName +'" disabled /></a></td>');
                            }else{
                                $('#row'+key+'').append('<td class="tableConLabels">'+ key +'</td><td><input type="text" name="'+ key +'" value="'+ value +'" disabled /></a></td>');
                            }
                        }
                    });

                    $('#midConTable').append('<tr id="row_pub_topic"></tr>');
                    $('#row_pub_topic').append('<td class="tableConLabels"> publish topic </td><td><input type="text" name="pub_topic" value="'+ pubTopic +'" disabled /></a></td>');
                    $('#midConTable').append('<tr id="row_sub_topic"></tr>');
                    $('#row_sub_topic').append('<td class="tableConLabels"> subscribe topic </td><td><input type="text" name="row_sub_topic" value="'+ subTopc +'" disabled /></a></td>');


                    $('#Msg').append('<table id="midHeaderTable" style="width:100%"></table>');
                    var fieldID = ''
                    var fieldCount = 0;
                    $.each(MsgHeader, function(key, value){
                        fieldCount ++;
                        fieldID = 'headerField'+fieldCount
                        $('#midHeaderTable').append('<tr id="row'+key+'"></tr>');
                        $('#row'+key+'').append('<td class="tableLabels">'+ key +'</td><td class="AutoScriptMessage" ><input id="text_'+fieldID+'" type="text" class="Messages_'+clickedMsgIDPar+'_Header_'+key+'" name="_'+ key +'" value="'+ value +'" /></a></td>');
                        
                        TextBoxHandle = document.getElementById("text_"+fieldID);
                        TextBoxHandle.addEventListener('focusout', changeHeaderValue.bind(TextBoxHandle));
                    });
                }
            });
        }
    });
    container = $('#MsgPayload');
    value_special_key = 'Messages_'+clickedMsgIDPar+'_Payload';

    //use a recursive function for payload to unfold the structure if there is.
    var rowCount = 0;
    recursive_getAutoScriptPayloadValues(MsgPayload, container, value_special_key, rowCount);
    // append submit button at the end of payload.
    var submit = document.createElement('div');
    submit.id = "submitButton";
    submit.className = "appendedDiv";
    submit.innerHTML = '<input type="button" class="updateValues buttonStyle" value="Update" id="'+scriptNamePar+'_'+protocolName+'_'+connection["xmlSchema"]+'_'+clickedMsgIDPar+'">';
    container.append(submit)
    container.append('<div id="status"></div>')
}
/**
 * 
 * @param {* message payload} payload 
 * @param {* for structure, contains the structure div/zlevel} container 
 * @param {* structure class-name, useful for differenting each and every field} value_special_key
 * @description:
 *      Since some fields have structure, we use zlevel and zLevelCount to differentiate the structure
 *      we are working at. Create ID for the leyers/structure level and control all fields of 
 * @returns: No return value
 */
function recursive_getAutoScriptPayloadValues(payload, container, value_special_key, rowCount){
    zLevelCount++; //hold the depth number of the structure
    var zLevel = document.createElement('div'); // hold the depth layer of the structure.
    zLevel.id = "zLevel"+zLevelCount;
    zLevel.className = "appendedDiv boxShadow";
    zLevel.style.zIndex = zLevelCount;
    zLevel.style.boxShadow = '-1px -1px 10px -3px  rgb(0, 0, 0)';
    zLevel.style.marginLeft = divMargin+10+'px';
    container.append(zLevel);

    $('#'+zLevel.id).append('<table id="PayTable'+zLevelCount+'" style="width:100%"></table>');
    var table = "PayTable"+zLevelCount;

    if($.isArray(payload)){
        $.each(payload, function(keyField, field){
            rowCount++;
            elementCount++;
            var divElement = document.createElement('div');
            divElement.id = 'element'+elementCount;
            divElement.className = "appendedDiv";
            zLevel.append(divElement);

            // check if it is structure
            if( ('enumType' in field) == false && ('value'in field) == false ){
                // append the field name, put a new layer for adding new elements, then recurse the structure
                ElementId = divElement.id
                $('#'+ElementId).append('<br/><p class="structField" id="structField'+zLevelCount+'_'+elementCount+'"  onclick="toggleStruct(structField'+zLevelCount+'_'+elementCount+')" ><i class="fa fa-angle-double-right"></i> '+ field['name'] +'</p>');
                value_special_key += '_'+keyField;
                recursive_getAutoScriptPayloadValues(field['members'], zLevel, value_special_key, rowCount);

                lst_value = value_special_key.split('_');
                lst_value_slip = lst_value.slice(0,-1);
                value_special_key = lst_value_slip.join('_');
            }
            
            // check if it is not a structure and not an enum
            else if( ('enumType' in field) == false && 'value'in field ){
                ElementId = divElement.id
                $('#'+table).append('<tr id="'+table+'PayRow'+rowCount+'"></tr>');
                $('#'+table+'PayRow'+rowCount+'').append('<td class="PaytableLabels">'+ field['name'] + '</td><td class="AutoScriptMessage"><input class="'+ value_special_key +'_'+ keyField +'" id="text_' + ElementId + '" type="text" name="'+ field['name'] +'" value="'+ field['value'] +'" /></td>');
                TextBoxHandle = document.getElementById("text_" + ElementId);
                TextBoxHandle.addEventListener('focusout', changeValue.bind(TextBoxHandle));
            }
            
            // check if it is an enum
            else if( 'enumType'in field ){
                var enums = '';
                $.each(field['members'], function(key, value){
                    if(value == field['value']){
                        enums += '<option value="'+value+'" selected="selected">'+ key +'</option>'; 
                    }else{
                        enums += '<option value="'+value+'">'+ key +'</option>';
                    }
                });
                ElementId = divElement.id

                $('#'+table).append('<tr id="'+table+'PayRow'+rowCount+'"></tr>');
                $('#'+table+'PayRow'+rowCount+'').append('<td class="PaytableLabels">'+ field['name'] + '</td><td class="AutoScriptMessage"><select name="'+ field['name'] +'" class="'+ value_special_key +'_'+ keyField +'" id="text_' + ElementId + '" >'+ enums +'</select></td>');
                

                SelectBoxHandle = document.getElementById("text_" + ElementId);
                SelectBoxHandle.addEventListener('focusout', changeValue.bind(SelectBoxHandle));

            }
        });
    }
    
}

/**
 * @param {* json string of all messages on the message manager} receivedMsgs
 * @description:
 *      The response panel/right panel, same as viewMsg/middle panel
 * @returns: No return value
 */
var dctKeyAlreadyExists = {};
async function viewAutoScriptMsgResponse(data, clickedMsgIDPar, scriptNamePar){
    msgResp = clickedMsgIDPar;
    $.each(data, function(scriptFile, scriptFileInfo){
        if(msgResp in scriptFileInfo && scriptNamePar == scriptFile){
            $.each(scriptFileInfo, function(key, inMsgs){
                if(key == clickedMsgIDPar){
                    Msg        = scriptFileInfo[msgResp];
                    MsgName    = Msg['Name'];
                    MsgHeader  = Msg['Header'];
                    MsgPayload = Msg['Payload'];
                    $('#msgNameResp').append('<h5>'+ MsgName +'<i class="receivedMsg'+msgResp+' receivedMsg">  </i></h5>');
                    $.ajax({
                        type: 'GET',
                        url: '/getRecord',
                        dataType: 'json',
                        async: true,
                        success: function(data){
                            var data = JSON.parse(data);
                            $('#MsgResp').append('<table id="midHeaderTableResp"></table>');
                            var fieldID = ''
                            var fieldCount = 0;
                            $.each(MsgHeader, function(key, value){
                                fieldCount ++;
                                fieldID = 'headerFieldResp'+fieldCount
                                $('#midHeaderTableResp').append('<tr id="row'+key+'Resp"></tr>');
                                $('#row'+key+'Resp').append('<td class="tableLabelsResp">'+ key +'</td><td><input type="text" id="text_'+fieldID+'" class="Messages_'+msgResp+'_HeaderResp_'+key+'" name="_'+ key +'" value="'+ value +'" disabled /></td>');
                                
                                TextBoxHandle = document.getElementById("text_"+fieldID);
                                TextBoxHandle.addEventListener('focusout', changeHeaderValue.bind(TextBoxHandle));

                            });
                        }
                    });
                }
            });
        }
    });
    
    // create a base container that holds the entire payload
    container = $('#MsgRespPayload');
    //give each message a special key
    value_special_key = 'Messages_'+msgResp+'_Payload';
    var fieldName = "";
    var rowCountResp = 0;
    dctKeyAlreadyExists = {};
    var messageKey = msgResp;
    recursive_getPayloadValuesResponse(messageKey, MsgPayload, container, value_special_key, rowCountResp, fieldName);
}

function event_autoSend(){
    $(document).on('click', '.autoSend', function(){
        
        fileName = this.className.split(" ")[2];

        var repeatAutoscripting = $(".repeatAutoscript_"+fileName);
        var repeatAutoscriptingState =  repeatAutoscripting.is(":checked");
        var dctValues = {};
        
        dctValues["fileName"] = fileName;
        dctValues["repeatAutoscripting"] = repeatAutoscriptingState;

        $(".messageStatus_"+fileName).empty();
        $(".messageStatus_"+fileName).fadeIn("slow");
        $(".messageStatus_"+fileName).html("sending messages");
        $(".messageStatus_"+fileName).css("color","green");
        
        $.ajax({
            type: 'POST',
            url : '/sendAutoScriptMessage',
            data: dctValues
        })
        .done(function(msg){
            if(msg != "error"){
                if(msg == "true"){
                    // document.querySelector(".repeatSend").style.visibility = "hidden";
                    $(".repeatSend_"+fileName).fadeOut("slow");
                    $(".messageStatus_"+fileName).empty();
                    $(".messageStatus_"+fileName).fadeIn("slow");
                    $(".messageStatus_"+fileName).html("sending messages ...");
                    $(".messageStatus_"+fileName).css("color","green");
                    setTimeout(function(){
                        $(".repeatSend_"+fileName).fadeIn("slow");
                        $(".repeatSend_"+fileName).html('\
                            <tr>\
                                <td>\
                                    <input type="button" class="stopSending buttonStyle '+fileName+'" value="Stop sending">\
                                </td>\
                            </tr>'
                        );
                    }, 1000);
                }else{
                    $(".messageStatus_"+fileName).empty();
                    $(".messageStatus_"+fileName).html("messages sent");
                    $(".messageStatus_"+fileName).css("color","green");
                    $(".messageStatus_"+fileName).fadeIn("slow");
                    $(".repeatSend_"+fileName).fadeOut("slow");
                    setTimeout(function(){
                        $(".messageStatus_"+fileName).fadeOut("slow");
                        $(".repeatSend_"+fileName).fadeIn("slow");
                    }, 1000);
                }
                
            }else{
                $(".messageStatus_"+fileName).html("Failed to send a Message");
                $(".messageStatus_"+fileName).css("color","red");
            }
            
        })
        .fail(function(msg){
            $(".messageStatus_"+fileName).html("Failed to send a Message");
            $(".messageStatus_"+fileName).css("color","red");
        });

    });

    $(document).on('click', '.stopSending', function(){
        var stopSendingMessage = confirm("stop sending message?");
        if(stopSendingMessage){
            fileName = this.className.split(" ")[2];
            var dctValues = {};
            dctValues["fileName"] = fileName;
            $.ajax({
                type: 'POST',
                url : '/stopAutoScriptMessage',
                data: dctValues
            })
            .done(function(msg){
                if(msg != "error"){
                    $(".messageStatus_"+fileName).fadeOut("slow");
                    $(".repeatSend_"+fileName).fadeIn("slow");
                    $(".repeatSend_"+fileName).html('\
                        <tr>\
                            <td class="repeatTD">\
                                <p>\
                                    Repeat\
                                </p>\
                            </td>\
                            <td>\
                                <label class="switch">\
                                    <input type="checkbox" class="repeatAutoscript_'+fileName+'">\
                                    <span class="slider round"></span>\
                                </label>\
                            </td> \
                            <td>\
                                <input type="button" class="autoSend buttonStyle '+fileName+'" value="Send all">\
                            </td>\
                        </tr>'
                    );    
                }else{
                    alert("Error stopping this message from sending");
                }
                
            })
            .fail(function(msg){
                alert("Failed to stop this message from sending");
            });
        }

    });
}




function event_startAutoscript(){
    $(document).on('click', '.startAutoscript', function(){
        var mqttProtocol =  $("#MQTTProtocol").is(':checked');
        var zmqProtocol = $("#ZMQProtocol").is(':checked');
        var prevProtocol = $("#prevProtocol").is(':checked');
        var conIp = $("#conIp").val();
        var conPort = $("#conPort").val();

        var postData = {};
        if(mqttProtocol == false && zmqProtocol == false && prevProtocol == false){
            alert("please select protocol");
        }else{
            if(mqttProtocol == true && zmqProtocol == false && prevProtocol == false){
                postData = {"protocol":"MQTT", "conIp":conIp, "conPort":conPort};
            }else if(mqttProtocol == false && zmqProtocol == true && prevProtocol == false){
                postData = {"protocol":"ZMQ", "conIp":conIp, "conPort":conPort};
            }else if(mqttProtocol == false && zmqProtocol == false && prevProtocol == true){
                postData = {"protocol":"previous", "conIp":conIp, "conPort":conPort};
            }

            if(Object.keys(postData).length != 0 && ((conIp.length != 0 && conPort.length != 0) || prevProtocol == true)){
                document.querySelector(".startAutoscript").style.visibility = "hidden";
                    $(".autoScriptingStatus").append("<div class='loading'>\
                    <div class='dot'></div> \
                    <div class='dot'></div> \
                    <div class='dot'></div> \
                    <div class='dot'></div> \
                    <div class='dot'></div> \
                </div>");

                $.ajax({
                    type: 'POST',
                    url : '/startAutoscript',
                    data: postData
                })
                .done(function(msg){

                    if(msg != "error"){
                        $("#autoScriptingStatus").empty();
                        $("#autoScriptingStatus").fadeIn("slow");
        
                        var newURL;
                        var curentURL = window.location.href;
        
                        if(curentURL.endsWith("AutoScript")){
                            newURL = curentURL;
                        }else{
                            newURL = curentURL+"AutoScript";
                        }
                        window.location.href = newURL;
                    }else{
                        $("#autoScriptingStatus").empty();
                        $("#autoScriptingStatus").html("Failed to start autoscripting");
                        $("#autoScriptingStatus").css("color","red");
                    }

                })
                .fail(function(msg){
                    $("#autoScriptingStatus").html("Failed to start autoscripting");
                    $("#autoScriptingStatus").css("color","red");
                });
            }else{
                alert("please enter IP and Port for selected protocol");
            }
    
        
        }
    });

    $(document).on('click', '#MQTTProtocol', function(){
        if($("#MQTTProtocol").is(':checked')){
            $(".changePassTr").fadeIn("slow");
        }
    });
    $(document).on('click', '#ZMQProtocol', function(){
        if($("#ZMQProtocol").is(':checked')){
            $(".changePassTr").fadeIn("slow");
        }
    });
    $(document).on('click', '#prevProtocol', function(){
        if($("#prevProtocol").is(':checked')){
            $(".changePassTr").fadeOut("slow");
        }else{
            $(".changePassTr").fadeIn("slow");
        }
    });


    $(document).on('click', '.restartAutoscript', function(){
        document.querySelector(".restartAutoscript").style.visibility = "hidden";
        $(".autoScriptingStatus").append("<div class='loading'>\
        <div class='dot'></div> \
        <div class='dot'></div> \
        <div class='dot'></div> \
        <div class='dot'></div> \
        <div class='dot'></div> \
        </div>");
        $.ajax({
            type: 'POST',
            url : '/restartAutoscript',
            data: ""
        })
        .done(function(msg){

            $("#autoScriptingStatus").empty();
            $("#autoScriptingStatus").fadeIn("slow");

            var newURL;
            var curentURL = window.location.href;

            if(curentURL.endsWith("AutoScript")){
                newURL = curentURL;
            }else{
                newURL = curentURL+"AutoScript";
            }
            window.location.href = newURL;
        })
        .fail(function(msg){
            $("#autoScriptingStatus").html("Failed to send a Message");
            $("#autoScriptingStatus").css("color","red");
        });

    });
}

function event_updateValues(){
    $(document).on('click', '.updateValues', function(){

        var dctValues = {};
        var MsgID = this.id;

        lstMsgInfo = MsgID.split("_");
        dctValues["scriptName"] = lstMsgInfo[0];
        dctValues["protocol"] = lstMsgInfo[1];
        dctValues["xmlSchema"] = lstMsgInfo[2];
        dctValues["msgID"] = lstMsgInfo.slice(3,lstMsgInfo.length).join("_");
        
        $.ajax({
            type: 'POST',
            url : '/updateValues',
            data: dctValues
        })
        .done(function(msg){
            if(msg != "error"){
                $("#status").html("Message Updated");
                $("#status").css("color","green");
            }else{
                $("#status").html("Failed to update a Message");
                $("#status").css("color","red");
            }
            
        })
        .fail(function(msg){
            $("#status").html("Failed to update a Message");
            $("#status").css("color","red");
        });

    });
}