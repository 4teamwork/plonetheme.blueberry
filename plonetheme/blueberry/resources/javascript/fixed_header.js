(function($) {

  function adjustHeader() {
    $("#container").css("padding-top", $(".masthead").outerHeight());
  }

  $(function() {
    if($(".blueberry-marketing").length) {
      adjustHeader();
    }
  });

})(window.jQuery);
