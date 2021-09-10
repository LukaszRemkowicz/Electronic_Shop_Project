const questionForm = document.querySelector('.question-form')

questionForm.addEventListener('submit', ()=>{
    let productId = event.target.dataset.productid
    let content = document.querySelector('#question-form').value

    event.preventDefault()

    const url = '/api/create-question/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrftoken,
        },
        body : JSON.stringify({
            'productId': productId,
            'content' : content,
        })
    })
    
    .then(response =>{
        return response.json()
    })

    .then(data =>{
        data = JSON.parse(data);
        
        
        window.location.reload()
    })
})