
window.onload = function(){
  var paginationPage = parseInt(jQuery('.cdp').attr('actpage'), 10);
  jQuery('.cdp_i').on('click', function(){
    var go = jQuery(this).attr('href').replace('#!', '');

    if (go === '+1') {
      paginationPage++;
    } else if (go === '-1') {
      paginationPage--;
    }else{
      paginationPage = parseInt(go, 10);
    }
    jQuery('.cdp').attr('actpage', paginationPage);
    jQuery.ajax({
          type: 'post',
          url: 'lazy_load_posts/',
          data: {
            'page': paginationPage,
            'csrfmiddlewaretoken': window.CSRF_TOKEN // from index.html
          },
          success: function(data) {
            // if there are still more pages to load,
            // append html to the posts div
            jQuery('.this').html("");
            jQuery('#replace1').html(data.posts_html);
          },
          error: function(xhr, status, error) {
            // shit happens friends!
          }
        });
  });
};



$(document).on('click','.votearrow1',function(event){
    event.preventDefault();
    var catid;
    catid = this.value;
        jQuery.get('/newspost/upvote_p/', {post_id: catid}, function(data){
            document.getElementById('upvote_count'+catid).innerHTML=data;
               // $('#upvote_count').html(data);
            document.getElementById('upvotes'+catid).style.visibility ='hidden';
           });


});







(function(jQuery) {
      jQuery(document).on('click','#lazyLoadLink', function() {
        var link = jQuery(this);
        var page = link.data('page');
        var page=page+1
        jQuery.ajax({
          type: 'post',
          url: 'lazy_load_posts/',
          data: {
            'page': page,
            'csrfmiddlewaretoken': window.CSRF_TOKEN // from index.html
          },
          success: function(data) {
            // if there are still more pages to load,
            // add 1 to the "Load More Posts" link's page data attribute
            // else hide the link
            // append html to the posts div
            jQuery('.this').html("");
            jQuery('#replace1').html(data.posts_html);
          },
          error: function(xhr, status, error) {
            // shit happens friends!
          }
        });
      });
    }(jQuery));
