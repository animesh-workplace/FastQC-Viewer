$(document).ready(function () {
  $(".nav-toggler").on("click", function () {
    console.log("Hello")
    $("navbar-toggler").toggleClass("is-active");
    $(".navbar-menu").toggleClass("is-active");
  });

  $(".multiqc").click(function () {
   var id = $(this).attr("href").toString();
   console.log(id)
   $.ajax({
    type: "GET",
    url: "media/Project/" + id + "/multiqc_report.html",
   })
  });
});

