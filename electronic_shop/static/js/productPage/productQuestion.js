const questionForm = document.querySelector('.question-form');
const changePic = document.querySelectorAll('.profileImage');


questionForm.addEventListener('submit', (e)=>{
    let productId = event.target.dataset.productid
    let content = document.querySelector('#question-form').value
    let questionName = document.querySelector('.question-form .form-group input').value

    e.preventDefault()

    console.log(questionName);

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
            'name': questionName
        })
    })

    .then(response =>{
        return response.json()
    })

    .then(data =>{
        data = JSON.parse(data);

        window.location.reload();
        window.scrollTo(0, 0);
    })
})

/** Add "pic" to comment. */
changePic.forEach( element => {
    const name = element.dataset.ownercomment.split(' ');
    let result;

    console.log('name', name);

    if (name[0] != ''){
        if (name.lenght >= 2){
            result = `${name[0][0]}${name[1][0]}`
        } else{
            result = `${name[0][0]}${name[0][1]}`
        }
    } else{
        result = 'US'
    }
    

    element.innerHTML = result
})