var updateCart = document.querySelectorAll('.update-cart');
var addButton = document.querySelector('.basket');
let getProductAmount = document.querySelector('.amount');

cartTotal = 0;

let selected;

if (getProductAmount != null){
    getProductAmount.addEventListener('change', function(){
        selected = this.value
    })
}

function changeAddButton(pieces, element){
    console.log('changeAddButton', pieces);

    // #TODO porownac wartosc koszyka z pieces produktu. Sprawdzic porownywanie koszyka usera
    // annonymous z pieces po stronie template
    if(+pieces <= 0){
        try{
            element.classList.remove('d-block');
            element.classList.add('d-none');
            parent = element.parentElement;

            parent.querySelector('.product-not-avaiable').classList.add('d-block');
            parent.querySelector('.product-not-avaiable').classList.remove('d-none')

        }catch (e){
            console.log(e);
        }

    } else{
        try{
            element.classList.remove('d-none');
            element.classList.add('d-block');
            parent = element.parentElement;
            parent.querySelector('.product-not-avaiable').classList.add('d-none');
            parent.querySelector('.product-not-avaiable').classList.remove('d-block')
        }catch (e){
            console.log(e);
        }

    }

}

function updateCartFunc(element, action){

    if (action !== 'delete' && document.querySelector('.quantity-div') !== null){

        let getDiv = document.querySelector(`[data-product="${element.dataset['product']}"]`).parentElement.parentElement

        let quantity = getDiv.querySelector('.quantity-div').querySelector('.border')
        let totalItem = getDiv.querySelector('.price-div').querySelector('.box-shadow').querySelector('.getTotal')

        quantity.innerHTML = JSON.parse(cartTotal).items
        totalItem.innerHTML = JSON.parse(cartTotal).summaryItem.toFixed(2)

    }


    let totalBasket = document.querySelector('.price-total');
    const totalItems = document.getElementById('shopping-cart');
    const subtalItems = document.querySelector('.subtotalItems');
    let navbarPrice = document.querySelector('.price-navbar')

    if (totalBasket !== null){
        totalBasket.innerHTML = `${JSON.parse(cartTotal).subtotal} $`;
        subtalItems.innerHTML = JSON.parse(cartTotal).totalItems;

    }

    navbarPrice.innerHTML = `${(+JSON.parse(cartTotal).subtotal).toFixed(2)} $`;
    totalItems.dataset['totalitems'] = JSON.parse(cartTotal).totalItems;
}


updateCart.forEach(element => {

    element.addEventListener('click', function(){

        const productId = this.dataset.product
        const action = this.dataset.action

        if (getProductAmount != null){
            getProductAmount = selected ?? 1
        }else{
            getProductAmount= 1
        }

        if (action === 'delete'){
            document.querySelector(`#product-${productId}`).remove()
        }

        if(action != undefined){
            if(user == 'AnonymousUser'){
                console.log('this: ', this)
                addCookieItem(productId, action, this)
            }else{
                updateUserOrder(productId, action, getProductAmount, this);
            }
        }
    })
})


function addCookieItem(productId, action, element){

    if (action === 'add'){

        if (cart['products'] === undefined){
            cart['products'] = {}
        }

        if (cart['products'][productId] === undefined){
            // console.log('cart po dodaniu', cart)
            cart['products'][productId] = {'quantity' : 1};
        }else{

            cart['products'][productId]['quantity'] += 1;

            if (cart['products'][productId]['quantity'] <= 0){
                // console.log('Removed');
                delete cart['products'][productId] ;
            }
        }
    }

    if (action === 'remove'){
        cart['products'][productId]['quantity'] -= 1;
        if (cart !== undefined && Object.keys(cart["products"]).length === 0){
            window.location.reload();
        };
    }

    if (action === 'delete'){
        delete cart['products'][productId];
        if (cart !== undefined && Object.keys(cart["products"]).length === 0){
            window.location.reload();
        }
    }

    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/";

    const url = '/api/order-cart-unauthorised-user/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrftoken,
        },
        body : JSON.stringify({
            'productId' : productId,
        })
    })

    .then((response) =>{
        return response.json()
    })
    .then((data) =>{

        data = JSON.parse(data);
        console.log('dwdwdwdwdwdwdwd', data);

        cartTotal = {
            'items' : 0,
            'summaryItem': 0,
            'subtotal': 0,
            'totalItems': 0,

        };

        if (action !== 'delete' || cart['products'][productId] !== undefined){
            filteredData = data['items'].filter(element => {
                if(element['product'].id === +productId)
                {return element}
            })[0];

            console.log('filteredData: ', filteredData)

            cartTotal.items = filteredData.quantity;
            cartTotal.summaryItem = +filteredData.get_total;
        }

        cartTotal.subtotal = +data['order'].get_cart_total
        cartTotal.totalItems = data['order'].get_cart_items

        // cartTotal = JSON.stringify({
        //     'items' : filteredData.quantity,
        //     'summaryItem': +filteredData.get_total,
        //     'subtotal': +data['order'].get_cart_total,
        //     'totalItems': data['order'].get_cart_items,

        // });

        cartTotal = JSON.stringify(cartTotal);
        // updateCartFunc(product, action);
        console.log('filteredData', filteredData);
        // data.items.forEach(el => {
        //     changeAddButton(el.product.pieces, element);
        //     updateCartFunc(el, action);
        // })

        changeAddButton(filteredData.product.pieces, element);
        updateCartFunc(filteredData, action);

    })
}

function updateUserOrder(productId, action, getProductAmount, element){

    const url = '/api/update-item/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrftoken,
        },
        body : JSON.stringify({
            'productId' : productId, 'action': action, 'amount': getProductAmount,
        })
    })

    .then((response) =>{
        return response.json();
    })

    .then((data) =>{

        console.log('data.pieces', data.pieces);

        if(JSON.parse(data).totalItems == 0){
            window.location.href = redirectToAccountUrl
        }
        cartTotal = data;

        if(document.querySelector('.add-to-cart') != null){
            changeAddButton(JSON.parse(data).pieces, element);
            const getPieces = document.querySelector('.pieces');
            if(getPieces){
                getPieces.innerText = `Left: ${+JSON.parse(data).pieces} pcs`

                let getProductAmount = document.querySelector('.amount')
                getProductAmount.innerHTML = ''
            }

            if (+JSON.parse(data).pieces === 0){
                try{
                    const newOption = document.createElement('option');
                    newOption.setAttribute('value', 0);
                    newOption.innerText = 0;
                    getProductAmount = document.querySelector('.amount')
                    getProductAmount.append(newOption);

                } catch (e){
                    console.log(e)
                }
            }

            if(getPieces){
                for (let num = 1; num <= +JSON.parse(data).pieces; num++){
                    const newOption = document.createElement('option')
                    newOption.setAttribute('value', num)
                    newOption.innerText = num;
                    getProductAmount = document.querySelector('.amount')
                    getProductAmount.append(newOption)
                }
            }
        }

        /** If there is "Buy now" button on website, redirect to cart page */
        updateCartFunc(element, action);
        const buyNow = document.querySelector('.buyNow');
        if (buyNow && element == buyNow){
            window.location.href = '/cart/'
        };

        /** Check if user is on summary cart page. If true then control +/- icons */
        const cartSummary = document.querySelectorAll('.quantity-div');

        cartSummary.forEach(element =>{

            if(JSON.parse(data).pieces <= 0){
                element.querySelector('.cartPiecesPlus').classList.add('d-none');
            } else if(JSON.parse(data).pieces != 0 && JSON.parse(data).items != 0){
                element.querySelector('.cartPiecesPlus').classList.remove('d-none');
                element.querySelector('.cartPiecesMinus').classList.remove('d-none');
            } else if(JSON.parse(data).items <= 0){
                element.querySelector('.cartPiecesMinus').classList.add('d-none');
                window.location.reload();
            }
        })
    })
}

