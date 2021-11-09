$(document).ready(function () {
  $(".nav-toggler").on("click", function () {
    console.log("Hello")
    $("navbar-toggler").toggleClass("is-active");
    $(".navbar-menu").toggleClass("is-active");
  });
  $('#success').delay(3000).fadeOut('slow');
  $('#error').delay(3000).fadeOut('slow');
});

