$(document).ready(function () {
   $(".flashes").hide();
   $(".flashes").fadeTo(2000, 500).slideUp(500, function() {
      $(".flashes").slideUp(500);
   });
});