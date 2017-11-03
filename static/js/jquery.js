$(document).ready(function() {

      if ($("#error_text").html().length == 0) {

            $("#error-box").hide();

        } else {

            $("#error-box").show();
            $("#error-box").removeClass('hidden');

        }
});

// Window load event used just in case window height is dependant upon images
$(window).bind("load", function() {

       var footerHeight = 0,
           footerTop = 0,
           $footer = $("#footer_js");

       positionFooter();

       function positionFooter() {

                footerHeight = $footer.height();
                footerTop = ($(window).scrollTop()+$(window).height()-footerHeight)+"px";

               if ( ($(document.body).height()+footerHeight) < $(window).height()) {
                   $footer.css({
                        position: "absolute"
                   }).animate({
                        top: footerTop
                   })
               } else {
                   $footer.css({
                        position: "static"
                   })
               }

       }

       $(window)
               .scroll(positionFooter)
               .resize(positionFooter)

});


$('input').focus(function(){
  $(this).parents('.form-group').addClass('focused');
});

$('input').blur(function(){
  var inputValue = $(this).val();
  if ( inputValue == "" ) {
    $(this).removeClass('filled');
    $(this).parents('.form-group').removeClass('focused');
  } else {
    $(this).addClass('filled');
  }
})