const listView = document.querySelector('.ListView');
const gridView = document.querySelector('.GridView');

const toogleDiv = document.querySelector('.toogle-products');
const productListDiv = document.querySelectorAll('.productList-flex');
const productsList = document.querySelectorAll('.productsList');
const freeDeliver = document.querySelectorAll('.free-deliver');
const productDescription = document.querySelectorAll('.product-description-list-page > div:first-child');
const productprice = document.querySelectorAll('.product-price-list-page');
const descList = document.querySelectorAll('.descriptionList');
const wrapImg = document.querySelectorAll('.img-wrap');
const starstDiv = document.querySelectorAll('.stars-div');


function addClasses(){
    listView.classList.remove('active');
    gridView.classList.add('active');
    // toogleDiv.classList.add('d-flex', 'flex-wrap', 'justify-content-between');
    toogleDiv.style.display = 'grid';
    toogleDiv.style.gridTemplateColumns = 'repeat(3, 10fr)';
    toogleDiv.style.gridGap = '0.5rem';

    // toogleDiv.classList.add = 'flex-wrap';
    // toogleDiv.classList.add = 'justify-content-between';

    productsList.forEach(element => {
        element.querySelector('.product-bar').classList.add('fix-to-box');
        // element.style.width = '33%';
    });

    productListDiv.forEach(element => {
        element.style.display = 'flex'
        element.style.flexDirection = 'column';
        element.style.height = '35rem';
        // element.style.width = '20rem';
        element.style.alignItems = 'center';
        element.style.justifyContent = 'center';
    });

    freeDeliver.forEach(element => {
        element.classList.remove('d-flex');
        element.style.display = 'none';
    });
    productDescription.forEach(element => {
        element.style.alignItems = 'center';
        // element.parentNode.style.width = '20rem';
        element.parentNode.style.height = 'auto';
        element.parentNode.style.marginBottom = '1rem'
        element.parentNode.style.marginTop = '2rem'
    });

    productprice.forEach(element => {
        element.classList.remove('justify-content-center');
        element.style.height = 'auto'
    })

    descList.forEach(element => {
        element.style.display = "none"
    });

    wrapImg.forEach(element => {
        element.style.marginLeft = '0';
        element.style.height = '13rem';
        element.parentNode.style.width = '100%';
        element.parentNode.style.justifyContent = 'center';

    });
}

function removeClasses(){
    listView.classList.add('active');
    gridView.classList.remove('active');

    toogleDiv.style.display = 'block';

    productsList.forEach(element => {
        element.querySelector('.product-bar').classList.remove('fix-to-box');
    });

    productListDiv.forEach(element => {
        element.style.display = 'grid';
        element.style.height = 'fit-content';
        element.style.gridTemplateColumns = '4fr 10fr 3fr'
        element.style.alignItems = 'center';
        element.style.justifyContent = 'center';
    });

    freeDeliver.forEach(element => {
        element.classList.add('d-flex');
    });

    productDescription.forEach(element => {
        element.style.alignItems = 'flex-start';
        element.parentNode.style.height = '100%';
        element.parentNode.style.marginBottom = '0rem'
        element.parentNode.style.marginTop = '0rem';
    });

    productprice.forEach(element => {
        element.classList.add('justify-content-center');
        element.style.height = '100%'
    })

    descList.forEach(element => {
        element.style.display = "block";
    });

    wrapImg.forEach(element => {
        element.style.marginLeft = '0';
        element.style.height = '100%';
        element.parentNode.style.width = 'auto';
        element.parentNode.style.justifyContent = 'flex-start';

    });

}

listView.addEventListener('click', removeClasses);
gridView.addEventListener('click', addClasses);