let slider_item1 = document.querySelectorAll('.swiper')


// For first
$(".swiper").eq(0).mouseenter(function(){
    swiper.autoplay.stop();
});


$(".swiper").eq(0).mouseleave(function(){
    swiper.autoplay.start();
});



if($(".swiper-slide").length === 1 || $(".swiper-slide").length === 0){
  $('.main-title1').css('display', 'none')
  $('.products').css('display', 'none')
// $(".swiper-button").css("display", "none");
}



var swiper = new Swiper(slider_item1[0], {
  autoplay: {
      delay: 7000,
      disableOnInteraction: false,
  },
  speed: 2000,
  slidesPerView: 4,

  loop:true,
  grabCursor: true,

  breakpoints: {

      1: {
          slidesPerView:1,
      },
      
      480: {
        slidesPerView: 1,
      },
      661: {
        slidesPerView: 2,
      },
      992: {
          slidesPerView: 4,
        }
    },
});
