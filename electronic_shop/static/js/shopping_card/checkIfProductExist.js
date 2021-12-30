/** Check if products from cart cookie exists. If not, delete id from object */

let productsList = JSON.parse(getCookie('cart')).products

for (let [productId, ] of Object.entries(productsList)){
    url = `/api/product/${productId}`
    fetch(url, {
        method: "GET",
        headers : {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrftoken,
        }
    })
    .then(response => response.json())
    .then(data => {
        if(!data.ean){
            delete cart['products'][productId]
        }
    })
}
