$(document).ready(function(){
    $('#youpray').hide().fadeIn(1000);
    $("#timedropdownul a").hide();
    $('.timedropselected').click(function(){
        $('#timedropdownul a').toggle();

    });


    $('.timedropitem').hover(function(){
        $(this).toggleClass('timedrophover');
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
        });
        }
 });
};

