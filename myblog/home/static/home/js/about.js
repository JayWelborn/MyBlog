function parallax(){
    var scrolled = $(window).scrollTop();
    console.log(scrolled)
    $('.bg').css('top', (0-(scrolled * 1.6)) + 'px');
}

$(document).ready(function(){
    $(window).scroll(function(){
        parallax();
    });
})
