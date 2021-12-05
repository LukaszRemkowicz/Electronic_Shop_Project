const productId = document.querySelector('.sold-left .update-cart')

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
        createSoldOutButton(productId, 'No enough on stock');
        productId.classList.remove('add-to-cart', 'update-cart');
        productId.removeAttribute('data-action');
        const clone = productId.cloneNode(true);

        productId.parentNode.replaceChild(clone, productId);
    }
})