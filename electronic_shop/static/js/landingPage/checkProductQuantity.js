const productId = document.querySelector('.sold-left .update-cart');
let piecesLeft = document.querySelector('.sold-left .piecesLeft');

function checkQuantity(){
    setTimeout(() => {
        fetch(`/api/product-quantity/${+productId.dataset.product}`, {
            method: "GET",
            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            if(data['order_quantity'] >= data['product_stock']){
                console.log('datkaaaaaaaa');

                createSoldOutButton(productId, 'Not in stock');
                productId.classList.remove('add-to-cart', 'update-cart');
                productId.removeAttribute('data-action');
                const clone = productId.cloneNode(true);

                productId.parentNode.replaceChild(clone, productId);
            };
            piecesLeft.innerHTML = `${data['product_stock'] - data['order_quantity']} pieces left`

        })
    }, 500);

};

if(productId){
    checkQuantity();
    productId.addEventListener('click', checkQuantity);
}
