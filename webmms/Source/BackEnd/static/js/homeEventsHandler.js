/*"""-----------------------------------------------------------------------------

Company  : Reutech Radar Systems
Designer : T Ramukosi
Mentor   : J Taylor
Generated: 2018-08-30
-----------------------------------------------------------------------------*/
// "use strict";
/** ----------------------------------------------------------------- Events for script-> home.js ------------------------------------------- */
function event_getActivePipes(){
    $.ajax({
        type: 'GET',
        url: '/activePipe',
        dataType: 'json',
        async: true,
        success: function(data){
            loadActivePipes(data);
        },
        error: function(msg){
            console.log('error getting Pipes requestedFile: pipes.json, script:home.js');
        }
    });
}


function event_getPipes(){
    $.ajax({
        type: 'GET',
        url: '/pipes_config',
        dataType: 'json',
        async: true,
        success: function(data){
            loadPipes(data);
        },
        error: function(msg){
            console.log('error getting Pipes requestedFile: pipes.json, script:homeEventHandler.js');
        }
    });
}

function event_getXmls(){
    $.ajax({
        type: 'GET',
        url: '/xmls.json',
        dataType: 'json',
        async: true,
        success: function(data){
            loadXmls(data);
        },
        error: function(msg){
            console.log('error getting xmls requestedFile: xmls.json, script:home.js');
        }
    });
}

function event_getInterfaceXmls(){
    $.ajax({
        type: 'GET',
        url: '/interface.json',
        dataType: 'json',
        async: true,
        success: function(data){
            loadInterfaceXmls(data);
        },
        error: function(msg){
            console.log('error getting xmls requestedFile: xmls.json, script:home.js');
        }
    });
}
function event_hidePipeBlock(){
    $('.AddPipe').addClass('displayNone');
    $('#webMMRules').addClass('displayNone');
}
function event_rrs_logo(){
    $(document).on('click', '.logo', function(){
        var href = 'https://www.reutechradar.com/';
        window.open(href, '_blank');
    });
}

function event_toggleActivePipeList(){
    $('#listOfActivePipes').next('div').toggle("slow");
}
function event_togglePipeList(){
    $('#listOfPipes').next('div').toggle("slow");
}
function event_changeBackgroundColor(){
    $(document).on('click', '#changeBackground', function(){
        var ac_change_hmi_background = $("#All-Panels").attr('class');
        if(ac_change_hmi_background == "row all-panels"){
            $("#All-Panels").attr('class','row all-panels-black');
            $(".fa-external-link").css('color','white');
            $("#changeBackground").attr('class','fa fa-toggle-off');
        }else{
            $("#All-Panels").attr('class','row all-panels')
            $(".fa-external-link").css('color','black');
            $("#changeBackground").attr('class','fa fa-toggle-on');
        }
    });
}
function event_on_homePage(str_url_path){
    var arr_navigating_menu = ['Pipes','Messages','Favourites','AutoScript'];

    var actimeMenu = str_url_path.split("/")[1];
    if(arr_navigating_menu.includes(actimeMenu)){
        $.each(arr_navigating_menu, function(key, val){
            if(val == actimeMenu){
                $("#"+val).addClass('activeMenu');
                $("."+val+'Menu').addClass('displayBlock');
                $("."+val+'Menu').removeClass('displayNone');
            }else{
                $("#"+val).removeClass('activeMenu');
                $("."+val+'Menu').removeClass('displayBlock');
                $("."+val+'Menu').addClass('displayNone');
            }
        }); 
    }
    else if(str_url_path == '/'){
        $.each(arr_navigating_menu, function(key, val){
            if(val == 'Messages'){
                $("#"+val).addClass('activeMenu');
                $("."+val+'Menu').addClass('displayBlock');
                $("."+val+'Menu').removeClass('displayNone');
            }else{
                $("#"+val).removeClass('activeMenu');
                $("."+val+'Menu').removeClass('displayBlock');
                $("."+val+'Menu').addClass('displayNone');
            }
        }); 
    }
}


function event_editActivePipe(){
    $(document).on('click', '#editActivePipe', function(){
        $('#pipeMidPanel').empty();
        $('#Msg').empty();
        $('#msgName').empty();
    
        $('#MsgResp').empty();
        $('#msgNameResp').empty();
        $('#recMsgs').empty();
        $('#recStatus').empty();
    
        $('#connections').empty();
        $('#autoScriptSetup').empty();
        $('#viewAutoScript').empty();
        $('#viewPipe').empty();
        if($('.AddPipe').is(":visible")){
            $('.AddPipe').toggle("slow");
        }
        if($('#webMMRules').is(":visible")){
            $('#webMMRules').toggle("slow");
        }
        
        key = this.className;
        $.ajax({
            type: 'GET',
            url: '/activePipe',
            dataType: 'json',
            async: true,
            success: function(data){
                editActivePipe(key, data);
            },
            error: function(msg){
                console.log('error getting Pipes (2) requestedFile: pipes.json, script:home.js');
            }
        });
    });
}

function event_editPipe(){
    $(document).on('click', '#editPipe', function(){
        $('#pipeMidPanel').empty();
        $('#Msg').empty();
        $('#msgName').empty();
    
        $('#MsgResp').empty();
        $('#msgNameResp').empty();
        $('#recMsgs').empty();
        $('#recStatus').empty();
    
        $('#connections').empty();
        $('#autoScriptSetup').empty();
        $('#viewAutoScript').empty();
        $('#viewPipe').empty();
        if($('.AddPipe').is(":visible")){
            $('.AddPipe').toggle("slow");
        }
        if($('#webMMRules').is(":visible")){
            $('#webMMRules').toggle("slow");
        }
        
        key = this.className;

        $.ajax({
            type: 'GET',
            url: '/pipes_config',
            dataType: 'json',
            async: true,
            success: function(data){
                editPipe(key, data);
            },
            error: function(msg){
                console.log('error getting Pipes (2) requestedFile: pipes.json, script:homeEventHandler.js');
            }
        });
    });
}
function event_addPipeButton(){
    $("#AddPipeButton").click( function(){
        $('.AddPipe').css('display','block');
        $('.AddPipe').empty();
        $('#webMMRules').css('display','block');
        $('#pipeMidPanel').empty();
        $('#Msg').empty();
        $('#msgName').empty();

        $('#MsgResp').empty();
        $('#msgNameResp').empty();

        $('#connections').empty();
        $('#autoScriptSetup').empty();
        $('#viewAutoScript').empty();
        $('#viewPipe').empty();
        $('#recMsgs').empty();
        $('#recStatus').empty();
        $(".selInterface").fadeOut();
        $('.clsUseMQTT').fadeOut();
        $('.clsUseZeroMQ').fadeOut();
        $('.clsUseZeroMQPub').fadeOut();

        addPipe();
    });
}

function event_connectPipe(){
    $(document).on('click', '#connectPipe', function(){
        var pipeName = $('#pipeName').val().length;
        if(pipeName <= 0 ){
            $("#connectionStatus").empty();
            $("#connectionStatus").fadeIn("slow");
            $("#connectionStatus").text("Please enter 'pipe name'");
            $("#connectionStatus").css("color","red")
            return
        }
        $("#connectPipe").fadeOut('slow');
        $("#DeletePipe").fadeOut('slow');
        $("#savePipe").fadeOut('slow');

        $("#connectionStatus").empty();
        $("#connectionStatus").fadeIn("slow");
        $("#connectionStatus").append("<div class='loading'>\
            <div class='dot'></div> \
            <div class='dot'></div> \
            <div class='dot'></div> \
            <div class='dot'></div> \
            <div class='dot'></div> \
            </div>");
        $.ajax({
            type: 'POST',
            url : '/connectPipe',
            data: $('#PipeForm').serialize()
        })
        .done(function(msg){
            if(msg != "connected"){
                $("#connectionStatus").empty();
                $("#connectionStatus").fadeIn("slow");
                $("#connectionStatus").text(msg);
                $("#connectionStatus").css("color","red");
                $("#connectPipe").fadeIn('slow');
                $("#DeletePipe").fadeIn('slow');
                $("#savePipe").fadeIn('slow');
            }else{
                $("#connectionStatus").empty();
                $("#connectionStatus").fadeIn("slow");
                $("#connectionStatus").text("Connected");
                $("#connectionStatus").css("color","green");
                setTimeout(function(){
                    $('.AddPipe').toggle("slow");
                    $('#webMMRules').toggle("slow");
                    $("#connectionStatus").toggle("slow");
                    $.ajax({
                        type: 'GET',
                        url: '/pipes_config',
                        dataType: 'json',
                        async: true,
                        success: function(data){
                            location.reload(true)
                        },
                        error: function(msg){
                            console.log('error getting Pipes (4) requestedFile: pipes.json, script:homeEventHandler.js');
                            $("#connectPipe").fadeIn('slow');
                            $("#DeletePipe").fadeIn('slow');
                            $("#savePipe").fadeIn('slow');
                        }
                    });

                },2000);
            }
            
        })
        .fail(function(msg){
            $("#connectionStatus").empty();
            $("#connectionStatus").fadeIn("slow");
            if(msg.hasOwnProperty("statusText")){
                $("#connectionStatus").text(msg["statusText"]); 
            }else{
                $("#connectionStatus").text(msg);
            }
            $("#connectionStatus").css("color","red");
            $("#connectPipe").fadeIn('slow');
            $("#DeletePipe").fadeIn('slow');
            $("#savePipe").fadeIn('slow');
        });

    }); 
}

function event_savePipe(){
    $(document).on('click', '#savePipe', function(){
        if($('#useZeroMQPub').is(':checked')){
            useZeroMQPub = "on";
        }else{
            useZeroMQPub = "off";
        }
        $.ajax({
            type: 'POST',
            url : '/savePipe',
            data: $('#PipeForm').serialize()
        })
        .done(function(msg){
            if(msg != "saved"){
                $("#connectionStatus").empty();
                $("#connectionStatus").fadeIn("slow");
                $("#connectionStatus").text(msg);
                $("#connectionStatus").css("color","red");
            }else{
                $("#connectionStatus").empty();
                $("#connectionStatus").fadeIn("slow");
                $("#connectionStatus").text("pipe saved");
                $("#connectionStatus").css("color","green");
                setTimeout(function(){
                    $.ajax({
                        type: 'GET',
                        url: '/pipes_config',
                        dataType: 'json',
                        async: true,
                        success: function(data){
                            alert("pipe saved");
                        },
                        error: function(msg){
                            console.log('error getting Pipes (4) requestedFile: pipes.json, script:homeEventHandler.js');
                        }
                    });

                },2000);
            }
            
        })
        .fail(function(msg){
            $("#connectionStatus").empty();
            $("#connectionStatus").fadeIn("slow");
            $("#connectionStatus").text(msg);
            $("#connectionStatus").css("color","red");
        });

    }); 
}

function event_disconnectPipe(){
    $(document).on('click', '#disPipe', function(){
        var con = confirm("are you sure you want to delete this pipe?");
        if(con){
            var  dctValues = {'pipeName': this.className};
            $.ajax({
                type: 'POST',
                url : '/disconnectPipe',
                data: dctValues
            })
            .done(function(msg){
                location.reload();
            });
        }
    });
}

function event_DeletePipe(){
    $(document).on('click', '#DeletePipe', function(){
        var con = confirm("are you sure you want to delete this pipe?");
        if(con){
            var  dctValues = {'pipeName': $("#pipeName").val()}
            $.ajax({
                type: 'POST',
                url : '/deletPipe',
                data: dctValues
            })
            .done(function(msg){
                if(msg == "error"){
                    alert("error deleting a pipe");
                }else{
                    location.reload();
                }
                
            });
        }
    });
}

function event_reset(){
    $(document).on('click', '#reset', function(){
        var con = confirm("are you sure you want to reset?");
        if(con){
            $.ajax({
                type: 'POST',
                url : '/reset'
            })
            .done(function(msg){
                alert("Message Manager Reset successfully...");
                location.reload();
            });
        }
    });
}
function event_menu(){
    $(".menu").click( function(){
        clearInterval(G_getFieldValuesAndUpdate);
        var activeMenuId = this.id;
        var arr_navigating_menu = ['Pipes','Messages','Favourites','AutoScript'];

        $.each(arr_navigating_menu, function(key, val){
            if(val == activeMenuId){
                $("#"+val).addClass('activeMenu');
                $("."+val+'Menu').addClass('displayBlock');
                $("."+val+'Menu').removeClass('displayNone');

                var curentURL = window.location.href;
                var lstURL = curentURL.split("/");

                var newURL = lstURL[0]+'//'+lstURL[2]+'/'+activeMenuId
                history.pushState({}, null, newURL);
                
            }else{
                $("#"+val).removeClass('activeMenu');
                $("."+val+'Menu').removeClass('displayBlock');
                $("."+val+'Menu').addClass('displayNone');
            }
        });
        $('#pipeMidPanel').empty();
        $('#Msg').empty();
        $('#MsgPayload').empty();
        $('#msgName').empty();

        $('#recMsgs').empty();
        $('#recStatus').empty();

        $('#MsgResp').empty();
        $('#MsgRespPayload').empty();
        $('#msgNameResp').empty();

        $('#connections').empty();
        $('#autoScriptSetup').empty();
        $('#viewAutoScript').empty();
        $('#viewPipe').empty();
        if($('.AddPipe').is(":visible")){
            $('.AddPipe').toggle("slow");
        }
        if($('#webMMRules').is(":visible")){
            $('#webMMRules').toggle("slow");
        }
        

        $('.FavMsgsMessage > li').toggle("fast");
    });
}
function event_log(){
    $(document).on('click', '#Log', function(){
        var href = window.location.host + '/log';
        window.open(href, '_blank');

    });
}
function event_recorded(){
    $("#recorded").click( function(){
        if($('.AddPipe').is(":visible")){
            $('.AddPipe').toggle("slow");
        }
        if($('#webMMRules').is(":visible")){
            $('#webMMRules').toggle("slow");
        }
        if($('.lstRecordedMsgs').is(":visible")){
        }else{
            $('.lstRecordedMsgs').toggle("slow");
        }
        $('#pipeMidPanel').empty();
        $('#Msg').empty();
        $('#msgName').empty();

        $('#MsgResp').empty();
        $('#msgNameResp').empty();

        $('#connections').empty();
        $('#autoScriptSetup').empty();
        $('#viewAutoScript').empty();
        $('#viewPipe').empty();
        $('#recMsgs').empty();
        $('#recStatus').empty();

        $.ajax({
            type: 'GET',
            url: '/getRecordedMessages',
            dataType: 'json',
            async: true,
            success: function(data){
                viewRecordedMessages(data)
            },
            error: function(msg){
                console.log('error getting Favmessages (6) requestedFile: favMsgs.json, script:messages.js');
            }
        });
    });
}
function event_checked_messages(){
    var lst_checked_msgs = []
    $(document).on('click', '#xml_check', function(){
        var id = $(this).closest('ul').attr('id');

        if($(this).is(':checked')){
            $.each($('#'+id+' > li > input'), function(key, value){
                var inputVal = $(this).val();
                $(".checkbox"+inputVal).prop('checked', true);
                
                if($.inArray( inputVal, lst_checked_msgs ) !== -1){
                    pass
                }else{
                    lst_checked_msgs.push(inputVal)
                }
            });
        }else{
            $.each($('#'+id+' > li > input'), function(key, value){
                var inputVal = $(this).val();
                $(".checkbox"+inputVal).prop('checked', false);
                lst_checked_msgs.splice($.inArray(inputVal, lst_checked_msgs),1);
            });
        }
    });
}
function event_msg_checkBoxAttr(){
    $(document).on('click', '#msg_checkBoxAttr', function(){
        if($(this).is(':checked')){
            val = $(this).val();
            $(".checkbox"+val).prop('checked', true);
            if($.inArray( val, lst_checked_msgs ) !== -1){
                pass
            }else{
                lst_checked_msgs.push(val)
            }

        }else{
            val = $(this).val();
            $(".checkbox"+val).prop('checked', false);
            lst_checked_msgs.splice($.inArray(val, lst_checked_msgs),1);
        }
    });
}
function event_saveData(){
    $(document).on('click', '.save_data', function(){
        $("#recStatus").html("saving selected files");
        $("#recStatus").css("color","green");

        var dctValues = {}
        $.each(lst_checked_msgs, function(key, value){
            dctValues[value] = value;
        });

        if(lst_checked_msgs.length > 0){
            $.ajax({
                type: 'POST',
                url : '/saveMsgs',
                data: dctValues
            })
            .done(function(fileName){
                $("#recStatus").html("file saved on ./record/json ");
                $("#recStatus").css("color","green");
                filenameWithJsonExtention = fileName+".json";
                fileUrl = '/download'+filenameWithJsonExtention;
                var name = filenameWithJsonExtention;
                downloadURI(fileUrl, name);
            })
            .fail(function(msg){
                $("#recStatus").html("Failed to send a Message");
                $("#recStatus").css("color","red");
            });
        }else{
            $("#recStatus").html("please select file to save");
            $("#recStatus").css("color","orange");
        }
        
    });
}
function event_save_csv(){
    $(document).on('click', '.save_csv', function(){
        $("#recStatus").html("saving selected files");
        $("#recStatus").css("color","green");

        var dctValues = {}
        $.each(lst_checked_msgs, function(key, value){
            dctValues[value] = value;
        });


        if(lst_checked_msgs.length > 0){
            $.ajax({
                type: 'POST',
                url : '/saveCsvMsgs',
                data: dctValues
            })
                .done(function(fileName){
                    $("#recStatus").html("file saved on ./record/csv ");
                    $("#recStatus").css("color","green");

                    filenameWithCsvExtention = fileName+".csv";
                    fileUrl = '/csvDownload'+filenameWithCsvExtention;
                    var name = filenameWithCsvExtention;
                    downloadURI(fileUrl, name);
                })
                .fail(function(msg){
                    $("#recStatus").html("Failed to send a Message");
                    $("#recStatus").css("color","red");
                });
        }else{
            $("#recStatus").html("please select file to save");
            $("#recStatus").css("color","orange");
        }
        
    });
}
function event_deleteData(){
    $(document).on('click', '.delete_data', function(){
        var dctValues = {}
        $.each(lst_checked_msgs, function(key, value){
            dctValues[value] = value;
        });
        if(lst_checked_msgs.length > 0){
            $.ajax({
                type: 'POST',
                url : '/deleteMsgs',
                data: dctValues
            })
                .done(function(msg){
                    refreshDelete();
                    $("#recStatus").html("messages deleted");
                    $("#recStatus").css("color","green");
                })
                .fail(function(msg){
                    refreshDelete();
                    $("#recStatus").html("Failed to Delete Messages");
                    $("#recStatus").css("color","red");
                });
        }else{
            refreshDelete();
            $("#recStatus").html("please select file to Delete");
            $("#recStatus").css("color","orange");
        }
        
    });
}

function event_listOfActivePipes(){
    $(document).on('click', '#listOfActivePipes', function(){
        $(this).next('div').toggle("slow");
        $(this).children('i').toggleClass('flip');
    });
}

function event_listOfPipes(){
    $(document).on('click', '#listOfPipes', function(){
        $(this).next('div').toggle("slow");
        $(this).children('i').toggleClass('flip');
    });
}

function event_databaseMessages(){
    $(document).on('click', '#databaseMessages', function(){
        window.open('databasePage','_bkank');
    });
}

function event_createDAtabaseFile(){
    $(document).on('click', '#databaseCreate', function(){
        console.log("clicked");
        
        $('#pipeMidPanel').empty();
        $('#Msg').empty();
        $('#msgName').empty();
    
        $('#MsgResp').empty();
        $('#msgNameResp').empty();
        $('#recMsgs').empty();
        $('#recStatus').empty();
    
        $('#connections').empty();
        $('#autoScriptSetup').empty();
        $('#viewAutoScript').empty();
        $('#viewPipe').empty();
        
        $.ajax({
            type: 'GET',
            url: '/xmls.json',
            dataType: 'json',
            async: true,
            success: function(data){
                loadXmlsForDatabase(data);
            },
            error: function(msg){
                console.log('error getting xmls requestedFile: xmls.json, script:home.js');
            }
        });
        
    });
}

function loadXmlsForDatabase(data){

    $('#pipeMidPanel').append('<form name="PipeForm" action="/" method="post" id="PipeForm"></form>');

    $('#PipeForm').append('<table name="table1" id="table1"></table>');

    $('#table1').append('<tr> <th> Database file name </th>  </tr>');
    $('#table1').append('<tr id="TR_FrstRaw" > </tr>');
    $('#TR_FrstRaw').append('<td> <input type="text" name="databaseFileName" id="databaseFileName" value="" required="required" /> </td>');

    $('#PipeForm').append('<div> <input type="button" name="connect" value="Create" id="CreateDatabase"> </div>');
}

function event_submitToCreateDatabase(){
    $(document).on('click', '#CreateDatabase', function(){
        $.ajax({
            type: 'POST',
            url : '/CreateDatabaseAll',
            data: $('#PipeForm').serialize()
        })
        .done(function(msg){
            if(msg != "saved"){
                $("#connectionStatus").empty();
                $("#connectionStatus").fadeIn("slow");
                $("#connectionStatus").text(msg);
                $("#connectionStatus").css("color","red");
                setInterval(function (){
                    $("#connectionStatus").fadeOut("slow");
                },3000);
            }else{
                $("#connectionStatus").empty();
                $("#connectionStatus").fadeIn("slow");
                $("#connectionStatus").text("Database file is created");
                $("#connectionStatus").css("color","green");

                setInterval(function (){
                    $("#connectionStatus").fadeOut("slow");
                },3000);

            }
            
        })
        .fail(function(msg){
            $("#connectionStatus").empty();
            $("#connectionStatus").fadeIn("slow");
            $("#connectionStatus").text(msg);
            $("#connectionStatus").css("color","red");
        });


    }); 
}

function event_smallEvents(){
    $(document).on('click', '#databaseStructure', function(){       
        $(".databaseChildren").toggle("slow");
        $(this).children('i').toggleClass('flip');
    });
}