let slider_item1 = document.querySelectorAll('.swiper')



// For first
$(".swiper").eq(0).mouseenter(function(){
    swiper.autoplay.stop();
});


$(".swiper").eq(0).mouseleave(function(){
    swiper.autoplay.start();
});






// For second
$(".swiper").eq(1).mouseenter(function(){
    swiper1.autoplay.stop();
});

$(".swiper").eq(1).mouseleave(function(){
    swiper1.autoplay.start();
});






// For third
$(".swiper").eq(2).mouseenter(function(){
    swiper2.autoplay.stop();
});

$(".swiper").eq(2).mouseleave(function(){
    swiper2.autoplay.start();
});




// For fourth
$(".swiper").eq(3).mouseenter(function(){
    swiper3.autoplay.stop();
});

$(".swiper").eq(3).mouseleave(function(){
    swiper3.autoplay.start();
});








// For fifth
$(".swiper").eq(4).mouseenter(function(){
    swiper4.autoplay.stop();
});

$(".swiper").eq(4).mouseleave(function(){
    swiper4.autoplay.start();
});





var swiper = new Swiper(slider_item1[0], {
    autoplay: {
      delay: 7000,
      disableOnInteraction: false,
    },
    speed: 2000,
    centeredSlides: true,
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },

    simulateTouch: true,
    loop: true,
    grabCursor: true,
    

});




var swiper1 = new Swiper(slider_item1[1], {
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

        325: {
            slidesPerView:2,
        },

        440: {
            slidesPerView: 2,
        },

        660: {
          slidesPerView: 2,
        },
        992: {
            slidesPerView: 4,
          }
      },
});


var swiper2 = new Swiper(slider_item1[2], {
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
        660: {
          slidesPerView: 2,
        },
        992: {
            slidesPerView: 4,
          }
      },
});


var swiper3 = new Swiper(slider_item1[3], {
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
        660: {
          slidesPerView: 2,
        },
        992: {
            slidesPerView: 4,
          }
      },
});


var swiper4 = new Swiper(slider_item1[4], {
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
        660: {
          slidesPerView: 2,
        },
        992: {
            slidesPerView: 4,
          }
      },
});














