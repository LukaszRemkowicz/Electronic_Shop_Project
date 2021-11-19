const listProducts = document.querySelector('#products .row');
const gridView = document.querySelector('.grid-view');
const listView = document.querySelector('.list-view');
const productRow = document.querySelectorAll('.product-rows');
const cardBody = document.querySelectorAll('.card .card-body');
const descriptionBody = document.querySelectorAll('.card-body-description');
let toogleButtons = document.querySelectorAll('.toogle-view');
const notDataBlock = document.querySelectorAll('.not-data-block');
const productStars = document.querySelectorAll('.product');
const buyListView = document.querySelectorAll('.buy-list-view');

let productDesc;
let descGrid;


function changeVisibility(element, display){
    if(element.length >=1){
        element.forEach(element => {
            element.style.display = display;
        });
    };

}

function checkParams(){
    let urlParams = new URLSearchParams(window.location.search);
    if(urlParams.get('grid') != null && urlParams.get('grid') === 'true'){
        add();
    } else {
        remove()
    }
};

checkParams()

/** Change classes on elements if Grid view is enabled */

function add(){
    listView.classList.remove('font-red');
    gridView.classList.add('font-red');

    changeUrls('grid', 'true');

    productDesc = document.querySelectorAll('.product-description');
    changeVisibility(productDesc, 'none')

    descGrid = document.querySelectorAll('.description-grid');
    changeVisibility(descGrid, 'block')

    listProducts.style.display = 'flex';
    productRow.forEach(element => {
        const getCard = element.querySelector('.card')
        element.style.maxWidth = '33.33%';
        getCard.style.flexDirection = 'column';
        getCard.querySelector('.card-img-top').style.width = "100%"
    });

    cardBody.forEach(element => {
        element.style.display = 'block';
    });

    descriptionBody.forEach(element => {
        element.style.width = 'auto'
    });

    notDataBlock.forEach(element => {
        element.classList.remove('pt-3');
        element.classList.add('pt-5');
        element.querySelectorAll('p').forEach(element => {
            element.classList.add('pl-5')
        })
    });

    productStars.forEach(element => {

        element.classList.remove('mt-3', 'pl-5');
    });

    productDesc.forEach(element => {

        element.classList.remove('pl-5');
        element.style.textAlign = 'center'
    });

    buyListView.forEach(element => {

        element.classList.add('justify-content-between');
        element.classList.remove('flex', 'flex-column', 'justify-content-center');
        element.querySelector('div:nth-child(1)').classList.remove('pb-5')
    })

    /** change price and heart divs */
    let catchStarsDiv = document.querySelectorAll('.buy-list-view .position-relative');
    catchStarsDiv.forEach(element =>{

        element.classList.remove('w-100');
        element.style.left = '3rem';
        element.style.bottom = '1rem';
    })

}

/** Change classes on elements if List view is enabled.*/

function remove(){

    listView.classList.add('font-red');
    gridView.classList.remove('font-red');

    changeUrls('grid', 'false');

    productDesc = document.querySelectorAll('.product-description');
    changeVisibility(productDesc, 'block');

    descGrid = document.querySelectorAll('.description-grid');
    changeVisibility(descGrid, 'none')

    listProducts.style.display = 'block';
    productRow.forEach(element => {
        const getCard = element.querySelector('.card')
        element.style.maxWidth = '100%';
        getCard.style.flexDirection = 'row';
        getCard.querySelector('.card-img-top').style.width = "30%";
        getCard.querySelector('.card-img-top').style.height = "13rem";
        getCard.querySelector('.card-img-top').style.padding = "1rem";
        getCard.querySelector('.card-img-top').style.alignSelf = "center";

    });
    cardBody.forEach(element => {
        element.style.display = 'flex';
        element.style.justifyContent = 'space-between';
    });

    descriptionBody.forEach(element => {
        element.style.width = '75%'
    });

    notDataBlock.forEach(element => {
        element.classList.remove('pt-5');
        element.classList.add('pt-3');
        element.querySelectorAll('p').forEach(element => {
            element.classList.remove('pl-5')
        })
    });

    productStars.forEach(element => {
        element.classList.add('mt-3', 'pl-5');
    });

    productDesc.forEach(element => {
        element.classList.add('pl-5');
        element.style.textAlign = 'left'
    });

    buyListView.forEach(element => {
        element.classList.remove('justify-content-between');
        element.classList.add('flex', 'flex-column', 'justify-content-center');

        element.querySelector('div:nth-child(1)').classList.add('pb-5')

    })

}


gridView.addEventListener('click', () => {
    add()
});

listView.addEventListener('click', () => {
    remove()
});