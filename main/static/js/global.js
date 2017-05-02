 // menu
 jQuery(document).ready(function() {
                  jQuerymenuLeft = jQuery('.pushmenu-left');
                  jQuerynav_list = jQuery('#nav_list');
                  
                  jQuerynav_list.click(function() {
                    jQuery(this).toggleClass('active');
                    jQuery('.pushmenu-push').toggleClass('pushmenu-push-toright');
                    jQuerymenuLeft.toggleClass('pushmenu-open');
                  });
                  
                  $("li.drop_down_menu").click(function(e){
              if (this == e.target) {
                $(this).toggleClass('open');
                $(this).children('ul').slideToggle('fast');
              }
              
                }); 
                   
            
              });

 // slider
 jQuery(document).ready(function() {
        jQuery('.fade').slick({
        dots: false,
        infinite: false,
        arrows: false,
        speed: 1000,
        dotsClass: 'slick-dots container',
        fade: true,
        autoplay: true,
        cssEase: 'linear'
      });
    });

// login
$('.click_form').hide();
    $('.login_icon').click(function(e){
        e.preventDefault();
        $('.click_form').fadeToggle(400);
    });

// new
     var nt_example1 = $('#nt-example1').newsTicker({
                row_height: 85,
                max_rows: 3,
                duration: 10000,
                prevButton: $('#nt-example1-prev'),
                nextButton: $('#nt-example1-next')
            });