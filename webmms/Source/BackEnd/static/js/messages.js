/*"""-----------------------------------------------------------------------------

Company  : Reutech Radar Systems
Designer : T Ramukosi
Mentor   : J Taylor
Generated: 2018-08-30
-----------------------------------------------------------------------------*/
// "use strict";
var receivedMsgs = '';
var favMsgs = {};
var G_dctReceivedMessagesInterval;
var G_dctAutoScriptMessages;
$(document).ready(function(){
    event_toggleAllFavMsgs(); // collapse all message when document loaded
    ajax_getAllFavMsgs(); // get all favorite messages from 
    clearInterval(G_dctReceivedMessagesInterval);
    dctReceivedMessages();
    ajax_get_all_messages(); //get list of all messages and favorite messages from the server and populate them on the document
    event_filterMsgs(); // filter message on keyup (search box)
    event_filterAutoScriptMsgs(); // filter message on keyup (search box)
    event_checkBoxAttr();// add to favorite everytime a checkbox is checked and remove when unchecked
    event_toggle_fav(); // toggle favorite messages list when the Favourite Messages button is clicked
    event_removeFavMsgs(); // remove a message from favorite when the remove button is clicked
    event_filterFavMsgs(); // filter favourite messages
    document.querySelector(".loader").style.visibility = "hidden";
    document.querySelector(".preloader").style.visibility = "hidden";

});