let getProductDataBars = document.querySelectorAll('.select-section');
const productDataBlock = document.querySelectorAll('.data-blocks');
const dataBlocks = document.querySelectorAll('.data-blocks button');

dataBlocks.forEach(element => {
    element.classList.add('font-point-seven-rem')
    element.classList.add('px-2')
});

const URL = window.location.href;
let newProduct;

String.prototype.capitalize = function() {
    return this.charAt(0).toUpperCase() + this.slice(1);
};

const createElements = (element) => {
    const newDiv = document.createElement('div');
    const newP = document.createElement('p');
    const newSpan = document.createElement('span');

    newDiv.className = 'd-flex';
    newP.className = 'text-left font-light-grey';
    let text = element.split('_').join(' ').capitalize();
    if (text === 'P c i e'){
        text = text.replaceAll(' ', '')
    }
    newP.innerText = `${text}: `;
    newP.style.marginBottom = '0'
    newSpan.className = 'px-2 pt-1 text-left product-spec-span';

    newSpan.innerText = newProduct[element.toLowerCase()];

    newP.appendChild(newSpan);
    newDiv.appendChild(newP);

    return newDiv

}

if(productDataBlock.length <= 2 && productDataBlock.length >= 1 ){

    const urlProduct = '/api/product-dict/';

    fetch(urlProduct, {
        method : 'POST',
        headers : {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrftoken,
        },
        body : JSON.stringify({
            'productId' : URL.split('/').slice(-2, -1) + ''
        })})
        .then(response => {
            return response.json()
        })
        .then((data) =>{

            newProduct = JSON.parse(data);

            try{
                const productSpecList = productDict[newProduct.cattegory];
                if (productSpecList !== undefined){
                    const newSpecDiv = document.createElement('div');
                    newSpecDiv.className = 'pt-3 data-blocks';

                    productSpecList.forEach(element =>{

                        newSpecDiv.appendChild(createElements(`${element}`));
                    });
                    getProductDataBars[getProductDataBars.length-1].appendChild(newSpecDiv)
                }

            } catch (e) {
                console.log('Oops, something went wrong', e)
            }
        })
}

const productDict = {
    'PC': ['Ram', 'processor', 'socket' , 'system', 'graph' , 'motherboard_chipset'],
    'TV': ['refresh_rate', 'diagonal', 'curved', 'smart_tv', 'resolution', 'matrix_type'],
    'Phones': ['cpu_clock', 'system', 'memory', 'ram', 'memory_card', 'screen_diagonal'],
    'Laptops': ['p_c_i_e', 'ram_freq', 'ram', 'resolution', 'screen_diagonal', 'system'],
    'Monitors': ['diagonal', 'matrix_type', 'curved', 'refresh_rate', 'resolution'],
    'SSD': ['producent_code', 'ean', 'capacity', 'format', 'reading_speed', 'writing_speed', 'life_time'],
    'Ram': ['producent_code', 'ean', 'capacity', 'frequency', 'modules_number', 'delay']
}


