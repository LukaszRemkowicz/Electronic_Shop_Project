const reviewForm = document.querySelector('.review-form')


function acceptReview(event){

    let content = document.querySelector('#opinion-form').value;
    let productId = document.querySelector('[data-productId]').dataset.productid
    let orderNumber = document.querySelector('.order-number-review').value

    event.preventDefault();

    const url = '/api/create-review/'
    
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrftoken,
        },
        body : JSON.stringify({
            'content' : content,
            'productId' : productId,
            'orderNumber': orderNumber,
            'stars' : numClicked,
        })
    })

    .then(response =>{
        return response.json()
    })

    .then(data =>{
        data = JSON.parse(data)
        console.log(data)
    })

}


reviewForm.addEventListener('submit', acceptReview);

