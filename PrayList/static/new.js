$(document).ready(function(){
    $('#youpray').hide().fadeIn(1000);
    $("#timedropdownul a").hide();
    $('.savedgroup').hide();
    $('#managegroups').hide();
    $('.topsavebutton').css("opacity", 0);
    $('.savedgroupplaceholder').hide();
    $('.timedropselected').click(function(){
        $('#timedropdownul a').toggle();

    });


    $('.timedropitem').hover(function(){
        $(this).toggleClass('timedrophover');
    });

        $('.savedgroup').hover(function(){
        $(this).children("a").toggleClass('savedgrouphover');
    });


    $('#mygroupsfirst').click(function() {
        $("#managegroups").toggle();
        $('.savedgroup').toggle();
    });

    $('.populargroupitem').hover(function() {
        $(this).children("button").css('opacity', 100);
        }, function() {
            $(this).children("button").css('opacity', 0);
    });

    $('.populargroupitemselected').hover(function() {
        $(this > '.topsavebutton').css('opacity', 100);
        }, function() {
            $(this > '.topsavebutton').css('opacity', 0);
    });

});

// function getCookie(name) {
//     var cookieValue = null;
//     if (document.cookie && document.cookie != '') {
//         var cookies = document.cookie.split(';');
//         for (var i = 0; i < cookies.length; i++) {
//             var cookie = jQuery.trim(cookies[i]);
//             // Does this cookie string begin with the name we want?
//             if (cookie.substring(0, name.length + 1) == (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }
// var csrftoken = getCookie('csrftoken');
// function csrfSafeMethod(method) {
//     // these HTTP methods do not require CSRF protection
//     return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
// }
// $.ajaxSetup({
//     crossDomain: false, // obviates need for sameOrigin test
//     beforeSend: function(xhr, settings) {
//         if (!csrfSafeMethod(settings.type)) {
//             xhr.setRequestHeader("X-CSRFToken", csrftoken);
//         }
//     }
// });

//   });



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


function subscribe(groupid, groupname, isTop) {
    if(isTop==="True") {
        $(".topsavebutton").find("."+ groupid).replaceWith("<button class=\"topsavebutton " + groupid + "\" onclick=\"unsubscribe(" + groupid + ", \'" + groupname + "\', \'True\')\" style=\"opacity:100;\">unsave</button>");
    } else {
        $(".topsavebutton").find("."+ groupid).replaceWith("<button class=\"topsavebutton " + groupid + "\" onclick=\"unsubscribe(" + groupid + ", \'" + groupname + "\', \'True\')\" style=\"opacity:0;\">unsave</button>");
    }
    $(".subscribe[class*=" + groupid + "]").replaceWith("<button class=\"subscribe " + groupid + "\" onclick=\"unsubscribe(" + groupid + ", \'" + groupname + "\')\">Saved!</button>");
    $.ajax({
        url: "/managegroups/" + groupid + "/",
        success: function(html) {
            if($('.savedgroup').is('*')) {
                $("<li class=\"savedgroup\" style=\"display: list-item;\"><a href=\"/group/Cancer/trending/\">" + groupname + "</a></li>").insertAfter($('.savedgroup').last());
            } else {
                $("<li class=\"savedgroup\" style=\"display: list-item;\"><a href=\"/group/Cancer/trending/\">" + groupname + "</a></li>").insertAfter($('.savedgroupplaceholder'));
            }
            $('#mygroups > li:contains(' + groupname + ')').hide();
        }
    });
}; 

function unsubscribe(groupid, groupname, isTop) {
     if(isTop==="True") {
        $(".topsavebutton").find("."+ groupid).replaceWith("<button class=\"topsavebutton " + groupid + "\" onclick=\"subscribe(" + groupid + ", \'" + groupname + "\', \'True\')\" style=\"opacity:100;\">save</button>");
    } else {
        $(".topsavebutton").find("."+ groupid).replaceWith("<button class=\"topsavebutton " + groupid + "\" onclick=\"subscribe(" + groupid + ", \'" + groupname + "\', \'True\')\" style=\"opacity:0;\">save</button>");          
    }
    $(".subscribe[class*=" + groupid + "]").replaceWith("<button class=\"subscribe "+ groupid + "\" onclick=\"subscribe(" + groupid + ", \'" + groupname + "\')\">Save</button>");
    $.ajax({
        url: "/managegroups/" + groupid + "/unsubscribe/",
        success: function(html) {
            $("#mygroups > li > a:contains(" + groupname + ")").remove();
           
    }
    });
}; 



