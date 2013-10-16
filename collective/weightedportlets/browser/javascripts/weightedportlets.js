function assignPortletWeight(weight) {
    var portlet = $(weight);
    var data = {'weight': portlet.find('input.weight').val(),
                'portlethash': portlet.attr('data-portlethash')};
    var assignW = $.ajax({
         data: data,
         type: "GET",
         async: false,
         url: "@@assign-weight-info",
         success: function(html) {
             portlet.prepend(html);
         },
         error: function(){
             portlet.prepend('Error saving weightings');
             return 'error';
         }
    }).responseText;
    return assignW;
}

$(document).ready(function() {
    if($('.portletAssignments .weight').length > 0) {
       $('.portletAssignments form').submit(function(e) {
           var portletid = ($(this).closest('.portlets-manager').attr('id'));
           if($('.weightedmessage').length > 0) {
              $('.weightedmessage').remove();
           }
           var weights = $('#'+portletid+' .portlet');
           for (var i = 0; i < weights.length; ++i) {
              var assignWeight = assignPortletWeight(weights[i]);
              if (assignWeight.indexOf('Error') > -1) {
                  return false;
              }
           }
       });
    }
});
