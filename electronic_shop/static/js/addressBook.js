const book = document.querySelectorAll('.book-box');

const formAddress = document.getElementById('formName');
const formCity = document.getElementById('formCity');
const formState = document.getElementById('formState');
const zipCode = document.getElementById('formZipCode');
const formStreetName = document.getElementById('formStreetName');

const addressBookDiv = document.querySelector('.book-addresses');

let activeButton = '';


book.forEach(element =>{
    element.addEventListener('click', () =>{
        formAddress.value = element.querySelector('.book-address').innerHTML
        formCity.value = element.querySelector('.book-city').innerHTML
        zipCode.value = element.querySelector('.book-postcode').innerHTML
        formState.value = element.querySelector('.book-state').innerHTML
        formStreetName.value = element.querySelector('.book-street').innerHTML
        
        if(activeButton != element && activeButton !== ''){
            activeButton.style.borderColor = '#cccccc'
        }
        
        activeButton = element
        
        if (activeButton !== ''){
            activeButton.style.borderColor = '#ff503c';
        }
})})





