$(document).ready(function() {

    /* PNGFix For IE6 */
    $(document).pngFix(); 

    /* Loading indicator */
    $(document).ajaxStart($.blockUI).ajaxStop($.unblockUI);
  
    /* Toggle */
    $(".toggle").click(function () {
      $(".toggled").toggle("slow");
    });  

    /* Jump */
    $('a[href*=#container]').click(function() {
      if (location.pathname.replace(/^\//,") == this.pathname.replace(/^\//,")
      && location.hostname == this.hostname) {
      var $target = $(this.hash);
      $target = $target.length && $target
      || $('[name=' + this.hash.slice(1) +']');
      if ($target.length) {
      var targetOffset = $target.offset().top;
      $('html,body')
      .animate({scrollTop: targetOffset}, 1000);
      return false;
      }}
    });
    
    /* Timeago */
    jQuery("abbr.timeago").timeago();  
   
    
    /* Editable */
    $(".mouseover").editable("/todo/update_text/", { 
      indicator : "<img src='indicator.gif'>",
      tooltip   : "Move mouseover to edit...",
      event     : "mouseover",
      style  : "inherit"
    });
    
    /* Notification */	
    $(".msgadd").bar({
		color 			 : '#FF6600',
		background_color : '#FFFFCC',
		position		 : 'bottom',
		removebutton     : false,
		message			 : 'Your todo has been added!',
		time			 : 4000
	});	
	$(".msgdelete").bar({
		color 			 : '#FF6600',
		background_color : '#FFFFCC',
		position		 : 'bottom',
		removebutton     : false,
		message			 : 'Your todo has been deleted!',
		time			 : 4000
	});	
});
