function blogParallax(){
    var scrolled = $(window).scrollTop();
    console.log(scrolled)
    $('.bg-blog').css('top', (0-(scrolled * 0.3)) + 'px');
}

$(document).ready(function(){
    $(window).scroll(function(){
        blogParallax();
    });
})  