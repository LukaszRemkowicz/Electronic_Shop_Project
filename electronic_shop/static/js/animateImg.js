$('.add-to-cart').on('click', function () {
    var button = $(this)
    var cart = $('#shopping-cart');
    var carTotal = cart.attr('data-totalitems')
    var newCartTotal = parseInt(carTotal) + 1;
    var imgtodrag = $(".main-pic");
    cart.attr('data-totalitems', newCartTotal);
    if (imgtodrag) {
        var imgclone = imgtodrag.clone()
            .offset({
            top: imgtodrag.offset().top,
            left: imgtodrag.offset().left
        })
            .css({
            'opacity': '0.5',
                'position': 'absolute',
                'height': '150px',
                'width': '150px',
                'z-index': '100'
        })
            .appendTo($('body'))
            .animate({
            'top': cart.offset().top + 10,
                'left': cart.offset().left + 10,
                'width': 75,
                'height': 75
        }, 1000, 'easeInOutExpo');

        setTimeout(function () {
            cart.effect("shake", {
                times: 2
            }, 200);
        }, 1500);

        imgclone.animate({
            'width': 0,
                'height': 0
        }, function () {
            $(this).detach()
        });

    }


});