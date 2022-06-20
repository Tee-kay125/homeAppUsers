/*"""-----------------------------------------------------------------------------

Company  : Reutech Radar Systems
Designer : T Ramukosi
Mentor   : J Taylor
Generated: 2018-08-30
-----------------------------------------------------------------------------*/
// "use strict";
var str_url_path = $(location).attr('pathname').toString();
var arr_xml_names = [];
var array_interface_xml_names = []
var savedNumOfXMls = 0;
var G_getFieldValuesAndUpdate;
var G_lstBusySendingAutoScripts = [];
$(document).ready(function(){
    event_getActivePipes();
    event_getPipes(); // Get pipes from server and call the loadPipes function to display all active pipes
    event_getXmls(); // Get xmls from server and call loadXmls function to display on the browser.
    event_getInterfaceXmls();
    event_hidePipeBlock(); // block for adding pipes is hidden when the page load
    event_rrs_logo();
    event_on_homePage(str_url_path); // display home page
    event_toggleActivePipeList();
    event_togglePipeList(); // Toggle the pipe list on document ready
    event_changeBackgroundColor();
    event_listOfActivePipes();
    event_listOfPipes(); // toggle pipe list on click
    event_editActivePipe();
    event_editPipe();
    event_addPipeButton(); //display a menu for adding pipes, when add pipe button is clicked
    event_addXmlButton(); //create an xml select input when a plus button is clicked
    event_connectPipe();
    event_savePipe();
    event_disconnectPipe();
    event_DeletePipe();
    event_reset();
    event_menu(); //manages menu, it changes the panel to active if clicked
    event_log();
    event_recorded();
    event_checked_messages();
    event_msg_checkBoxAttr();
    event_saveData();
    event_save_csv();
    event_deleteData();

    event_databaseMessages();
    event_createDAtabaseFile();
    event_submitToCreateDatabase()
    event_smallEvents();
});