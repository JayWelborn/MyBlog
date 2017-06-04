function parallax(){
    var scrolled = $(window).scrollTop();
    console.log(scrolled)
    $('.bg').css('top', (0-(scrolled * 0.4)) + 'px');
}

$(document).ready(function(){
    $(window).scroll(function(){
        parallax();
    });
})
