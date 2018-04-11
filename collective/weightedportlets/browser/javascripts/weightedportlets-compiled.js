$(document).ready(function() {
  if($('.portletAssignments .weight').length > 0) {
    $('.portletAssignments .weight').blur(function() {
      $('.weightedmessage').remove();
      var portlet = $(this).closest('.portlet');
      $.post('@@assign-weight-info',
        {'weight': $(this).val(), 'portlethash': $(this).attr('data-portlethash')},
        function(html) {
          if (html) { portlet.prepend(html); }
        },
        function() {
          portlet.prepend('Error saving weighting');
        }
      );
    });
  }
});
