
$(document).on('click','#upvotes',function(event){
    event.preventDefault();
    var catid;
    catid = this.value;
        jQuery.get('/newspost/upvote_p/', {post_id: catid}, function(data){
            console.log(document.getElementById('upvote_count'));
            document.getElementById('upvote_count').innerHTML=data;
               // $('#upvote_count').html(data);
            document.getElementById('upvotes').style.visibility ='hidden';
           });


});

$(document).on('click','.votearrow',function(e){
    e.preventDefault();
    var cid;
     cid = this.value;
        jQuery.get('/newspost/upvote_c/', {comment_id: cid}, function(data){
            document.getElementById('comment-count'+cid).innerHTML=data;
           });


});



$(document).on('click','.link',function(event){
        event.preventDefault();
    var rid;
    rid=this;
   $('links'+rid['id']).style.display='block';
   // $(this).css('visibility', 'hidden');

});


 $(document).on('submit','.form_comment',function(e1) { // catch the form's submit event
    e1.preventDefault();
            var frm=jQuery(this);
            var token = jQuery('input[name="csrfmiddlewaretoken"]').prop('value');
            jQuery.ajax({ // create an AJAX call...
                data: {'data1':frm.serialize(),'csrfmiddlewaretoken': token ,'id':frm.attr('data_commentid')}, // get the form data
                type: frm.attr('method'), // GET or POST
                url: frm.attr('action'), // the file to call
            success : function(result) {
                var child = result['child_id'];
               $('links'+frm.attr('data_commentid')).style.display='none';
            jQuery('#table'+frm.attr('data_commentid')).after('<tr  class="athing comtr"id=table'+child+'></tr>');

            document.getElementById('table'+child).innerHTML = result['html']
        },
            error: function(result){
            }
            });
            return false;
        });
 $(document).on('submit','.post_comment',function(e1) { // catch the form's submit event
    e1.preventDefault();
            var frm=jQuery(this);

            var token = jQuery('input[name="csrfmiddlewaretoken"]').prop('value');
            jQuery.ajax({ // create an AJAX call...
                data: {'data1':frm.serialize(),'csrfmiddlewaretoken': token ,'id':frm.attr('data_id')}, // get the form data
                type: frm.attr('method'), // GET or POST
                url: frm.attr('action'), // the file to call
            success : function(result) {
                var table=document.getElementsByClassName('athing comtr ');
                if (table.length!=0)
                {
                var list= document.getElementsByClassName('athing comtr ');
                var t=list[list.length-1]
                var comment = result['comment_id']
            jQuery('#'+t['id']).after('<tr  class="athing comtr"id=table'+comment+'></tr>');
            document.getElementById('table'+comment).innerHTML = result['html']

                        jQuery('html, body').animate({
                scrollTop: (jQuery('#table'+comment).offset().top)
            },500);
                    }
            else{

                var comment = result['comment_id']
            jQuery('.comment-tree').append('<tr  class="athing comtr"id=table'+comment+'></tr>');
            document.getElementById('table'+comment).innerHTML = result['html']

            }
        },
            error: function(result){
            }
            });
            return false;
        });
