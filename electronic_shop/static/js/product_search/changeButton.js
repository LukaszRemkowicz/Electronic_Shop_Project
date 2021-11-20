const addBtns = document.querySelectorAll('.add-to-cart');

function createNotAvaiableBtn(){
    let div = document.createElement('div')
    div.classList.add('btn-light', 'ml-2', 'p-2', 'pt-2', 'text-center', 'product-not-avaiable');
    div.innerText = 'Product is not avaiable';

    return div
}

function changeButton(pieces, element){
    if(+pieces <= 0){
        element.classList.add('d-none');
        element.parentElement.append(createNotAvaiableBtn);
    } else{
        document.querySelector('.product-not-avaiable').classList.add('d-none');
        element.classList.add('d-block');
    }
}

addBtns.forEach(element => {
    element.addEventListener('click', ()=> {
        changeButton()
    })
})