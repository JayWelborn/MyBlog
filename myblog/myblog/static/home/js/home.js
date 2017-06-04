var jumboHeight = $('.jumbotron').outerHeight() + 50;
function parallax(){
    var scrolled = $(window).scrollTop();
    $('.bg').css('height', (jumboHeight-scrolled) + 'px');
}

$(document).ready(function(){
    $(window).scroll(function(){
        parallax();
    });
})
