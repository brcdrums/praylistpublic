$(document).ready(function(){
    $('#youpray').hide().fadeIn(1000);
    $("#timedropdownul a").hide();
    $('.savedgroup').hide();
    $('#managegroups').hide();
    $('.timedropselected').click(function(){
        $('#timedropdownul a').toggle();

    });


    $('.timedropitem').hover(function(){
        $(this).toggleClass('timedrophover');
    });

        $('.savedgroup').hover(function(){
        $(this).toggleClass('savedgrouphover');
    });


    $('#mygroupsfirst').click(function() {
        $("#managegroups").toggle();
        $('.savedgroup').toggle();
    });


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    crossDomain: false, // obviates need for sameOrigin test
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

  });



function voteitem(postid) {
     $.ajax({
        url: "/post/" + postid + "/",
        success: function(html) {
            $('#upvote').fadeOut('slow', function() {
                var div = $("<p id=\"youpray\">√ You've prayed for this!</p>").hide();
                $(this).replaceWith(div);
                $('#youpray').fadeIn('slow');
            var scorenum = parseInt(document.getElementById("prayerscore").innerHTML.slice(9));
            $('#prayerscore').fadeOut('slow', function(){
                var newscore = scorenum + 1;
                $('#prayerscore').replaceWith("<p id=\"prayerscore\" style=\"color: red;\">Prayers: " + newscore + "</p>");
                $('#prayerscore').fadeIn('slow');
            });
        });
        }
 });
};


function subscribe(groupid, groupname) {
    var clickedclass = ".subscribe " + groupid;
    $.ajax({
        url: "/managegroups/" + groupid + "/",
        success: function(html) {
            $("button[class*=" + groupid + "]").replaceWith("<button class=\"subscribe {{ group.id }}\" onclick=\"unsubscribe({{ group.id }})\">Saved!</button>");
            $("<li class=\"savedgroup\" style=\"display: list-item;\"><a href=\"/group/Cancer/trending/\">" + groupname + "</a></li>").insertAfter($('.savedgroup').last());
            $('#mygroups > li:contains(' + groupname + ')').hide();
    }
    });
}; 

function unsubscribe(groupid, groupname) {
    $.ajax({
        url: "/managegroups/" + groupid + "/unsubscribe/",
        success: function(html) {
            $("button[class*=" + groupid + "]").replaceWith("<button class=\"subscribe {{ group.id }}\" onclick=\"subscribe({{ group.id }})\">Save</button>");
            $("#mygroups > li > a:contains(" + groupname + ")").remove();

    }
    });
}; 

