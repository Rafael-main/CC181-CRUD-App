$(document).ready(function(){
    $("#courseInput").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      $("#deptcolcorTable tr").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
  }); 