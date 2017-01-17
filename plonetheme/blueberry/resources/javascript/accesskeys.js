(function($) {

  $(function() {
      // Change accesskey of sitemap to 4, since 3 is reserved for the contact form.
      $('#siteaction-sitemap a').attr('accesskey', '4');

      // Change accesskey of accessibilit-info to 9, since 0 is reserved for the startpage.
      $('#siteaction-accessibility a').attr('accesskey', '9');
  
      // Move curser into the searchbox with accesskey 5.
      $('input#searchGadget').attr('accesskey', '5');
      // Change advanced search accesskey to 6 if available
      $('#portal-advanced-search > a').attr('accesskey', '6')
    }
  );

})(window.jQuery);
