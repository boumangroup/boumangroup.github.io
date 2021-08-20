/*
* Greedy Navigation
*
* http://codepen.io/lukejacksonn/pen/PwmwWV
*
*/

var $nav = $('#site-nav');
var $btn = $('#site-nav button');
var $vlinks = $('#site-nav .visible-links');
var $hlinks = $('#site-nav .hidden-links');
var $window = $(window);
var $vlinksWidth = $vlinks.width();

function updateNav() {
  if($window.width() > $vlinksWidth + 150) {

    if($vlinks.children().length == 0) {
      // Move hidden links to the visible list.
      $hlinks.children().prependTo($vlinks);
    }
    
    // Hide dropdown button.
    if(!$btn.hasClass('hidden')) {
      $btn.addClass('hidden');
    }
  }
  
  else {
    if($hlinks.children().length == 0) {
      // Move visible links to hidden list.
      $vlinks.children().prependTo($hlinks);
    }
    
    // Show dropdown button.
    if($btn.hasClass('hidden')) {
      $btn.removeClass('hidden');
    }
  }
}

// Window listeners

$(window).resize(function() {
  updateNav();
});

$btn.on('click', function() {
  $hlinks.toggleClass('hidden');
  $(this).toggleClass('close');
});

updateNav();