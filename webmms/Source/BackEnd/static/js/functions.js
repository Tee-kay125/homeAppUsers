/*"""-----------------------------------------------------------------------------

Company  : Reutech Radar Systems
Designer : T Ramukosi
Mentor   : J Taylor
Generated: 2018-08-30
-----------------------------------------------------------------------------*/
// "use strict";
// var { favMsgs } = require('./messages.js');
/** ----------------------------------------------------------------- functions for script: home.js ------------------------------------------- */

/**
 * @param {*Returned Pipes from Ajax Get call} data 
 * @description:
 *      display all active pipes
 * @returns:
 *      No return value
 */

function loadActivePipes(data){
    $('.activePipeList').empty();
    $.each(data, function(key, val){
        $('.activePipeList').append('<p id="editActivePipe" class="'+key+'">'+ key +'</p>');
    });
}


/**
 * @param {*Returned Pipes from Ajax Get call} data 
 * @description:
 *      display all active pipes
 * @returns:
 *      No return value
 */

function loadPipes(data){
    $('.pipeList').empty();
    $.each(data, function(key, val){
        $('.pipeList').append('<p id="editPipe" class="'+key+'">'+ key +'</p>');
    });
}

/**
 * @param {*Returned xmls from Ajax Get call} data 
 * @description:
 *      populate first xml select field
 * @returns:
 *      No return value
 */
function loadXmls(data){
    $.each(data, function(key, val){
        arr_xml_names.push(val);
        $('#sel1').append('<option value='+val+'>'+ val +'</option>');
    });
}

function loadInterfaceXmls(data){
    $.each(data, function(key, val){
        array_interface_xml_names.push(val);
        $('#selInter1').append('<option value='+val+'>'+ val +'</option>');
    });
}

/**
 * @param {*holds the xml's attribute} xml_to_remove 
 * @description:
 *      this function remove xml select box and its button when its clicked
 * @returns:
 *      No return value
 */

function removeXml(xml_to_remove){
    $('#'+xml_to_remove.id).remove();
    faToRemove = 'fa'+ xml_to_remove.id.substring(3);
    $('#'+faToRemove).remove();
    sysToRemove = 'sys'+ xml_to_remove.id.substring(3);
    $('#'+sysToRemove).remove();
    destToRemove = 'dest'+ xml_to_remove.id.substring(3);
    $('#'+destToRemove).remove();

    schemaToRemove = 'selSchema'+ xml_to_remove.id.substring(3);
    $('#'+schemaToRemove).remove();

    InterfaceToRemove = 'selInter'+ xml_to_remove.id.substring(3);
    $('#'+InterfaceToRemove).remove();

    var trToRemove = 'xml_inter_'+ xml_to_remove.id.substring(3);
    $('.'+trToRemove).remove();

    
}

function useMQTTChanged(){
    if($("#useMQTT").is(':checked')){
        $(".clsUseMQTT").removeAttr("disabled");
        $(".clsUseMQTT").fadeIn();
    }else{
        $(".clsUseMQTT").attr("disabled","disabled");
        $(".clsUseMQTT").fadeOut();
    }
}
function useZeroMQChanged(){
    if($("#useZeroMQ").is(':checked')){
        $(".clsUseZeroMQ").removeAttr("disabled");
        $(".clsUseZeroMQ").fadeIn();
    }else{
        $(".clsUseZeroMQ").attr("disabled","disabled");
        $(".clsUseZeroMQ").fadeOut();
    }
}

function useZeroMQPubChanged(){
    if($("#useZeroMQPub").is(':checked')){
        $(".clsUseZeroMQPub").removeAttr("disabled");
        $(".clsUseZeroMQPub").fadeIn();
    }else{
        $(".clsUseZeroMQPub").attr("disabled","disabled");
        $(".clsUseZeroMQPub").fadeOut();
    }
}

/**
 * @param {*holds the xml's attribute} xml_to_remove 
 * @description:
 *      this function remove xml select box and its button when its clicked
 * @returns:
 *      No return value
 */
function removeXmlFromPipe(xml_to_remove){
    lstValues = []
    pipeName = $('#OpenedPipeName').val()
    lstValues.push(pipeName)
    xmlName  = $(xml_to_remove).val();
    lstValues.push(xmlName)
    $('#TR'+xml_to_remove.id).remove();
    dctValues = {'pipeName':pipeName, 'xmlName':xmlName};
    $.ajax({
        type: 'POST',
        url : '/editPipe',
        data: dctValues
    })
    .done(function(msg){
        console.log("xml removed from pipe");
    });
}

 /**
 * @param {*Pipe key} key 
 * @param {*Returned data} data 
 * @description:
 *      this function remove xml select box and its button when its clicked
 * @returns:
 *      No return value
 */
function addPipe(){
    var MQTT_IP = "";
    var MQTT_PORT = "";
    var ZMQ_PUB_IP = "";
    var ZMQ_PUB_PORT= "";
    var ZMQ_SUB_IP = "";
    var ZMQ_SUB_PORT = "";

    $('#pipeMidPanel').append('<form name="PipeForm" action="/" method="post" id="PipeForm"></form>');

    $('#PipeForm').append('<table name="table1" id="table1"></table>');

    $('#table1').append('<tr> <th> Pipe Name </th>  <th> XML SCHEMA </th>  </tr>');
    $('#table1').append('<tr id="TR_FrstRaw" > </tr>');
    $('#TR_FrstRaw').append('<td> <input type="text" id="pipeName" name="pipe" value="" required="required" /> </td>');
    $('#TR_FrstRaw').append('<td class="td_selectSchema"> <select name="acXmlSchema" class="form-control xmlSchema" id="xmlSchema"> </select> </td> <td rowspan="1">');
    $('#xmlSchema').append('<option value="ADCS"> ADCS </option>');
    $('#xmlSchema').append('<option value="BR12"> BR12 </option>');

    $('#PipeForm').append('<table name="table2" id="table2"></table>');

    $('#table2').append('<tr id="TR_SecRow" > </tr>');    
    $('#TR_SecRow').append('<td> <input type="checkbox" name="useMQTT" id="useMQTT" onchange="useMQTTChanged()" /> MQTT Pub/Sub </td>');
    $('#TR_SecRow').append('<td> <input type="checkbox" name="ZeroMQPub" id="useZeroMQPub" onchange="useZeroMQPubChanged()"/> ZeroMQ Pub </td>');  

    $('#table2').append('<tr id="TR_ThirdRaw" > </tr>');
    $('#TR_ThirdRaw').append('<td> <input type="checkbox" name="useZeroMQ" id="useZeroMQ" onchange="useZeroMQChanged()"/> ZeroMQ Sub </td>');
    $('#TR_ThirdRaw').append('<td> <input type="checkbox" name="pubSubTagSwap" id="usePubSubTagSwap"/> Swap MIC Pub/Sub </td>');

    $('#PipeForm').append('<table name="tableIP_PORT" id="tableIP_PORT"></table>');
    $('#tableIP_PORT').append('<tr class="clsUseMQTT" style="display: none;"> <td class="tabDescription"> MQTT IP </td> <td> <input type="text" id="MQTTRemoteIP" name="MQTTRemoteIP" value="" /> </td> </tr>');
    $('#tableIP_PORT').append('<tr class="clsUseMQTT" style="display: none;"> <td class="tabDescription"> MQTT Port </td> <td> <input type="text" id="MQTTPort" name="MQTTPort" value="" /> </td> </tr>');    
    
    $('#tableIP_PORT').append('<tr class="clsUseZeroMQPub" style="display: none;"> <td class="tabDescription"> ZeroMQ Pub </td> <td> <input type="text" id="ZeroMQRemoteIPPub" name="ZeroMQRemoteIPPub" value="" /> </td> </tr>');
    $('#tableIP_PORT').append('<tr class="clsUseZeroMQPub" style="display: none;"> <td class="tabDescription"> ZeroMQ Port Pub </td> <td> <input type="text" id="ZeroMQPortPub" name="ZeroMQPortPub" value="" /> </td> </tr>');
    
    $('#tableIP_PORT').append('<tr class="clsUseZeroMQ" style="display: none;"> <td class="tabDescription"> ZeroMQ IP Sub </td> <td> <input type="text" id="ZeroMQRemoteIP" name="ZeroMQRemoteIP" value="" /> </td> </tr>');
    $('#tableIP_PORT').append('<tr class="clsUseZeroMQ" style="display: none;"> <td class="tabDescription"> ZeroMQ Port Sub </td> <td> <input type="text" id="ZeroMQPort" name="ZeroMQPort" value="" /> </td> </tr>');
    
    $('#PipeForm').append('<table name="tableXmls" id="tableXmls"></table>');
    $('#tableXmls').append('<tr class="tr_header"><th colspan="2"> <i class="fa fa-plus-circle" id="AddXmlButton"> add more xml</i> </th></tr>');

    var xmlIndex = 1;
    var xml_to_remove = 'sel'+(xmlIndex);
    var faToRemove = 'fa'+(xmlIndex);

    $('#tableXmls').append('<tr class="xml_inter_'+xmlIndex+'"> <td class="td_selectXML"> <select name="xml'+(xmlIndex)+'" class="form-control selXml" id="sel'+(xmlIndex)+'"> </select> </td> <td rowspan="2"> <i class="fa fa-times-circle removeXml" id="'+faToRemove+'" onclick="removeXml('+xml_to_remove+')" ></i> </td> </tr>');

    $.each(arr_xml_names, function(keyMainXmls, valMainXmls){
        $('#sel'+(xmlIndex)).append('<option value="'+ valMainXmls +'">'+ valMainXmls +'</option>');
    });

    $('#tableXmls').append('<tr class="xml_inter_'+xmlIndex+'"> <td> <select name="Interface'+(xmlIndex)+'" class="form-control" id="selInter'+(xmlIndex)+'"> </select> </td> </tr>');
    
    $.each(array_interface_xml_names, function(keyMainXmls, valMainXmls){
        $('#selInter'+(xmlIndex)).append('<option value="'+ valMainXmls +'">'+ valMainXmls +'</option>');
    });

    $('#PipeForm').append('<table name="table_buttons" id="table_buttons"></table>');
    $('#table_buttons').append('<tr><td> <input type="button" name="connect" value="Connect"  id="connectPipe" /> </td> <td> <input type="button" name="savePipe" value="save pipe"  id="savePipe" /> </td> </tr>');
}


 /**
 * @param {*Pipe key} key 
 * @param {*Returned data} data 
 * @description:
 *      this function remove xml select box and its button when its clicked
 * @returns:
 *      No return value
 */
function editActivePipe(key, data){

    var MQTT_IP = "";
    var MQTT_PORT = "";
    var ZMQ_PUB_IP = "";
    var ZMQ_PUB_PORT= "";
    var ZMQ_SUB_IP = "";
    var ZMQ_SUB_PORT = "";
    var xml_Schema = "";


    $('#pipeMidPanel').append('<form name="PipeForm" action="/" method="post" id="PipeForm"></form>');

    $('#PipeForm').append('<table name="table2" id="table2"></table>');


    $('#table2').append('<tr> <th> Pipe Name </th> <th> xml Schema </th></tr>');
    $('#table2').append('<tr> <td> <input type="text" id="pipeName" name="pipe" value="'+key+'" placeholder="pipe name" readonly/> </td> \
    <td class="td_selectSchema"> <select name="acXmlSchema" class="form-control xmlSchema" id="xmlSchema" disabled="disabled" > </select> </td> </tr>');
    
    if(data[key]["xml_schema"] == "ADCS"){
        $('#xmlSchema').append('<option value="ADCS" selected> ADCS </option>');
        $('#xmlSchema').append('<option value="BR12"> BR12 </option>');
    }else{
        $('#xmlSchema').append('<option value="ADCS"> ADCS </option>');
        $('#xmlSchema').append('<option value="BR12" selected> BR12 </option>');
    }
    



    $('#PipeForm').append('<table name="table1" id="table1"></table>');
    $('#table1').append('<tr id="TR_FrstRaw" > </tr>');
    if(data[key].hasOwnProperty('mqtt_pub_sub')){
        $('#TR_FrstRaw').append('<td> <input type="checkbox" name="useMQTT" id="useMQTT" onchange="useMQTTChanged()" checked="checked" disabled="disabled" /> MQTT Pub/Sub </td>');
        MQTT_IP = data[key]["mqtt_pub_sub"][0];
        MQTT_PORT = data[key]["mqtt_pub_sub"][1];
    }else{
        $('#TR_FrstRaw').append('<td> <input type="checkbox" name="useMQTT" id="useMQTT" onchange="useMQTTChanged()" disabled="disabled" /> MQTT Pub/Sub </td>');
    }
    
    if(data[key].hasOwnProperty('zeromq_pub')){
        $('#TR_FrstRaw').append('<td> <input type="checkbox" name="ZeroMQPub" id="useZeroMQPub" onchange="useZeroMQPubChanged()" checked="checked" disabled="disabled" /> ZeroMQ Pub </td>');
        ZMQ_PUB_IP = data[key]["zeromq_pub"][0];
        ZMQ_PUB_PORT= data[key]["zeromq_pub"][1];

    }else{
        $('#TR_FrstRaw').append('<td> <input type="checkbox" name="ZeroMQPub" id="useZeroMQPub" onchange="useZeroMQPubChanged()" disabled="disabled" /> ZeroMQ Pub </td>');
    }

    $('#table1').append('<tr id="TR_SecRow" > </tr>');

    if(data[key].hasOwnProperty('zeromq_sub')){
        $('#TR_SecRow').append('<td> <input type="checkbox" name="useZeroMQ" id="useZeroMQ" onchange="useZeroMQChanged()" checked="checked" disabled="disabled" /> ZeroMQ Sub </td>');
        ZMQ_SUB_IP = data[key]["zeromq_sub"][0];
        ZMQ_SUB_PORT = data[key]["zeromq_sub"][1];
    }else{
        $('#TR_SecRow').append('<td> <input type="checkbox" name="useZeroMQ" id="useZeroMQ" onchange="useZeroMQChanged()" disabled="disabled" /> ZeroMQ Sub </td>');
    }

    if(data[key]['swap_mic_pub_sub'] == "on"){
        $('#TR_SecRow').append('<td> <input type="checkbox" name="pubSubTagSwap" id="usePubSubTagSwap" checked="checked" disabled="disabled" /> Swap MIC Pub/Sub </td>');
    }else{
        $('#TR_SecRow').append('<td> <input type="checkbox" name="pubSubTagSwap" id="usePubSubTagSwap" disabled="disabled" /> Swap MIC Pub/Sub </td>');
    }


    $('#PipeForm').append('<table name="tableIP_PORT" id="tableIP_PORT"></table>');
    if(data[key].hasOwnProperty('mqtt_pub_sub')){
        $('#tableIP_PORT').append('<tr class="clsUseMQTT"> <td class="tabDescription"> MQTT IP </td> <td> <input type="text" id="MQTTRemoteIP" name="MQTTRemoteIP" value="'+MQTT_IP+'" readonly /> </td> </tr>');
        $('#tableIP_PORT').append('<tr class="clsUseMQTT"> <td class="tabDescription"> MQTT Port </td> <td> <input type="text" id="MQTTPort" name="MQTTPort" value="'+MQTT_PORT+'" readonly /> </td> </tr>');
    }else{
        $('#tableIP_PORT').append('<tr class="clsUseMQTT" style="display: none;"> <td class="tabDescription"> MQTT IP </td> <td> <input type="text" id="MQTTRemoteIP" name="MQTTRemoteIP" value="'+MQTT_IP+'" readonly /> </td> </tr>');
        $('#tableIP_PORT').append('<tr class="clsUseMQTT" style="display: none;"> <td class="tabDescription"> MQTT Port </td> <td> <input type="text" id="MQTTPort" name="MQTTPort" value="'+MQTT_PORT+'" readonly /> </td> </tr>');    
    }
    if(data[key].hasOwnProperty('zeromq_pub')){
        $('#tableIP_PORT').append('<tr class="clsUseZeroMQPub"> <td class="tabDescription"> ZeroMQ Pub IP </td> <td> <input type="text" id="ZeroMQRemoteIPPub" name="ZeroMQRemoteIPPub" value="'+ZMQ_PUB_IP+'" readonly /> </td> </tr>');
        $('#tableIP_PORT').append('<tr class="clsUseZeroMQPub"> <td class="tabDescription"> ZeroMQ Pub Port </td> <td> <input type="text" id="ZeroMQPortPub" name="ZeroMQPortPub" value="'+ZMQ_PUB_PORT+'" readonly /> </td> </tr>');
    }else{
        $('#tableIP_PORT').append('<tr class="clsUseZeroMQPub" style="display: none;"> <td class="tabDescription"> ZeroMQ Pub IP </td> <td> <input type="text" id="ZeroMQRemoteIPPub" name="ZeroMQRemoteIPPub" value="'+ZMQ_PUB_IP+'" readonly /> </td> </tr>');
        $('#tableIP_PORT').append('<tr class="clsUseZeroMQPub" style="display: none;"> <td class="tabDescription"> ZeroMQ Pub Port </td> <td> <input type="text" id="ZeroMQPortPub" name="ZeroMQPortPub" value="'+ZMQ_PUB_PORT+'" readonly /> </td> </tr>');
    }
    if(data[key].hasOwnProperty('zeromq_sub')){
        $('#tableIP_PORT').append('<tr class="clsUseZeroMQ"> <td class="tabDescription"> ZeroMQ Sub IP </td> <td> <input type="text" id="ZeroMQRemoteIP" name="ZeroMQRemoteIP" value="'+ZMQ_SUB_IP+'" readonly /> </td> </tr>');
        $('#tableIP_PORT').append('<tr class="clsUseZeroMQ"> <td class="tabDescription"> ZeroMQ Sub Port </td> <td> <input type="text" id="ZeroMQPort" name="ZeroMQPort" value="'+ZMQ_SUB_PORT+'" readonly /> </td> </tr>');
    }else{
        $('#tableIP_PORT').append('<tr class="clsUseZeroMQ" style="display: none;"> <td class="tabDescription"> ZeroMQ Sub IP </td> <td> <input type="text" id="ZeroMQRemoteIP" name="ZeroMQRemoteIP" value="'+ZMQ_SUB_IP+'" readonly /> </td> </tr>');
        $('#tableIP_PORT').append('<tr class="clsUseZeroMQ" style="display: none;"> <td class="tabDescription"> ZeroMQ Sub Port </td> <td> <input type="text" id="ZeroMQPort" name="ZeroMQPort" value="'+ZMQ_SUB_PORT+'" readonly /> </td> </tr>');
    }
    
    $('#PipeForm').append('<table name="tableXmls" id="tableXmls"></table>');

    $.each(data[key]["xmls"], function(xmlIndex, valSavedXml){
        
        var xml_to_remove = 'sel'+(xmlIndex+1);
        var faToRemove = 'fa'+(xmlIndex+1);

        $('#tableXmls').append('<tr class="xml_inter_'+(xmlIndex+1)+'"> <td class="td_selectXML"> <select name="xml'+(xmlIndex+1)+'" class="form-control selXml" id="sel'+(xmlIndex+1)+'" disabled="disabled" > </select> </td> <td rowspan="2" > </td> </tr>');

        $.each(arr_xml_names, function(keyMainXmls, valMainXmls){
            if(valSavedXml === valMainXmls){
                $('#sel'+(xmlIndex+1)).append('<option value="'+ valMainXmls +'" selected>'+ valMainXmls +'</option>');
            }else{
                $('#sel'+(xmlIndex+1)).append('<option value="'+ valMainXmls +'">'+ valMainXmls +'</option>');
            }
        });

        $('#tableXmls').append('<tr class="xml_inter_'+(xmlIndex+1)+'"> <td> <select name="Interface'+(xmlIndex+1)+'" class="form-control" id="selInter'+(xmlIndex+1)+'" disabled="disabled"> </select> </td> </tr>');
        
        $.each(array_interface_xml_names, function(keyMainXmls, valMainXmls){
            if(data[key]["mic"][xmlIndex] === valMainXmls){
                $('#selInter'+(xmlIndex+1)).append('<option value="'+ valMainXmls +'" selected>'+ valMainXmls +'</option>');
            }else{
                $('#selInter'+(xmlIndex+1)).append('<option value="'+ valMainXmls +'">'+ valMainXmls +'</option>');
            }
        });

    });

    savedNumOfXMls = data[key]["xmls"].length + 1;

    
}



 /**
 * @param {*Pipe key} key 
 * @param {*Returned data} data 
 * @description:
 *      this function remove xml select box and its button when its clicked
 * @returns:
 *      No return value
 */
function editPipe(key, data){
    
    var MQTT_IP = "";
    var MQTT_PORT = "";
    var ZMQ_PUB_IP = "";
    var ZMQ_PUB_PORT= "";
    var ZMQ_SUB_IP = "";
    var ZMQ_SUB_PORT = "";
    var xml_Schema = "";


    $('#pipeMidPanel').append('<form name="PipeForm" action="/" method="post" id="PipeForm"></form>');

    $('#PipeForm').append('<table name="table2" id="table2"></table>');


    $('#table2').append('<tr> <th> Pipe Name </th> <th> xml Schema </th></tr>');
    $('#table2').append('<tr> <td> <input type="text" id="pipeName" name="pipe" value="'+key+'" placeholder="pipe name" required/> </td> \
    <td class="td_selectSchema"> <select name="acXmlSchema" class="form-control xmlSchema" id="xmlSchema"> </select> </td> </tr>');
    
    if(data[key]["xml_schema"] == "ADCS"){
        $('#xmlSchema').append('<option value="ADCS" selected> ADCS </option>');
        $('#xmlSchema').append('<option value="BR12"> BR12 </option>');
    }else{
        $('#xmlSchema').append('<option value="ADCS"> ADCS </option>');
        $('#xmlSchema').append('<option value="BR12" selected> BR12 </option>');
    }
    



    $('#PipeForm').append('<table name="table1" id="table1"></table>');
    $('#table1').append('<tr id="TR_FrstRaw" > </tr>');
    if(data[key].hasOwnProperty('mqtt_pub_sub')){
        $('#TR_FrstRaw').append('<td> <input type="checkbox" name="useMQTT" id="useMQTT" onchange="useMQTTChanged()" checked="checked" /> MQTT Pub/Sub </td>');
        MQTT_IP = data[key]["mqtt_pub_sub"][0];
        MQTT_PORT = data[key]["mqtt_pub_sub"][1];
    }else{
        $('#TR_FrstRaw').append('<td> <input type="checkbox" name="useMQTT" id="useMQTT" onchange="useMQTTChanged()"/> MQTT Pub/Sub </td>');
    }
    
    if(data[key].hasOwnProperty('zeromq_pub')){
        $('#TR_FrstRaw').append('<td> <input type="checkbox" name="ZeroMQPub" id="useZeroMQPub" onchange="useZeroMQPubChanged()" checked="checked"/> ZeroMQ Pub </td>');
        ZMQ_PUB_IP = data[key]["zeromq_pub"][0];
        ZMQ_PUB_PORT= data[key]["zeromq_pub"][1];

    }else{
        $('#TR_FrstRaw').append('<td> <input type="checkbox" name="ZeroMQPub" id="useZeroMQPub" onchange="useZeroMQPubChanged()"/> ZeroMQ Pub </td>');
    }

    $('#table1').append('<tr id="TR_SecRow" > </tr>');

    if(data[key].hasOwnProperty('zeromq_sub')){
        $('#TR_SecRow').append('<td> <input type="checkbox" name="useZeroMQ" id="useZeroMQ" onchange="useZeroMQChanged()" checked="checked" /> ZeroMQ Sub </td>');
        ZMQ_SUB_IP = data[key]["zeromq_sub"][0];
        ZMQ_SUB_PORT = data[key]["zeromq_sub"][1];
    }else{
        $('#TR_SecRow').append('<td> <input type="checkbox" name="useZeroMQ" id="useZeroMQ" onchange="useZeroMQChanged()"/> ZeroMQ Sub </td>');
    }

    if(data[key]['swap_mic_pub_sub'] == "on"){
        $('#TR_SecRow').append('<td> <input type="checkbox" name="pubSubTagSwap" id="usePubSubTagSwap" checked="checked" /> Swap MIC Pub/Sub </td>');
    }else{
        $('#TR_SecRow').append('<td> <input type="checkbox" name="pubSubTagSwap" id="usePubSubTagSwap"/> Swap MIC Pub/Sub </td>');
    }

    $('#PipeForm').append('<table name="tableIP_PORT" id="tableIP_PORT"></table>');
    if(data[key].hasOwnProperty('mqtt_pub_sub')){
        $('#tableIP_PORT').append('<tr class="clsUseMQTT"> <td class="tabDescription"> MQTT IP </td> <td> <input type="text" id="MQTTRemoteIP" name="MQTTRemoteIP" value="'+MQTT_IP+'" /> </td> </tr>');
        $('#tableIP_PORT').append('<tr class="clsUseMQTT"> <td class="tabDescription"> MQTT Port </td> <td> <input type="text" id="MQTTPort" name="MQTTPort" value="'+MQTT_PORT+'" /> </td> </tr>');
    }else{
        $('#tableIP_PORT').append('<tr class="clsUseMQTT"> <td class="tabDescription"> MQTT IP </td> <td> <input type="text" id="MQTTRemoteIP" name="MQTTRemoteIP" value="'+MQTT_IP+'" /> </td> </tr>');
        $('#tableIP_PORT').append('<tr class="clsUseMQTT"> <td class="tabDescription"> MQTT Port </td> <td> <input type="text" id="MQTTPort" name="MQTTPort" value="'+MQTT_PORT+'" /> </td> </tr>');    
    
        if(!$("#useQTT").is(":checked")){
            $('.clsUseMQTT').fadeOut()
        }
    }
    if(data[key].hasOwnProperty('zeromq_pub')){
        $('#tableIP_PORT').append('<tr class="clsUseZeroMQPub"> <td class="tabDescription"> ZeroMQ Pub IP </td> <td> <input type="text" id="ZeroMQRemoteIPPub" name="ZeroMQRemoteIPPub" value="'+ZMQ_PUB_IP+'" /> </td> </tr>');
        $('#tableIP_PORT').append('<tr class="clsUseZeroMQPub"> <td class="tabDescription"> ZeroMQ Pub Port </td> <td> <input type="text" id="ZeroMQPortPub" name="ZeroMQPortPub" value="'+ZMQ_PUB_PORT+'" /> </td> </tr>');
    }else{
        $('#tableIP_PORT').append('<tr class="clsUseZeroMQPub" style="display: none;"> <td class="tabDescription"> ZeroMQ Pub IP </td> <td> <input type="text" id="ZeroMQRemoteIPPub" name="ZeroMQRemoteIPPub" value="'+ZMQ_PUB_IP+'" /> </td> </tr>');
        $('#tableIP_PORT').append('<tr class="clsUseZeroMQPub" style="display: none;"> <td class="tabDescription"> ZeroMQ Pub Port </td> <td> <input type="text" id="ZeroMQPortPub" name="ZeroMQPortPub" value="'+ZMQ_PUB_PORT+'" /> </td> </tr>');
        if(!$("#useZeroMQPub").is(":checked")){
            $('.clsUseZeroMQPub').fadeOut()
        }
    }
    if(data[key].hasOwnProperty('zeromq_sub')){
        $('#tableIP_PORT').append('<tr class="clsUseZeroMQ"> <td class="tabDescription"> ZeroMQ Sub IP </td> <td> <input type="text" id="ZeroMQRemoteIP" name="ZeroMQRemoteIP" value="'+ZMQ_SUB_IP+'" /> </td> </tr>');
        $('#tableIP_PORT').append('<tr class="clsUseZeroMQ"> <td class="tabDescription"> ZeroMQ Sub Port </td> <td> <input type="text" id="ZeroMQPort" name="ZeroMQPort" value="'+ZMQ_SUB_PORT+'" /> </td> </tr>');
    }else{
        $('#tableIP_PORT').append('<tr class="clsUseZeroMQ" style="display: none;"> <td class="tabDescription"> ZeroMQ Sub IP </td> <td> <input type="text" id="ZeroMQRemoteIP" name="ZeroMQRemoteIP" value="'+ZMQ_SUB_IP+'" /> </td> </tr>');
        $('#tableIP_PORT').append('<tr class="clsUseZeroMQ" style="display: none;"> <td class="tabDescription"> ZeroMQ Sub Port </td> <td> <input type="text" id="ZeroMQPort" name="ZeroMQPort" value="'+ZMQ_SUB_PORT+'" /> </td> </tr>');
        if(!$("#useZeroMQ").is(":checked")){
            $('.clsUseZeroMQ').fadeOut()
        }
    }
    
    $('#PipeForm').append('<table name="tableXmls" id="tableXmls"></table>');
    $('#tableXmls').append('<i class="fa fa-plus-circle" id="AddXmlButton"> add more xml</i>');

    $.each(data[key]["xmls"], function(xmlIndex, valSavedXml){
        
        var xml_to_remove = 'sel'+(xmlIndex+1);
        var faToRemove = 'fa'+(xmlIndex+1);

        $('#tableXmls').append('<tr class="xml_inter_'+(xmlIndex+1)+'"> <td class="td_selectXML"> <select name="xml'+(xmlIndex+1)+'" class="form-control selXml" id="sel'+(xmlIndex+1)+'"> </select> </td> <td rowspan="2" > <i class="fa fa-times-circle removeXml" id="'+faToRemove+'" onclick="removeXml('+xml_to_remove+')" ></i> </td> </tr>');

        $.each(arr_xml_names, function(keyMainXmls, valMainXmls){
            if(valSavedXml === valMainXmls){
                $('#sel'+(xmlIndex+1)).append('<option value="'+ valMainXmls +'" selected>'+ valMainXmls +'</option>');
            }else{
                $('#sel'+(xmlIndex+1)).append('<option value="'+ valMainXmls +'">'+ valMainXmls +'</option>');
            }
        });

        $('#tableXmls').append('<tr class="xml_inter_'+(xmlIndex+1)+'"> <td> <select name="Interface'+(xmlIndex+1)+'" class="form-control" id="selInter'+(xmlIndex+1)+'"> </select> </td> </tr>');
        
        $.each(array_interface_xml_names, function(keyMainXmls, valMainXmls){
            if(data[key]["mic"][xmlIndex] === valMainXmls){
                $('#selInter'+(xmlIndex+1)).append('<option value="'+ valMainXmls +'" selected>'+ valMainXmls +'</option>');
            }else{
                $('#selInter'+(xmlIndex+1)).append('<option value="'+ valMainXmls +'">'+ valMainXmls +'</option>');
            }
        });

    });

    $('#PipeForm').append('<table name="tableXmls" id="tableXmls"> <tr><td><input type="button" name="connect" value="Connect"  id="connectPipe" /></td> <td> <input type="button" name="savePipe" value="save pipe"  id="savePipe" /> </td> <td> <input type="button" name="delete" value="DeletePipe"  id="DeletePipe" /> </td></tr> </table>');

    savedNumOfXMls = data[key]["xmls"].length + 1;
}

function event_addXmlButton(){
    
    var int_count_xml_number = 1;
    var int_count_xml_number2 = 1;

    $(document).on('click', '#AddXmlButton', function(){
        if(int_count_xml_number2 == 1) int_count_xml_number2 += savedNumOfXMls + 1;
        else int_count_xml_number2 += 1;
        var xml_to_remove = 'sel'+int_count_xml_number2;
        var faToRemove = 'fa'+int_count_xml_number2;

        $('#tableXmls').append('<tr class="xml_inter_'+int_count_xml_number2+'"> <td class="td_selectXML"><select name="xml'+int_count_xml_number2+'" class="form-control selXml" id="'+ xml_to_remove +'"></select></td> <td rowspan="2"> <i class="fa fa-times-circle removeXml" id="'+faToRemove+'" onclick="removeXml('+xml_to_remove+')" ></i> </td></tr>');
        $.each(arr_xml_names, function(key, val){
            $('#sel'+int_count_xml_number2).append('<option value="'+ val +'">'+ val +'</option>');
        });

        $('#tableXmls').append('<tr class="xml_inter_'+int_count_xml_number2+'"> <td> <select name="Interface'+int_count_xml_number2+'" class="form-control selInterface" id="selInter'+ int_count_xml_number2 +'"></select> </td> </tr>');
        $.each(array_interface_xml_names, function(key, val){
            $('#selInter'+int_count_xml_number2).append('<option value="'+ val +'">'+ val +'</option>');
        });

    });

}
/**
 * @param {*holds recordee messages} data 
 * @description:
 *      Display all recorded messages
 * @returns:
 *      No return value
 */
function viewRecordedMessages(data){
    var elementP = document.createElement('div');
    elementP.className = "recHeader";
    elementP.innerHTML = '<p> Recorded Messages </p>';
    $('#recMsgs').append(elementP)

    var data = JSON.parse(data);
    var existing_xmlMsgs = []
    $.each(data, function(key, value){
        if(($.inArray(value["xmlName"], existing_xmlMsgs)) == -1){
            var xmlElem = '<ul id="recXml_'+value["xmlName"]+'" class="recordedMsgs_ul"><input id="xml_check" type="checkbox"><i>'+ value["xmlName"] +'</i></ul>';
            existing_xmlMsgs.push(value["xmlName"]);
        }
        var elem =  '<li><input id="msg_checkBoxAttr" type="checkbox" class="checkbox'+key+'" value="'+key+'" ><i class="msg'+key+'" id="'+ key +'">'+ value['Name'] +'</i></li>';
        $('#recMsgs').append(xmlElem)
        $('#recXml_'+value["xmlName"]).append(elem);
    });

    var submit = document.createElement('div');
    submit.id = "submitButton";
    submit.className = "appendedDiv";
    submit.innerHTML = '<input type="button" class="save_data" value="Save as Json">';
    $('#recMsgs').append(submit)

    var saveCsvRecord = '<input type="button" class="save_csv" value="Save as CSV">';
    $('#submitButton').append(saveCsvRecord)

    var delRecord = '<input type="button" class="delete_data" value="Delete">';
    $('#submitButton').append(delRecord)
}

/**
 * @param: No params 
 * @description:
 *      Called when ever a recorded message is deleted or an attempt to delete a message is made
 * @returns: No return value
 */
function refreshDelete(){
    if($('.AddPipe').is(":visible")){
        $('.AddPipe').toggle();
    }
    if($('.lstRecordedMsgs').is(":visible")){
        pass;
    }else{
        $('.lstRecordedMsgs').toggle();
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
}

/**
 * @param {* path to the file} fileUrl
 * @param {* file name} name 
 * @description:
 *      Called whenever a recorded message is being saved
 * @returns: No return value
 */
function downloadURI(fileUrl, name){
    var link = document.createElement("a");
    link.download = name;
    link.href = fileUrl;
    link.click();
}


/** ----------------------------------------------------------------- functions for script: messages.js ------------------------------------------- */
/**
 * @param {* No params}
 * @description:
 *      get received messages and update number of received messages every second
 * @returns: No return value
 */
function dctReceivedMessages (){
	G_dctReceivedMessagesInterval = setInterval(function (){
	    $.ajax({
	        type: 'GET',
	        url: '/dctReceivedMessages',
	        dataType: 'json',
	        async: true,
	        success: function(data){
                receivedMsgs = data;
	            updateNoOfReceivedMsgs(receivedMsgs);
	        },
	        error: function(msg){
	            console.log('error getting dctReceivedMsgs (7) requestedFile: dctReceivedMessages.json, script:messages.js');
	        }
	    });
    },1000);
}

 /**
 * @param {* holds all messages received} receivedMsgs
 * @description:
 *      use the message_key/class_name to update number of received messages 
 * @returns: No return value
 */
function updateNoOfReceivedMsgs(receivedMsgs){
    $('.receivedMsg').text('');
    $('.totNumOfSubMsgs').text('');

    var noOfmsgs = 0;
    var pageTitle = document.title;
    var lstPageTitle = pageTitle.split(')');
    var trimedPageTittle = '';
    if(lstPageTitle.length <= 1){
        trimedPageTittle = lstPageTitle[0]
    }else{
        trimedPageTittle = lstPageTitle[1]
    }

    var msgID = getUrlVars()['msgID'];
    
    if(trimedPageTittle != "Message Manager"){
        $.each(receivedMsgs, function(dctKey, dctVal){
            $('.receivedMsg'+dctKey).text(dctVal);
    
            var dctKeyLst = dctKey.split('_');
            var dctKeyTypeResp = parseInt(dctKeyLst[2]);
            var dctKeyResp = dctKeyLst[0]+'_'+dctKeyLst[1]+'_'+dctKeyTypeResp;
            
            $('.receivedMsg'+dctKeyResp).text(dctVal);
            if(msgID == dctKey){
                noOfmsgs = noOfmsgs+dctVal;
            }
        });
    }else{
        $.each(receivedMsgs, function(dctKey, dctVal){
            $('.receivedMsg'+dctKey).text(dctVal);
    
            var dctKeyLst = dctKey.split('_');
            var dctKeyTypeResp = parseInt(dctKeyLst[2]);
            var dctKeyResp = dctKeyLst[0]+'_'+dctKeyLst[1]+'_'+dctKeyTypeResp;
            
            $('.receivedMsg'+dctKeyResp).text(dctVal);
    
            noOfmsgs = noOfmsgs+dctVal;
        });
    }

    var dctKeyLst;
    var dctKey_ID;
    var dctTotNumOfSubMsgs = {}
    $.each(receivedMsgs, function(dctKey, dctVal){
        dctKeyLst = dctKey.split('_');
        dctKey_ID = dctKeyLst[0]+'_'+dctKeyLst[1]+'_'+dctKeyLst[2];
        if(dctKey_ID in dctTotNumOfSubMsgs){
            dctTotNumOfSubMsgs[dctKey_ID] = +parseInt(dctTotNumOfSubMsgs[dctKey_ID])+dctVal
        }else{
            dctTotNumOfSubMsgs[dctKey_ID] = dctVal
        }        
    });
    $.each(dctTotNumOfSubMsgs, function(dctKey, dctVal){
        $('.totNumOfSubMsgs_'+dctKey).text(dctVal);
    });

    changeTitle(noOfmsgs, trimedPageTittle);
}

function changeTitle(noOfmsgs, pageTitle){
    var newPageTitle = '';

    if(noOfmsgs == 0){
        newPageTitle = pageTitle;
        document.title = newPageTitle;
    }else{
        newPageTitle = '('+ noOfmsgs +')'+pageTitle;
        document.title = newPageTitle;
    }
}

function getUrlVars(){
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
 /**
 * @param {* json string of all messages on the message manager} data
 * @description:
 *      This function read all active pipes and their xmls in the system and
 *      display messages in a structure, the xmlFile, then its associated messages
 * @returns: No return value
 */
function lstMsgs(data){
    clearInterval(G_getFieldValuesAndUpdate);
    $('#Msgs').remove(); //remove all messages before you load new messages
    $('.MessagesMenu').append('<div id="Msgs"></div>'); //add Msgs ID for for appending new list of messages

    data = data['xmls'];
    $.each(data, function(index, xml){
        var xmlFile = ''
        $.each(xml, function(key, connAndMsgs){
            if(key == 'Connection'){
                $.each(connAndMsgs, function(key2, inConn){
                    if(key2 == 'xmlFile'){
                        if(inConn.length == 0){
                            $('#Msgs').append('<ul class="No messages for this selected protocol xmlNames"><p class="xmlName" id="xml_No messages for this selected protocol"><i class="fa fa-angle-double-right"></i> No messages for this selected protocol </p></ul>');
                            return false;
                        }
                        $('#Msgs').append('<ul class="'+ inConn +' xmlNames"><p class="xmlName" id="xml_'+inConn+'"><i class="fa fa-angle-double-right"></i> '+ inConn +'</p></ul>');
                        xmlFile = inConn;
                        $('.'+xmlFile).append('<ul><p class="ListMessages"><i class="fa fa-angle-double-right"></i> Messages </p></ul>');
                    }
                });
            }
            else if(key == 'Messages'){
                var lstSubUL = [];
                $.each(connAndMsgs, function(key2, inMsgs){
                    if($.inArray(key2,favMsgs['messages']) != -1){
                        lstKeys = [];
                        $.each(receivedMsgs, function(dctKey, dcyVal){
                            lstKeys.push(dctKey);
                        });

                        if(receivedMsgs[key2] != null){
                            $('.'+xmlFile+' > ul').append('<li><input id="checkBoxAttr" type="checkbox" name="checkbox'+key2+'" value="'+key2+'" checked><i class="messageLink fav recording_'+key2+'" id="'+ key2 +'">'+ inMsgs['Name'] +'</i><i class="receivedMsg'+key2+' receivedMsg">'+ receivedMsgs[key2] +'</i></li>');
                        }else{
                            $('.'+xmlFile+' > ul').append('<li><input id="checkBoxAttr" type="checkbox" name="checkbox'+key2+'" value="'+key2+'" checked><i class="messageLink fav recording_'+key2+'" id="'+ key2 +'">'+ inMsgs['Name'] +'</i><i class="receivedMsg'+key2+' receivedMsg"></i></li>');
                        }
                    }else{
                        lstKeys = [];
                        $.each(receivedMsgs, function(dctKey, dcyVal){
                            lstKeys.push(dctKey);
                        });
                        
                        var subUL = inMsgs['Name'].split('_')[0];
                        if($.inArray(subUL,lstSubUL) == -1){
                            $('.'+xmlFile+' > ul').append('<ul class="'+subUL+'" ><p class="lstMessagesFold"><i class="fa fa-angle-double-right"></i> '+subUL+'  <i class="totNumOfSubMsgs totNumOfSubMsgs_'+key2+'"> </i></p></ul>');
                        };
                        lstSubUL.push(subUL);
                        if(receivedMsgs[key2] != null){
                            $('.'+xmlFile+' > ul > .'+subUL).append('<li class="listAttr"><input id="checkBoxAttr" type="checkbox" name="checkbox'+key2+'" value="'+key2+'"><i class="messageLink recording_'+key2+'" id="'+ key2 +'">'+ inMsgs['Name'] +'</i><i class="receivedMsg'+key2+' receivedMsg">'+ receivedMsgs[key2] +'</i></li>');
                        }else{
                            $('.'+xmlFile+' > ul > .'+subUL).append('<li class="listAttr"><input id="checkBoxAttr" type="checkbox" name="checkbox'+key2+'" value="'+key2+'"><i class="messageLink recording_'+key2+'" id="'+ key2 +'">'+ inMsgs['Name'] +'</i><i class="receivedMsg'+key2+' receivedMsg"></i></li>');
                        }
                    }
                });
            }
        });
    });

    check_if_recording(data); //check if the message is being recorded and assign a recording png
}



/**
 * @param {* json string of all messages on the message manager} data
 * @description:
 *      check if the message is being recorded and assign a recording png
 * @returns: No return value
*/
function check_if_recording(data){
    $.ajax({
        type: 'GET',
        url: '/getRecord',
        dataType: 'json',
        async: true,
        success: function(lstRecording){ 
            var lstRecordings = JSON.parse(lstRecording);
            var messageRecording = 0;
            $.each(data, function(index, xml){
                var xmlFile = ''
                $.each(xml, function(key, connAndMsgs){
                    if(key == 'Messages'){
                        $.each(connAndMsgs, function(key2, inConn){
                            if($.inArray(key2, lstRecordings["msgs"]) != -1){
                                messageRecording += messageRecording;
                                $(".recording_"+key2).attr("class", "messageLink recording_"+key2+" recording");
                                $(".recording_"+key2).append('<img src="/static/images/Record.png" class="msgRecording" />');      
                            }
                        });
                    }
                });
            });
        }
    });
}
/**
 * @param {* json string of all messages on the message manager} data
 * @description:
 *      list all favorite messages
 * @returns: No return value
 */
function lstFavMsgs(data){
    data = data['xmls'];
    $('#FavMsgs').append('<ul class="FavMsgsMessage"><p><i class="fa fa-angle-double-right"></i> Favourite Messages </p></ul>');
    $.each(data, function(index, xml){
        var xmlFile = ''
        $.each(xml, function(key, connAndMsgs){
            if(key == 'Messages'){
                $.each(connAndMsgs, function(key2, inMsgs){
                    if($.inArray(key2,favMsgs['messages']) != -1){
                            lstKeys = [];
                            $.each(receivedMsgs, function(dctKey, dcyVal){
                                lstKeys.push(dctKey);
                            });
                            if(receivedMsgs[key2] != null){
                                $('.FavMsgsMessage').append('<li><i class="fa fa-times-circle removeFavMsg" id='+key2+'></i><i class="messageLink" id="'+ key2 +'">'+ inMsgs['Name'] +'</i><i class="receivedMsg'+key2+' receivedMsg">'+ receivedMsgs[key2] +'</i></li>');
                            }else{
                                $('.FavMsgsMessage').append('<li><i class="fa fa-times-circle removeFavMsg" id='+key2+'></i><i class="messageLink" id="'+ key2 +'">'+ inMsgs['Name'] +'</i><i class="receivedMsg'+key2+' receivedMsg"></i></li>');
                            }
                    }
                });
            }
        });
    });
}


/** ----------------------------------------------------------------- functions for script: ViewMsg.js ------------------------------------------- */
/**
 * @param {*}
 * @description:
 *      Get the values of received message every 2 seconds and call the update function to update the fields
 * @returns: No return value
*/

function check_if_recording(data){
    $.ajax({
        type: 'GET',
        url: '/getRecord',
        dataType: 'json',
        async: true,
        success: function(lstRecording){ 
            var lstRecordings = JSON.parse(lstRecording);
            var messageRecording = 0;
            $.each(data, function(index, xml){
                var xmlFile = ''
                $.each(xml, function(key, connAndMsgs){
                    if(key == 'Messages'){
                        $.each(connAndMsgs, function(key2, inConn){
                            if($.inArray(key2, lstRecordings["msgs"]) != -1){
                                messageRecording += messageRecording;
                                $(".recording_"+key2).attr("class", "messageLink recording_"+key2+" recording");
                                $(".recording_"+key2).append('<img src="/static/images/Record.png" class="msgRecording" />');      
                            }
                        });
                    }
                });
            });
        }
    });
}

var dctFieldAndVal = {};
var fieldAlreadyExists = {};
function getFieldValues(clickedMsgIDPar){
    G_getFieldValuesAndUpdate = setInterval(function(){
        $.ajax({
            type: 'GET',
            url: '/fieldVals_'+msgResp,
            dataType: 'json',
            async: true,
            success: function(data){
                updateFieldVals(data);
            }
        });
    },1000);
}

function getLstHeader(data, msgResp){

    var lstMsgHeader;
    data = data['xmls'];

    $.each(data, function(index, xml){
        if(msgResp in xml['Messages']){
            Msg           = xml['Messages'][msgResp];
            lstMsgHeader = Msg['Header'];
        }
    });
    return lstMsgHeader
}

function getLstPayload(data, msgResp){

    var lstMsgPayload;
    data = data['xmls'];

    $.each(data, function(index, xml){
        if(msgResp in xml['Messages']){
            Msg           = xml['Messages'][msgResp];
            lstMsgPayload = Msg['Payload'];
        }
    });
    return lstMsgPayload
}

function recursive_getFieldValues(lstPayload, isStructure){
    $.each(lstPayload, function(key, field){
        if (('enumType' in field) == false && ('value'in field) == false) {
            isStructureTmp = isStructure+field['name']
            recursive_getFieldValues(field['members'], isStructureTmp)
        }
        if (('enumType' in field) == false && ('value'in field) == true) {
            var tmpFiledName = isStructure+field['name']
            if(fieldAlreadyExists.hasOwnProperty(tmpFiledName)){
                fieldAlreadyExists[tmpFiledName] = parseInt(fieldAlreadyExists[tmpFiledName])+1;
                tmpFiledName = tmpFiledName+fieldAlreadyExists[tmpFiledName];
            }else{
                fieldAlreadyExists[tmpFiledName] = 0;
            }
            dctFieldAndVal[tmpFiledName]=field['value']
        }
        if (('enumType' in field) == true ) {
            var tmpFiledName = isStructure+field['name']
            if(fieldAlreadyExists.hasOwnProperty(tmpFiledName)){
                fieldAlreadyExists[tmpFiledName] = parseInt(fieldAlreadyExists[tmpFiledName])+1;
                tmpFiledName = tmpFiledName+fieldAlreadyExists[tmpFiledName];
            }else{
                fieldAlreadyExists[tmpFiledName] = 0;
            }
            dctFieldAndVal[tmpFiledName]=field['value']
        }
    });
    return dctFieldAndVal;
}

/**
 * @param {* Holds received fileds values} dctFieldVal
 * @description:
 *      Update opened message field values
 * @returns: No return value
*/
function updateFieldVals(dctFieldVal){
    $.each(dctFieldVal, function(dctKey, dctVal){
        
        var lstHeaderFields = ["MsgLength","MsgType","MsgStatus","ModuleAddress","MsgId","MsgCount","TimeStampMs","ProcessStartCnt"];

        var tmpDctMsgId = dctKey.split("_");
        var tmpMsgId = tmpDctMsgId[0]
        
        for(let x = 1; x<tmpDctMsgId.length -1; x++){
            tmpMsgId = tmpMsgId+"_"+tmpDctMsgId[x];
        }
        tmpDctKey = dctKey;

        if(lstHeaderFields.includes(tmpDctKey.split("_")[3])){
            var fieldClassNameResp = "Messages_"+tmpMsgId+"_HeaderResp_"+tmpDctKey.split("_")[3];
            var fieldClassNameRespNewTab = "Messages_"+tmpMsgId+"_HeaderRespNewTab_"+tmpDctKey.split("_")[3];
            
            $('.'+fieldClassNameResp).val(dctVal);
            $('.'+fieldClassNameRespNewTab).val(dctVal);
        }else{
            if(selectBoxMembers.hasOwnProperty(tmpDctKey)){
                $('.'+dctKey).val(selectBoxMembers[tmpDctKey][dctVal]);
                $('.'+dctKey).parent().attr("title", selectBoxMembers[tmpDctKey][dctVal]);
                
                $('.NewTab_'+dctKey).val(selectBoxMembers[tmpDctKey][dctVal]);
                $('.NewTab_'+dctKey).parent().attr("title", selectBoxMembers[tmpDctKey][dctVal]);
                
            }else{
                $('.'+dctKey).val(dctVal);
                $('.'+dctKey).parent().attr("title",dctVal);

                $('.NewTab_'+dctKey).val(dctVal);
                $('.NewTab_'+dctKey).parent().attr("title",dctVal);
            }
        }
    });
}

/**
 * @param {* json string of all messages on the message manager} data
 * @description:
 *      display message fields when message is clicked
 * @returns: No return value
 */

async function viewMsg(data, clickedMsgIDPar){

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
    data = data['xmls']
    $.each(data, function(index, xml){
        if(clickedMsgIDPar in xml['Messages']){
            Msg        = xml['Messages'][clickedMsgIDPar];
            connection = xml['Connection']
            MsgName    = Msg['Name'];
            MsgHeader  = Msg['Header'];
            MsgPayload = Msg['Payload'];
            protocolName = Msg['Individual_Message_Protocol'];
            pubTopic   = Msg['Msg_Topic'];
            subTopc    = Msg['Msg_Topic_Sub'];
            var selectBoxOptions;

            $.each(G_dctAutoScriptMessages, function(key, value){
                selectBoxOptions += '<option value="'+key+'">'+ key +'</option>';
            });
            
            $('#msgName').append('<h5 id="MessageName">'+ MsgName +'</h5>');
            $('#viewAutoScript').append('<b><i class="fa fa-angle-double-right"></i> Auto script </b>');

            $('#autoScriptSetup').append('<form id="autoScriptSetupForm"></form>');
            $('#autoScriptSetupForm').append('<table id="autoScriptSetupTable" style="width:100%"></table>');
            $('#autoScriptSetupTable').append('<tr>\
                                                <td>\
                                                    <input type="radio" class="radioScriptClass" name="scriptType" value="newScript" checked="checked">\
                                                    <label for="newScript"> New script </label>\
                                                </td>\
                                                <td>\
                                                    <input type="radio" class="radioScriptClass" name="scriptType" value="existingScript">\
                                                    <label for="existingScript"> Existing script </label>\
                                                </td>\
                                            </tr>');
            
            $('#autoScriptSetupTable').append('<tr>\
                                                <td>\
                                                    <label for="scriptName"> Script name </label>\
                                                </td>\
                                                <td class="newScriptInputBlock" style="display: block;">\
                                                    <input type="text" name="scriptName" value="" />\
                                                </td>\
                                                <td class="existingScriptInputBlock" style="display: none;">\
                                                <select name="scriptName" >'+ selectBoxOptions +'</select>\
                                                </td>\
                                            </tr>');

            $('#autoScriptSetupTable').append('<tr>\
                                                <td>\
                                                    <label for="delayInSecName"> Delay (sec) </label>\
                                                </td>\
                                                <td>\
                                                    <input type="number" name="delayInSecName" value="0.1" min="0.1" class="delayInSecNameInput" />\
                                                </td>\
                                            </tr>');
            $('#autoScriptSetupForm').append('<input id="'+clickedMsgIDPar+'"type="button" name="Submit" class="addToScript" value="Add to script">');
            
            

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
            $('#row_pub_topic').append('<td class="tableConLabels"> publish topic </td><td><input type="text" name="pub_topic" class="pub_topic" value="'+ pubTopic +'" disabled /></a></td>');
            $('#midConTable').append('<tr id="row_sub_topic"></tr>');
            $('#row_sub_topic').append('<td class="tableConLabels"> subscribe topic </td><td><input type="text" name="row_sub_topic" value="'+ subTopc +'" disabled /></a></td>');


            $('#Msg').append('<table id="midHeaderTable" style="width:100%"></table>');
            var fieldID = ''
            var fieldCount = 0;
            $.each(MsgHeader, function(key, value){
                fieldCount ++;
                fieldID = 'headerField'+fieldCount
                $('#midHeaderTable').append('<tr id="row'+key+'"></tr>');
                $('#row'+key+'').append('<td class="tableLabels">'+ key +'</td><td><input id="text_'+fieldID+'" type="text" class="Messages_'+clickedMsgIDPar+'_Header_'+key+'" name="_'+ key +'" value="'+ value +'" /></a></td>');
                
                TextBoxHandle = document.getElementById("text_"+fieldID);
                TextBoxHandle.addEventListener('focusout', changeHeaderValue.bind(TextBoxHandle));
            });


        }
    });
    container = $('#MsgPayload');
    value_special_key = 'Messages_'+clickedMsgIDPar+'_Payload';

    //use a recursive function for payload to unfold the structure if there is.
    var rowCount = 0;
    recursive_getPayloadValues(MsgPayload, container, value_special_key, rowCount);
    // append submit button at the end of payload.
    var submit = document.createElement('div');
    submit.id = "submitButton";
    submit.className = "appendedDiv";
    submit.innerHTML = '<input type="button" class="sendValues" value="Submit">';
    container.append(submit)
    container.append('<div id="status"></div>')
    if(protocolName == "not_provided"){
        $(".sendValues").css("disabled");
        submit.innerHTML = 'This message cant be send because it does not have Protocol.';
        $("#submitButton").css({"margin-top":"10px"});
    }
}

function viewMsgNewTab(data, clickedMsgIDPar){

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
    data = data['xmls']
    $.each(data, function(index, xml){
        if(clickedMsgIDPar in xml['Messages']){
            Msg        = xml['Messages'][clickedMsgIDPar];
            connection = xml['Connection']
            MsgName    = Msg['Name'];
            MsgHeader  = Msg['Header'];
            MsgPayload = Msg['Payload'];
            pubTopic   = Msg['Msg_Topic'];
            subTopc    = Msg['Msg_Topic_Sub'];

            MsgName    = Msg['Name'];
            title = MsgName; //.slice(0,-3);
            $('#title').text(title);
            
            $('#msgName').append('<h5 id="MessageName">'+ MsgName +'</h5>');
            $('#viewAutoScript').append('<b><i class="fa fa-angle-double-right"></i> Auto script </b>');
            $('#viewPipe').append('<b><i class="fa fa-angle-double-right"></i> Pipe </b>');

            $('#connections').append('<table id="midConTable" style="width:100%"></table>');
            $.each(connection, function(key, value){
                if(key == "RemoteIP" || key == "Port"){
                }else{
                    $('#midConTable').append('<tr id="row'+key+'"></tr>');
                    $('#row'+key+'').append('<td class="tableConLabels">'+ key +'</td><td><input type="text" name="'+ key +'" value="'+ value +'" disabled /></a></td>');
                }
            });
            $('#midConTable').append('<tr id="row_pub_topic"></tr>');
            $('#row_pub_topic').append('<td class="tableConLabels"> pub_topic </td><td><input type="text" name="pub_topic" value="'+ pubTopic +'" disabled /></a></td>');
            $('#midConTable').append('<tr id="row_sub_topic"></tr>');
            $('#row_sub_topic').append('<td class="tableConLabels"> row_sub_topic </td><td><input type="text" name="row_sub_topic" value="'+ subTopc +'" disabled /></a></td>');

            $('#Msg').append('<table id="midHeaderTable" style="width:100%"></table>');
            var fieldID = ''
            var fieldCount = 0;
            $.each(MsgHeader, function(key, value){
                fieldCount ++;
                fieldID = 'headerField'+fieldCount
                $('#midHeaderTable').append('<tr id="row'+key+'"></tr>');
                $('#row'+key+'').append('<td class="tableLabels">'+ key +'</td><td><input id="text_'+fieldID+'" type="text" class="Messages_'+clickedMsgIDPar+'_Header_'+key+'" name="_'+ key +'" value="'+ value +'" /></a></td>');
                
                TextBoxHandle = document.getElementById("text_"+fieldID);
                TextBoxHandle.addEventListener('focusout', changeHeaderValue.bind(TextBoxHandle));
            });


        }
    });
    container = $('#MsgPayload');
    value_special_key = 'Messages_'+clickedMsgIDPar+'_Payload';

    //use a recursive function for payload to unfold the structure if there is.
    var rowCount = 0;
    recursive_getPayloadValues(MsgPayload, container, value_special_key, rowCount);
    // append submit button at the end of payload.
    var submit = document.createElement('div');
    submit.id = "submitButton";
    submit.className = "appendedDiv";
    submit.innerHTML = '<input type="button" class="sendValues" value="Submit">';
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
function recursive_getPayloadValues(payload, container, value_special_key, rowCount){
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
                setTimeout(recursive_getPayloadValues(field['members'], zLevel, value_special_key, rowCount), 200);

                lst_value = value_special_key.split('_');
                lst_value_slip = lst_value.slice(0,-1);
                value_special_key = lst_value_slip.join('_');
            }
            
            // check if it is not a structure and not an enum
            else if( ('enumType' in field) == false && 'value'in field ){
                ElementId = divElement.id
                $('#'+table).append('<tr id="'+table+'PayRow'+rowCount+'"></tr>');
                $('#'+table+'PayRow'+rowCount+'').append('<td class="PaytableLabels">'+ field['name'] + '</td><td><input class="'+ value_special_key +'_'+ keyField +'" id="text_' + ElementId + '" type="text" name="'+ field['name'] +'" value="'+ field['value'] +'" /></td>');

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
                $('#'+table+'PayRow'+rowCount+'').append('<td class="PaytableLabels">'+ field['name'] + '</td><td><select name="'+ field['name'] +'" class="'+ value_special_key +'_'+ keyField +'" id="text_' + ElementId + '" >'+ enums +'</select></td>');
                

                SelectBoxHandle = document.getElementById("text_" + ElementId);
                SelectBoxHandle.addEventListener('focusout', changeValue.bind(SelectBoxHandle));

            }
        });
    }
    
}

/**
 * @param {* ID of a clicked message} MsgId
 * @description:
 *      empty number of received messages when a message is viewed
 * @returns: No return value
 */
// 
function messageViewed(MsgId){
    viewedMessage = {'MsgId':MsgId}
    $.ajax({
        type: 'POST',
        url : '/updateReceivedMessage',
        data: viewedMessage
     })
    .done(function(msg){
        $("#status").html("");
    });

    $.ajax({
        type: 'GET',
        url: '/dctReceivedMessages',
        dataType: 'json',
        async: true,
        success: function(data){
            updateNoOfReceivedMsgs(data)
        },
        error: function(msg){
            console.log('error getting dctReceivedMsgs (7) requestedFile: dctReceivedMessages.json, script:messages.js');
        }
    });
}

/**
 * @param {* json string of all messages on the message manager} receivedMsgs
 * @description:
 *      The response panel/right panel, same as viewMsg/middle panel
 * @returns: No return value
 */
var dctKeyAlreadyExists = {};
async function viewMsgResponse(data, clickedMsgIDPar){
    data = data['xmls'];
    msgResp = clickedMsgIDPar;
    $.each(data, function(index, xml){
        if(msgResp in xml['Messages']){
            Msg        = xml['Messages'][msgResp];
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
var elementCount = 0;
var zLevelCount = 0;
var divMargin = 0;
var valuePath = [];

// 
function recursive_getPayloadValuesResponse(messageKey, payload, container, value_special_key, rowCountResp, fieldName){

    zLevelCount++; // the strructure level count
    var zLevelResp = document.createElement('div'); // create a div that will hold all messages for this layer

    //give a layer id, className and the css z-index
    zLevelResp.id = "zLevelResp"+zLevelCount;
    zLevelResp.className = "appendedDivResp boxShadowResp";
    zLevelResp.style.zIndex = zLevelCount;
    zLevelResp.style.boxShadow = '-1px -1px 10px -3px rgb(0, 0, 0)';
    zLevelResp.style.marginLeft = divMargin+10+'px';
    // append this layer to the main container
    container.append(zLevelResp);
    //get the layer by ID and create a table for storing name and values
    $('#'+zLevelResp.id).append('<table id="PayTableResp'+zLevelCount+'" style="width:100%"></table>');
    // create a table variable containing the current table ID
    var table = "PayTableResp"+zLevelCount;

    // check if payload passed is array.
    if($.isArray(payload)){
        // holds the number of rows in a payload
        $.each(payload, function(keyField, field){
            rowCountResp++;
            elementCount++;
            // create a div for holding each row/element/field of the payload
            var divElementResp = document.createElement('div');
            divElementResp.id = 'elementResp'+elementCount;
            divElementResp.className = "appendedDivResp";
            zLevelResp.append(divElementResp);

            if( ('enumType' in field) == false && ('value'in field) == false ){
                ElementIdResp = divElementResp.id
                $('#'+ElementIdResp).append('<br/><p class="structField" id="structField'+zLevelCount+'_'+elementCount+'"  onclick="toggleStruct(structField'+zLevelCount+'_'+elementCount+')" ><i class="fa fa-angle-double-right"></i> '+ field['name'] +'</p>');
                if(value_special_key.endsWith('Payload')){
                    value_special_key += '_'+keyField;
                }else{
                    value_special_key += '_members_'+keyField;
                }
                
                var newfieldName = fieldName+field["name"]
                recursive_getPayloadValuesResponse(messageKey, field['members'], zLevelResp, value_special_key, rowCountResp, newfieldName);
            }
            
            else if( ('enumType' in field) == false && 'value'in field ){
                var fieldNameTemp = fieldName+field["name"]
                if(dctKeyAlreadyExists.hasOwnProperty(fieldNameTemp)){
                    dctKeyAlreadyExists[fieldNameTemp] = parseInt(dctKeyAlreadyExists[fieldNameTemp])+1;
                    fieldNameTemp = fieldName+field["name"]+dctKeyAlreadyExists[fieldNameTemp];
                }else{
                    dctKeyAlreadyExists[fieldNameTemp] = 0;
                }

                ElementIdResp = divElementResp.id
                $('#'+table).append('<tr id="'+table+'PayRow'+rowCountResp+'Resp" ></tr>');
                $('#'+table+'PayRow'+rowCountResp+'Resp').append('<td class="PaytableLabelsResp">'+ field['name'] + '</td><td title="'+ field['value'] +'"><input class="'+value_special_key+'_'+ keyField+' NewTab_'+messageKey+'_'+fieldNameTemp+'" id="text_'+ElementIdResp+'" type="text" name="'+ field['name'] +'" value="'+ field['value'] +'" disabled="disabled" /></td>');
                
                TextBoxHandle = document.getElementById("text_" + ElementIdResp);
                TextBoxHandle.addEventListener('focusout', changeValue.bind(TextBoxHandle));
            }
            
            else if( 'enumType'in field ){
                var enumFieldNameTemp = messageKey+"_"+fieldName+field["name"]

                if(dctKeyAlreadyExists.hasOwnProperty(enumFieldNameTemp)){
                    dctKeyAlreadyExists[enumFieldNameTemp] = parseInt(dctKeyAlreadyExists[enumFieldNameTemp])+1;
                    enumFieldNameTemp = fieldName+field["name"]+dctKeyAlreadyExists[enumFieldNameTemp];
                }else{
                    dctKeyAlreadyExists[enumFieldNameTemp] = 0;
                }
                
                dctGetMembers = {}
                ElementIdResp = divElementResp.id
                var enumVal = '';
                var selArray = [];
                $.each(field['members'], function(key, value){

                    dctGetMembers[value] = key
                    

                    if(value == field['value']){
                        enumVal = key
                        selArray.push('<option value='+key+' selected="selected" >'+key+'</option>');
                    }else{
                        selArray.push('<option value='+key+' >'+key+'</option>');
                    }
                });
                selectBoxMembers[enumFieldNameTemp] = dctGetMembers
                $('#'+table).append('<tr id="'+table+'PayRow'+rowCountResp+'Resp" ></tr>');
                $('#'+table+'PayRow'+rowCountResp+'Resp').append('<td class="PaytableLabelsResp" >'+ field['name'] + '</td><td title="'+enumVal+'" ><select class="'+value_special_key+'_'+keyField+' '+enumFieldNameTemp+'" id="text_' + ElementIdResp + '" name="'+ field['name'] +'" disabled="disabled" >'+selArray+'</select></td>');
                
            }
        });
    }
}

var dctKeyAlreadyExists = {};
async function viewMsgResponseNewTab(data, clickedMsgIDPar){
    data = data['xmls'];
    msgResp = clickedMsgIDPar;
    $.each(data, function(index, xml){
        if(msgResp in xml['Messages']){
            Msg        = xml['Messages'][msgResp];
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
                        $('#row'+key+'Resp').append('<td class="tableLabelsResp">'+ key +'</td><td><input type="text" id="text_'+fieldID+'" class="Messages_'+msgResp+'_HeaderRespNewTab_'+key+'" name="_'+ key +'" value="'+ value +'" disabled /></td>');
                        
                        TextBoxHandle = document.getElementById("text_"+fieldID);
                        TextBoxHandle.addEventListener('focusout', changeHeaderValue.bind(TextBoxHandle));

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
    recursive_getPayloadValuesResponseNewTab(messageKey, MsgPayload, container, value_special_key, rowCountResp, fieldName);
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
var elementCount = 0;
var zLevelCount = 0;
var divMargin = 0;
var valuePath = [];

// 
function recursive_getPayloadValuesResponseNewTab(messageKey, payload, container, value_special_key, rowCountResp, fieldName){

    zLevelCount++; // the strructure level count
    var zLevelResp = document.createElement('div'); // create a div that will hold all messages for this layer

    //give a layer id, className and the css z-index
    zLevelResp.id = "zLevelResp"+zLevelCount;
    zLevelResp.className = "appendedDivResp boxShadowResp";
    zLevelResp.style.zIndex = zLevelCount;
    zLevelResp.style.boxShadow = '-1px -1px 10px -3px rgb(0, 0, 0)';
    zLevelResp.style.marginLeft = divMargin+10+'px';
    // append this layer to the main container
    container.append(zLevelResp);
    //get the layer by ID and create a table for storing name and values
    $('#'+zLevelResp.id).append('<table id="PayTableResp'+zLevelCount+'" style="width:100%"></table>');
    // create a table variable containing the current table ID
    var table = "PayTableResp"+zLevelCount;

    // check if payload passed is array.
    if($.isArray(payload)){
        // holds the number of rows in a payload
        $.each(payload, function(keyField, field){
            rowCountResp++;
            elementCount++;
            // create a div for holding each row/element/field of the payload
            var divElementResp = document.createElement('div');
            divElementResp.id = 'elementResp'+elementCount;
            divElementResp.className = "appendedDivResp";
            zLevelResp.append(divElementResp);

            if( ('enumType' in field) == false && ('value'in field) == false ){
                ElementIdResp = divElementResp.id
                $('#'+ElementIdResp).append('<br/><p class="structField" id="structField'+zLevelCount+'_'+elementCount+'"  onclick="toggleStruct(structField'+zLevelCount+'_'+elementCount+')" ><i class="fa fa-angle-double-right"></i> '+ field['name'] +'</p>');
                if(value_special_key.endsWith('Payload')){
                    value_special_key += '_'+keyField;
                }else{
                    value_special_key += '_members_'+keyField;
                }
                
                var newfieldName = fieldName+field["name"]
                setTimeout(recursive_getPayloadValuesResponseNewTab(messageKey, field['members'], zLevelResp, value_special_key, rowCountResp, newfieldName), 200);
            }
            
            else if( ('enumType' in field) == false && 'value'in field ){
                var fieldNameTemp = fieldName+field["name"]
                if(dctKeyAlreadyExists.hasOwnProperty(fieldNameTemp)){
                    dctKeyAlreadyExists[fieldNameTemp] = parseInt(dctKeyAlreadyExists[fieldNameTemp])+1;
                    fieldNameTemp = fieldName+field["name"]+dctKeyAlreadyExists[fieldNameTemp];
                }else{
                    dctKeyAlreadyExists[fieldNameTemp] = 0;
                }

                ElementIdResp = divElementResp.id
                $('#'+table).append('<tr id="'+table+'PayRow'+rowCountResp+'Resp" ></tr>');
                $('#'+table+'PayRow'+rowCountResp+'Resp').append('<td class="PaytableLabelsResp">'+ field['name'] + '</td><td title="'+ field['value'] +'"><input class="'+value_special_key+'_'+ keyField+' NewTab_'+messageKey+'_'+fieldNameTemp+'" id="text_'+ElementIdResp+'" type="text" name="'+ field['name'] +'" value="'+ field['value'] +'" disabled="disabled" /></td>');
                
                TextBoxHandle = document.getElementById("text_" + ElementIdResp);
                TextBoxHandle.addEventListener('focusout', changeValue.bind(TextBoxHandle));
            }
            
            else if( 'enumType'in field ){
                var enumFieldNameTemp = messageKey+"_"+fieldName+field["name"]

                if(dctKeyAlreadyExists.hasOwnProperty(enumFieldNameTemp)){
                    dctKeyAlreadyExists[enumFieldNameTemp] = parseInt(dctKeyAlreadyExists[enumFieldNameTemp])+1;
                    enumFieldNameTemp = fieldName+field["name"]+dctKeyAlreadyExists[enumFieldNameTemp];
                }else{
                    dctKeyAlreadyExists[enumFieldNameTemp] = 0;
                }
                
                dctGetMembers = {}
                ElementIdResp = divElementResp.id
                var enumVal = '';
                var selArray = [];
                $.each(field['members'], function(key, value){

                    dctGetMembers[value] = key
                    

                    if(value == field['value']){
                        enumVal = key
                        selArray.push('<option value='+key+' selected="selected" >'+key+'</option>');
                    }else{
                        selArray.push('<option value='+key+' >'+key+'</option>');
                    }
                });

                selectBoxMembers[enumFieldNameTemp] = dctGetMembers
                $('#'+table).append('<tr id="'+table+'PayRow'+rowCountResp+'Resp" ></tr>');
                $('#'+table+'PayRow'+rowCountResp+'Resp').append('<td class="PaytableLabelsResp" >'+ field['name'] + '</td><td title="'+enumVal+'" ><select class="'+value_special_key+'_'+keyField+' '+enumFieldNameTemp+'" id="text_' + ElementIdResp + '" name="'+ field['name'] +'" disabled="disabled" >'+selArray+'</select></td>');
                
            }
        });
    }
}

/**
 * @param {*}
 * @description:
 *      this function changes the value on the json file with a change on the input
 * @returns: No return value
 */

function changeValue(){
    val = this.value
    thisClassName = this.className;
    lstPathKey = thisClassName.split('_');
    lstPathKey.push(val);

    var payloadFoundForKey = false;
    var payloadFound = false;
    var dctCounter = 0;
    dctPath = {};
    dctKey = [];
    var ackeyPath = "";

    $.each(lstPathKey, function(key, val){
        if(val == "Payload"){
            payloadFoundForKey = true;
            ackeyPath = dctKey.join("_");
        }
        if(!payloadFoundForKey){
            if(val != "Messages"){
                dctKey.push(val);
            }
        }
    });
    dctPath[dctCounter++] = ackeyPath;
    $.each(lstPathKey, function(key, val){
        if(val == "Payload"){
            payloadFound = true;
        }if(payloadFound){
            dctPath[dctCounter++] = val;
        }
    });
    G_changedValues.push(dctPath);

    $(".loader_ring").empty();
    document.querySelector(".loader").style.visibility = "visible";

    parentClass = $(this).parent().attr("class");
    if(parentClass == "AutoScriptMessage"){
        $.ajax({
            type: 'POST',
            url : '/autoScriptMessage',
            data: dctPath
        })
        .done(function(msg){
            console.log("sent");
            document.querySelector(".loader").style.visibility = "hidden";
        });
    }else{
        $.ajax({
            type: 'POST',
            url : '/message',
            data: dctPath
        })
        .done(function(msg){
            console.log("sent");
            document.querySelector(".loader").style.visibility = "hidden";
        });
    }
}

/**
 * @param {*}
 * @description:
 *      this function changes the value on the json file with a change on the input on the header
 * @returns: No return value
 */

function changeHeaderValue(){
    val = this.value
    thisClassName = this.className;
    lstPathKey = thisClassName.split('_');
    var refCounter = 0;
    lstPathKey.push(val);
    var lstRefKey = [];
    var acPath = "";
    dctPath = {}

    $.each(lstPathKey, function(key, val){
        if(val != "Messages" && key < (lstPathKey.length)-3){
            lstRefKey.push(val)
        }
    });
    acPath = lstRefKey.join("_");
    dctPath[0] = acPath;
    dctPath[1] = lstPathKey[lstPathKey.length-2];
    dctPath[2] = lstPathKey[lstPathKey.length-1];
    
    parentClass = $(this).parent().attr("class");
    if(parentClass == "AutoScriptMessage"){
        $.ajax({
            type: 'POST',
            url : '/editAutoScriptHeader',
            data: dctPath
        })
        .done(function(msg){
            console.log("done");
            document.querySelector(".loader").style.visibility = "hidden";
        });
    }else{
        $.ajax({
            type: 'POST',
            url : '/editHeader',
            data: dctPath
        })
        .done(function(msg){
            console.log("done");
        });
    }
}
/**
 * @param {* holds the id of the field} fieldId
 * @description:
 *      This function toggles the structure when called
 * @returns: No return value
 */
function toggleStruct(fieldId){
    $('#'+fieldId.id).parent().next('div').toggle('fast');
    $('#'+fieldId.id+' > .fa-angle-double-right').toggleClass('flip')
}

function toggleAllstructures(){
    $('.structField').parent().next('div').toggle('fast');
    $('.structField > .fa-angle-double-right').toggleClass('flip')
}
 /**
 * @param {*}
 * @description:
 *      Fade in or out the if the messge is recording on the message list (Left panel)
 * @returns: No return value
 */

var state = 1;
function toggleRecord() {
    setInterval(function(){
        $.ajax({
            type: 'GET',
            url: '/getRecord',
            dataType: 'json',
            async: true,
            success: function(data){
                var data = JSON.parse(data);
                if($.inArray(msgID, data['msgs']) != -1){
                    if(state == 0){
                        $('.record_status'+msgID+' img').fadeTo( "slow", 0.2);
                        state = 1;
                    }else{
                        $('.record_status'+msgID+' img').fadeTo( "slow", 1);
                        state = 0;
                    }
                }
            }
        });
    },1000);
}

 /**
 * @param {* json string of all messages on the message manager} receivedMsgs
 * @description:
 *      The response panel/right panel, same as viewMsg/middle panel
 * @returns: No return value
 */

/**
 * @param {* json string of all messages on the message manager} receivedMsgs
 * @description:
 *      The response panel/right panel, same as viewMsg/middle panel
 * @returns: No return value
 */

/**
 * @param {* json string of all messages on the message manager} receivedMsgs
 * @description:
 *      The response panel/right panel, same as viewMsg/middle panel
 * @returns: No return value
 */

/**
 * @param {* json string of all messages on the message manager} receivedMsgs
 * @description:
 *      The response panel/right panel, same as viewMsg/middle panel
 * @returns: No return value
 */