/*"""-----------------------------------------------------------------------------

Company  : Reutech Radar Systems
Designer : T Ramukosi
Mentor   : J Taylor
Generated: 2018-08-30
-----------------------------------------------------------------------------*/
// "use strict";
var msgID = '';
var msgResp;
var selectBoxMembers = {};
var G_changedValues = [];

$(document).ready(function(){
    setTimeout(function(){
        event_message_clicked(); // this event is triggered everytime a message is clicked (left panel)
        event_autoScriptMessage_clicked()
        event_toggle_items(); //collapse all the messages on document load and expand when clicked
    },5000);
    event_sendValues(); // Handles the send event, get all the values from mid panel fields and send to server
    event_updateValues();
    event_autoSend();
    event_startAutoscript();
    event_addToScript();
    event_changeScriptType();
    event_toggleWhenClicked(); // toggles pipe information when clicked
    event_toggleAutoScriptWhenClicked();
    event_record(); // Start and stop recording when the record button is clicked, show if the message is being recorded or not by fading in and out.
});