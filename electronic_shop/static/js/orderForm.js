const btnForm = document.querySelector('.addres-form')
const btnSubmit = document.querySelector('.form-submit')
const payment = document.querySelector('.payment')
const paymentBtn = document.querySelector('.payment-btn')
const paymentMethods = document.querySelectorAll('.payment-images')


let status = 0
let activeButtonPayment = ''

const paymentMethod = []

if (document.querySelector('.ship_info_a') != null){
    document.querySelector('.ship_info_a').addEventListener('click', () =>{
        if (orderSummary === 0){
            console.log('im here')
            document.querySelector('.submit-button').style.backgroundColor = '#757575'
        }
    })
}


function getNameOfPayment(event){
    const name = this.dataset.name
    paymentMethods.length = 0
    paymentMethod.push(name)

    if(activeButtonPayment != this && activeButtonPayment !== ''){
        activeButtonPayment.style.borderColor = '#cccccc'
    }

    activeButtonPayment = this

    if (activeButtonPayment !== ''){
        activeButtonPayment.style.borderColor = '#ff503c';
    }

}

paymentMethods.forEach(element =>{
    element.addEventListener('click', getNameOfPayment)
})


const addressForm = document.querySelector('.addres-form')

function acceptForm(event){
    event.preventDefault();
    const customerName = event.target[name='formName'].value.trim();
    const customerCity = event.target[name='formCity'].value.trim();
    const customerState = event.target[name='formState'].value.trim();
    const customerZipcode = event.target[name='formZipCode'].value.trim();
    const customerStreet = event.target[name='formStreetName'].value.trim();
    let customerEmail = event.target[name='formEmail'];

    // form Validation

    console.log(customerEmail)

    let error = 0

    if (customerName.split(' ').length === 1){
        setErrorFor(event.target[name='formName'], 'Not valid Name and Surname')
        error = 1
    }else if (customerName === ''){
        setErrorFor(event.target[name='formName'], 'Username cannot be blank');
        error = 1;
    }else{
        setSuccessFor(event.target[name='formName'])
    }

    if (customerCity === '' ){
        setErrorFor(event.target[name='formCity'], 'City cannot be blank');
        error = 1;
    }else{
        setSuccessFor(event.target[name='formCity'])
    }

    if (customerState === '' ){
        setErrorFor(event.target[name='formState'], 'State cannot be blank');
        error = 1
    }else{
        setSuccessFor(event.target[name='formState'])
    }

    if (customerZipcode === ''){
        setErrorFor(event.target[name='formZipCode'], 'Zipcode cannot be blank');
        error = 1
    }else{
        setSuccessFor(event.target[name='formZipCode'])
    }

    if (customerStreet === ''){
        setErrorFor(event.target[name='formStreetName'], 'Street cannot be blank');
        error = 1
    }else{
        setSuccessFor(event.target[name='formStreetName'])
    }

    if (user === 'AnonymousUser' || customerEmail.placeholder.trim() === 'Email..'){
        customerEmail = customerEmail.value
    }else{
        customerEmail = customerEmail.placeholder.trim()
    }

    if (!isEmail(customerEmail)){
        setErrorFor(event.target[name='formEmail'], 'Not a valid email');
        error = 1
    }else if (customerEmail === ''){
        setErrorFor(event.target[name='formEmail'], 'Email cannot be blank');
        error = 1
    }else{
        setSuccessFor(event.target[name='formEmail'])
    }



    // Fetch api to View point

    const url = '/api/order-completed/'

    if (error === 0){
        fetch(url, {
            method : 'POST',
            headers : {
                'Content-Type': 'application/json',
                'X-CSRFToken' : csrftoken,
            },
            body : JSON.stringify({
                'price': orderSummary,
                'payment': paymentMethod[0],
                'customerName' : customerName,
                'customerCity' : customerCity,
                'customerState' : customerState,
                'customerZipcode' : customerZipcode,
                'customerStreet' : customerStreet,
                'customerEmail' : customerEmail,
            })})

            .then(response => {
                // console.log(event);
                return response.json()
            })

            .then((data) =>{
                console.log('data: ', data)
                // location.reload()

                alert('Order sent')

                document.querySelector('.shopping-cart').dataset['totalitems'] = 0

                console.log(user)
                if(user === 'AnonymousUser'){
                    window.location.href = redirectToLandingPage
                }else{
                    window.location.href = redirectToAccountUrl
                }



                cart = {}
                document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
            })
    }

}

if (addressForm != null){
    addressForm.addEventListener('submit', acceptForm)
}


// Error handler

function setErrorFor(name, message){

    const formControl = name.parentElement;
    formControl.classList.remove('success-form');

    if (formControl.querySelector('p') !== null){
        const newP = formControl.querySelector('p');
        newP.classList.add("alert");
        newP.innerHTML = message;
    }

    formControl.classList.add('error-form')

    document.querySelector('#shipping-methods').classList.remove('show')
    document.querySelector('#catch-form').classList.add('show')

}

function setSuccessFor(username){

    const formControl = username.parentElement

    formControl.classList.remove('error-form')
    formControl.classList.add('success-form');

}


function isEmail(email) {
	return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
}


