var jumboHeight = $('.jumbotron').outerHeight();
function parallax(){
    var scrolled = $(window).scrollTop();
    $('.bg').css('height', (jumboHeight-(scrolled/2)) + 'px');
}

$(window).scroll(function(e){
    parallax();
});