// $('.add-to-cart').on('click', function () {
//     var button = $(this)
//     var cart = $('#shopping-cart');
//     var carTotal = cart.attr('data-totalitems')
//     var newCartTotal = parseInt(carTotal) + 1;
//     var imgtodrag = $(".main-pic");
//     cart.attr('data-totalitems', newCartTotal);
//     if (imgtodrag) {
//         var imgclone = imgtodrag.clone()
//             .offset({
//             top: imgtodrag.offset().top,
//             left: imgtodrag.offset().left
//         })
//             .css({
//             'opacity': '0.5',
//                 'position': 'absolute',
//                 'height': '150px',
//                 'width': '150px',
//                 'z-index': '100'
//         })
//             .appendTo($('body'))
//             .animate({
//             'top': cart.offset().top + 10,
//                 'left': cart.offset().left + 10,
//                 'width': 75,
//                 'height': 75
//         }, 1000, 'easeInOutExpo');

//         setTimeout(function () {
//             cart.effect("shake", {
//                 times: 2
//             }, 200);
//         }, 1500);

//         imgclone.animate({
//             'width': 0,
//                 'height': 0
//         }, function () {
//             $(this).detach()
//         });

//     }


// });

function getOffset(element){
    /** Helper fuinction to determinate top and left offset */

    if (!element.getClientRects().length){
        return { top: 0, left: 0 };
    }

    let rect = element.getBoundingClientRect();
    let win = element.ownerDocument.defaultView;
    return ({
        top: rect.top + win.pageYOffset,
        left: rect.left + win.pageXOffset
    });
}

let addToCart = document.querySelectorAll('.add-to-cart')
addToCart = [... addToCart]

addToCart.forEach(element =>{
    element.addEventListener('click', function () {

        /** Slow down animation if user is at the bottom of the page */
        const indexOf = (addToCart.indexOf(element)%addToCart.length) *300

        const imgtodrag = element.parentElement.parentElement.parentElement.parentElement.querySelector('.main-pic');
        const imgtodragTop = getOffset(imgtodrag).top
        const imgtodragLeft = getOffset(imgtodrag).left

        const basket = document.querySelector('#shopping-cart');
        const topBasket = Math.round(basket.getBoundingClientRect().top);
        const leftBasket = Math.round(basket.getBoundingClientRect().left);

        if (imgtodrag) {

            const imgclone = imgtodrag.cloneNode(true);
            imgclone.style.cssText = `opacity: 0.5;
                                    position: absolute;
                                    height: 150px;
                                    width: 150px;
                                    z-index: 100;`

            document.querySelector('body').appendChild(imgclone);

            imgclone.animate([
                        {
                            'top': `${imgtodragTop}px`,
                            'left': `${imgtodragLeft}px`
                        },
                        {
                            top: `${topBasket + 10}px`,
                            left: `${leftBasket + 20}px`,
                            width: '55px',
                            height: '55px',
                            easing: 'ease-in',
                            opacity: 0.7,
                        },
                    ], {duration: 600+indexOf, fill: 'forwards'} )

            setTimeout(function () {

                // Shake animation
                imgclone.animate([
                    { transform: `translate(2px, 1px) rotate(0deg)`,  opacity: 0.7} ,
                    { transform: `translate(-1px, -2px) rotate(-5deg)`,  opacity: 0.7},
                    { transform: `translate(-3px, 0px) rotate(3deg)`, opacity: 0.7},
                    { transform: `translate(0px, 2px) rotate(0deg)`, opacity: 0.7},
                    { transform: `translate(1px, -1px) rotate(3deg)`, opacity: 0.6},
                    { transform: `translate(-1px, 2px) rotate(-5deg)`, opacity: 0.5},
                    { transform: `translate(-3px, 1px) rotate(0deg)`, opacity: 0.4},
                    { transform: `translate(2px, 1px) rotate(-5deg)`, opacity: 0.3},
                    { transform: `translate(-1px, -1px) rotate(3deg)`, opacity: 0.2},
                    { transform: `translate(2px, 2px) rotate(0deg)`, opacity: 0.1},
                    { transform: `translate(1px, -2px) rotate(-5deg)`, opacity: 0},
                ], {duration:900, fill: 'forwards'});

            }, 700);

            setTimeout(() => {
                imgclone.animate([
                    {
                        'width': 0,
                        'height': 0,
                    }
                ], {duration: 100, fill: 'forwards'});

                document.querySelector('body').removeChild(imgclone)
            }, 1700)
        }
    });
})
