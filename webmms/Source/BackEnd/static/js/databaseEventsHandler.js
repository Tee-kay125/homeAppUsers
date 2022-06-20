
/*
    -------------------------------Database------------------------------------
*/

function event_getDatabaseMessage(){
    $.ajax({
        type: 'GET',
        url: '/getDatabaseMessage',
        dataType: 'json',
        async: true,
        success: function(data){
            $(".left-panel").empty();
            G_dctMessageInfo = data;
            displayMessages(G_dctMessageInfo);
            console.log(G_dctMessageInfo);
        },
        error: function(msg){
            console.log('error getting Pipes requestedFile: pipes.json, script:home.js');
        }
    });
}

function event_getCommonTypes(){
    $.ajax({
        type: 'GET',
        url: '/getCommonTypes',
        dataType: 'json',
        async: true,
        success: function(data){
            G_dctCommoTypes = data;
            console.log(G_dctCommoTypes);
        },
        error: function(msg){
            console.log('error getting Pipes requestedFile: pipes.json, script:home.js');
        }
    });
}

setTimeout(function(){
    $('.messageName').toggle();
    $('.messageBlock').toggle();
 }, 1000);

function displayMessages(data){
    $(".left-panel").append('<input type="button" id="reloadDatabaseImport" name="reloadDatabaseImport" value="Reload" />');
    $.each(data, function(fileName, fileNameInfo){
        $(".left-panel").append('<ul> <i class="fa fa-angle-double-right closedArrow"></i> <span class="fileName '+fileName+' fileName__'+fileName+'" > '+ fileName +' </span></ul>');
        $.each(fileNameInfo, function(messageBlock, messageBlockInfo){
            $(".left-panel").append('<ul><span class="messageBlock messageBlock__'+fileName+' '+fileName+'__'+messageBlock+' messageBlock__'+fileName+'__'+messageBlock+'"><i class="fa fa-angle-double-right closedArrow"></i> '+ messageBlock +' </span></ul>');
            $.each(messageBlockInfo, function(messageName, messageInfo){
                $('.left-panel').append('<li class="messageName children__'+fileName+'__'+messageBlock+' '+fileName+'__'+messageBlock+'__'+messageName+'"> '+ messageName +'</li>');
            });
        });
        $(".left-panel").append('<div class="exportButon"> <input type="button" name="deleteFile" value="Delete file" class="deleteFile" id="fileName__'+fileName+'">   <input type="button" name="export" value="save changes" class="exportMessageBlock" id="fileName__'+fileName+'"> <div>');
      });
}

function event_toggleMessage(){
    $(document).on('click', '.fileName', function(){
        var fileClassName = this.className;
        var blockClassNameSplit = fileClassName.split(" ")[1];
        $('.messageBlock__'+blockClassNameSplit).toggle();

        if($(this).prev().hasClass('closedArrow')){
            $(this).prev().removeClass("closedArrow");
            $(this).prev().addClass("openedArrow");
        }else{
            $(this).prev().removeClass("openedArrow");
            $(this).prev().addClass("closedArrow");
        }
        
    });

    $(document).on('click', '.messageBlock', function(){
        var blockClassName = this.className;
        var blockClassNameSplit = blockClassName.split(" ")[2];
        $('.children__'+blockClassNameSplit).toggle("fast");
        
        if($(this).children().hasClass('closedArrow')){
            $(this).children().removeClass("closedArrow");
            $(this).children().addClass("openedArrow");
        }else{
            $(this).children().removeClass("openedArrow");
            $(this).children().addClass("closedArrow");
        }

    });
}

function event_messageClicked(){
    $(document).on('click', '.messageName', function(){
        var blockClassName = this.className;
        var blockClassNameSplit = blockClassName.split(" ")[2];
        var lstClassName = blockClassNameSplit.split("__");
        G_dctUpdateDictionary = {};
        $(".right-panel").empty();
        viewMessage(G_dctMessageInfo[lstClassName[0]][lstClassName[1]][lstClassName[2]], lstClassName);
    });
}

function viewMessage(Msg, lstClassName){
    $(".right-panel").append('<div class="MsgName">'+Msg["acMessageName"]+'</div>');
    var fieldStructKey = "base";
    var valueSpecialKey = lstClassName[0]+"__"+lstClassName[1]+"__"+lstClassName[2];
    recursiveGetValues(Msg["dctMessagePayload"], $(".right-panel"), fieldStructKey, valueSpecialKey);

    
    $(".right-panel").append('<div class="updateMessageDiv"><input type="button" name="updateMessage" value="update" class="updateMessage"></div>');
}


function recursiveGetValues(payload, parentBase, fieldStructKey, valueSpecialKey){
    var divElementBase = document.createElement('div');
    divElementBase.className = fieldStructKey+"__child";
    divElementBase.id = fieldStructKey+"__child";
    divElementBase.style.boxShadow = '-1px -1px 10px -3px  rgb(0, 0, 0)';
    divElementBase.style.marginLeft = 10+'px';
    $(parentBase).append(divElementBase);
    $.each(payload["Attr"], function(indexNo, fieldInfo){
        if("Type" in fieldInfo){
            valueSpecialKey = valueSpecialKey+"__"+indexNo;
            var fieldType;
            if(fieldInfo['Type'].startsWith('Autogen')){
                fieldType = fieldInfo['Type'].split('.')[2];
            }else{
                fieldType = fieldInfo['Type'];
            }
            if(fieldType.startsWith('E')){
                var enums = '';
                $.each(G_dctCommoTypes[fieldType], function(enumKey, enumInfo){
                    $.each(enumInfo, function(enumName, enumValue){
                        if(enumValue == fieldInfo["Value"]){
                            enums += '<option value="'+enumValue+'" selected="selected">'+ enumName +'</option>'; 
                        }else{
                            enums += '<option value="'+enumValue+'">'+ enumName +'</option>';
                        }
                    });
                });

                var textBoxID = valueSpecialKey+"__Value";
                $("#"+divElementBase.id).append('<table class="rawTextTable"><tr class="tableRow"><td class="labelTableData">'+ fieldInfo["Name"] +': </td><td class="textTableData"><select name="'+ fieldInfo['name'] +'" id="'+textBoxID+'" >'+ enums +'</select></td></tr></table>');
                TextBoxHandle = document.getElementById(textBoxID);
                TextBoxHandle.addEventListener('focusout', changeFieldValue.bind(TextBoxHandle));
            
            
            }else if(fieldInfo.hasOwnProperty("Value")){
                var textBoxID = valueSpecialKey+"__Value";
                $("#"+divElementBase.id).append('<table class="rawTextTable"><tr class="tableRow"><td class="labelTableData">'+ fieldInfo["Name"] +': </td><td class="textTableData"><input type="text" id="'+textBoxID+'" value ="'+fieldInfo["Value"]+'" ></td></tr></table>');
                TextBoxHandle = document.getElementById(textBoxID);
                TextBoxHandle.addEventListener('focusout', changeFieldValue.bind(TextBoxHandle));
            }else{
                fieldStructKey = fieldStructKey+'__'+fieldInfo["Name"];
                $("#"+divElementBase.id).append(' <ul class="level1Struct '+fieldStructKey+'"><p onclick="event__expandStructure(\''+fieldStructKey+'\')"> <i class="fa fa-angle-double-down structDown"></i> '+fieldInfo["Name"]+'</p></ul>');
                recursiveGetValues(fieldInfo["Attr"], divElementBase, fieldStructKey, valueSpecialKey)
                
                fieldStructKey = fieldStructKey.split(/__|,/);
                fieldStructKey.pop();
                fieldStructKey = fieldStructKey.join("__");
            }

            valueSpecialKey = valueSpecialKey.split(/__|,/);
            valueSpecialKey.pop();
            valueSpecialKey = valueSpecialKey.join("__");
        }else{
            $("#"+divElementBase.id).append('<table class="rawTextTable" style="textAlign:center;" ><tr class="tableRow" style="textAlign:center;"><td class="labelTableData" style="textAlign:center;"> No Available payload </td></tr></table>');
                
        }
    })

    setTimeout(function(){
       $('.structureUL').toggle("fast"); 
    }, 1000);
}

function event__expandStructure(fieldStructKey){
        $('.'+fieldStructKey+'__child').toggle("fast");

        if($('.'+fieldStructKey).find("i").hasClass('structRight')){
            $('.'+fieldStructKey).find("i").removeClass("structRight");
            $('.'+fieldStructKey).find("i").addClass("structDown");
        }else{
            $('.'+fieldStructKey).find("i").removeClass("structDown");
            $('.'+fieldStructKey).find("i").addClass("structRight");
        }

}

/**
 * @param {*}
 * @description:
 *      this function changes the value on the json file with a change on the input on the header
 * @returns: No return value
 */

function changeFieldValue(){
    var acActualValue = this.value
    var acTextBoxId = this.id;
    G_dctUpdateDictionary[acTextBoxId]=  acActualValue;
}

function event_updateDictionary(){
    $(document).on('click', '.updateMessage', function(){
        console.log(G_dctUpdateDictionary);

        $.ajax({
            type: 'POST',
            url : '/updateDictionary',
            data: G_dctUpdateDictionary
        })
        .done(function(msg){
            console.log(msg);
            event_getDatabaseMessage();
            alert("Message updated");
        });
    });
}

function event_vExportMessageBlock(){
    $(document).on('click', '.exportMessageBlock', function(){
        var dctExportMessage;
        var filename = this.id.split("__")[1];
        dctExportMessage = {"fileName": this.id.split("__")[1]};
        console.log(dctExportMessage);
        $.ajax({
            type: 'POST',
            url : '/exportMessageBlock',
            data: dctExportMessage
        })
        .done(function(msg){
            alert("Message Exported");
            $('.download_'+filename).attr('href', 'file:///'+msg);
            location.reload(true)
        });
    });
}

function event_vReloadDatabase(){
    $(document).on('click', '#reloadDatabaseImport', function(){

        $('#reloadDatabaseImport').toggle("slow");

        $.ajax({
            type: 'POST',
            url : '/reloadDatabaseImport',
            data: ""
        })
        .done(function(msg){
            event_getDatabaseMessage();
            location.reload(true)
        })
        .fail(function(msg){
            console.log("fail")
        });
    });
}

function event_vDeleteFile(){
    $(document).on('click', '.deleteFile', function(){

        var fileName = this.id;
        var dctFileProperty = {"fileName":fileName};

        $(this).toggle("slow");

        $.ajax({
            type: 'POST',
            url : '/deleteFile',
            data: dctFileProperty
        })
        .done(function(msg){
            event_getDatabaseMessage();
            location.reload(true)
        })
        .fail(function(msg){
            console.log("fail")
        });
    });
}