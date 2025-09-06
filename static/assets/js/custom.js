(function ($) {

  "use strict";

  $(window).on('load', function () {
    $('#js-preloader').addClass('loaded');
    if ($('.cover').length) {
      $('.cover').parallax({
        imageSrc: $('.cover').data('image'),
        zIndex: '1'
      });
    }
    $("#preloader").animate({
      'opacity': '0'
    }, 600, function () {
      setTimeout(function () {
        $("#preloader").css("visibility", "hidden").fadeOut();
      }, 300);
    });
  });

  $(window).scroll(function () {
    var scroll = $(window).scrollTop();
    var box = $('.header-text').height();
    var header = $('header').height();
    if (scroll >= box - header) {
      $("header").addClass("background-header");
    } else {
    }
  });

  var width = $(window).width();
  $(window).resize(function () {
    if (width > 767 && $(window).width() < 767) {
      location.reload();
    } else if (width < 767 && $(window).width() > 767) {
      location.reload();
    }
  });

  $(document).ready(function () {
    
    if ($('.menu-trigger').length) {
      $(".menu-trigger").on('click', function () { 
        // منوی اصلی را باز و بسته می‌کند
        $('.header-area').toggleClass('menu-open');
        // اسکرول صفحه را قفل/آزاد می‌کند
        $('body').toggleClass('menu-is-open');

        // دو عکس همبرگر و ضربدر را جابجا می‌کند
        $(this).find('#hamburger-img').toggle();
        $(this).find('#close-img').toggle();
      });
    }

    $('#themeToggleMobile').on('click', function () {
      $('#themeToggle').click();
    });

    $('#themeToggle').on('click', function () {
      setTimeout(function () {
        var isDarkMode = $('body').hasClass('dark-mode');
        if (isDarkMode) {
          $('#moonIconMobile').hide();
          $('#sunIconMobile').show();
        } else {
          $('#moonIconMobile').show();
          $('#sunIconMobile').hide();
        }
      }, 10);
    });

    $('.scroll-to-section a[href*=\\#]:not([href=\\#])').on('click', function () {
      if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
        var target = $(this.hash);
        target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
        if (target.length) {
          var width = $(window).width();
          
          if (width < 992 && $('.header-area').hasClass('menu-open')) {
            $('.menu-trigger').click();
          }

          $('html,body').animate({
            scrollTop: (target.offset().top) - 80
          }, 700);
          return false;
        }
      }
    });

    $('.owl-banner').owlCarousel({
      center: true, items: 1, loop: true, nav: true,
      navText: ['<i class="fa fa-angle-left" aria-hidden="true"></i>', '<i class="fa fa-angle-right" aria-hidden="true"></i>'],
      margin: 30, responsive: { 992: { items: 1 }, 1200: { items: 1 } },
      autoplay: true, autoplayTimeout: 3000, autoplayHoverPause: true,
    });

    $('.owl-testimonials').owlCarousel({
      center: true, items: 1, loop: true, nav: true,
      navText: ['<i class="fa fa-angle-left" aria-hidden="true"></i>', '<i class="fa fa-angle-right" aria-hidden="true"></i>'],
      margin: 30, responsive: { 992: { items: 1 }, 1200: { items: 1 } }
    });

    const elem = document.querySelector('.event_box');
    const filtersElem = document.querySelector('.event_filter');
    if (elem) {
      const rdn_events_list = new Isotope(elem, {
        itemSelector: '.event_outer',
        layoutMode: 'masonry'
      });
      if (filtersElem) {
        filtersElem.addEventListener('click', function (event) {
          if (!event.target.matches('a')) { return; }
          const filterValue = event.target.getAttribute('data-filter');
          rdn_events_list.arrange({ filter: filterValue });
          filtersElem.querySelector('.is_active').classList.remove('is_active');
          event.target.classList.add('is_active');
          event.preventDefault();
        });
      }
    }
    
    const dropdownOpener = $('.main-nav ul.nav .has-sub > a');
    if (dropdownOpener.length) {
      dropdownOpener.each(function () {
        var _this = $(this);
        _this.on('tap click', function (e) {
          var thisItemParent = _this.parent('li');
          var submenu = thisItemParent.find('> ul.sub-menu');
          if (submenu.is(':visible')) {
            submenu.slideUp(450, 'easeInOutQuad');
            thisItemParent.removeClass('is-open-sub');
          } else {
            thisItemParent.addClass('is-open-sub');
            thisItemParent.siblings().removeClass('is-open-sub').find('.sub-menu').slideUp(250, 'easeInOutQuad', function () {
              submenu.slideDown(250, 'easeInOutQuad');
            });
          }
          e.preventDefault();
        });
      });
    }

  });

})(window.jQuery);

