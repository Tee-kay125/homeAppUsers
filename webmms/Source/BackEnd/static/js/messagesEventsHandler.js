/*"""-----------------------------------------------------------------------------

Company  : Reutech Radar Systems
Designer : T Ramukosi
Mentor   : J Taylor
Generated: 2018-08-30
-----------------------------------------------------------------------------*/
// "use strict";

/** ----------------------------------------------------------------- Events for script-> messages.js ------------------------------------------- */
function event_toggleAllFavMsgs(){
    $('.FavMsgsMessage > li').toggle("fast");
}

function ajax_getAllFavMsgs(){
    $.ajax({
        type: 'GET',
        url: '/favMsgs.json',
        dataType: 'json',
        async: true,
        success: function(data){
            favMsgs = data;
        },
        error: function(msg){
            console.log('error getting Favmessages (6) requestedFile: favMsgs.json, script:messages.js');
        }
    }); 
}

function ajax_get_all_messages(){
    $.ajax({
        type: 'GET',
        url: '/output.json',
        dataType: 'json',
        async: true,
        success: function(data){
            lstMsgs(data[1]);
            lstFavMsgs(data[1]);
            lstAutoScriptMessages(data[2]);
            G_dctAutoScriptMessages = data[2];
        },
        error: function(msg){
            console.log('error getting messages (5) requestedFile: output.json, script:messages.js');
        }
    });
}

function event_filterMsgs(){
    $("#filterBox").keyup(function(){
        var filter;
        filter = this.value.toUpperCase();
        liToFilter = $(".messageLink");
        $.each(liToFilter, function(key, value){
            element = $("#"+value.id);
            elementText = element.text().toUpperCase();
            if(elementText.indexOf(filter) != -1){
                element.parent("li").parent("ul").show();
            }else{
                element.parent("li").parent("ul").hide();
            }
        });
    });
}

function event_checkBoxAttr(){
    $(document).on('click', '#checkBoxAttr', function(){
        if($(this).is(':checked')){
            val = $(this).val();
            dctValues = {'value':val};
            $.ajax({
                type: 'POST',
                url : '/editFavs',
                data: dctValues
            })
            .done(function(msg){
                console.log("checkbox Clicked");
            });
        }else{
            val = $(this).val();
            dctValues = {'value2':val};
            $.ajax({
                type: 'POST',
                url : '/editFavs',
                data: dctValues
            })
            .done(function(msg){
                console.log("done");
            });
        }
    });
}

function  event_toggle_fav(){
    $(document).on('click', '.FavMsgsMessage > p', function(){
        $('.FavMsgsMessage > li').toggle("fast");
        $('.FavMsgsMessage > p > i').toggleClass('flip');
    });
}

function event_removeFavMsgs(){
    $(document).on('click', '.removeFavMsg', function(){
        $(this).parent().addClass("displayNone");

        val = this.id;
        dctValues = {'valueFav':val};
        $.ajax({
            type: 'POST',
            url : '/editFavs',
            data: dctValues
        })
            .done(function(msg){
                console.log("done");
            });
    });
}

function event_filterFavMsgs(){
    $(document).on('click', '#filter > .fa-search', function(){
        $('#filterBox').toggle('fast');
    });
}