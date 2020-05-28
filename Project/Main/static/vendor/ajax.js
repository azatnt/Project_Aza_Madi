$(function() {
    $('#search').keyup(function() {
        var search = $('#search').val();
        if($.trim(search.length) == 0)
        {
          $('#search_results').html('');
        }

        else{
          $.ajax({
          type: 'POST',
          url: '/search/',
          data: {
            'search' : search,
            'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val()
          },
          success: searchSuccess,
          dataType: 'html',

        });
        }

    });
  });




function searchSuccess(data, textStatus, jqXHR)
{
  $('#search_results').html(data);
}
