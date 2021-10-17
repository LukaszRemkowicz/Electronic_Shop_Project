let getProductDataBars = document.querySelectorAll('.data-blocks')

const URL = window.location.href;
let newProduct = 0

String.prototype.capitalize = function() {
    return this.charAt(0).toUpperCase() + this.slice(1);
}

const createElements = (element) => {
    const newDiv = document.createElement('div');
    const newP = document.createElement('p');
    const newSecondP = document.createElement('p');

    newDiv.className = 'd-flex';
    newP.className = 'px-5 pt-1 text-left';
    newP.innerText = element.split('_').join(' ').capitalize();
    newSecondP.className = 'px-5 pt-1 text-left font-light-grey';

    newSecondP.innerText = newProduct[element.toLowerCase()];

    newDiv.appendChild(newP);
    newDiv.appendChild(newSecondP);

    return newDiv

}

if(getProductDataBars.length <= 2 && getProductDataBars.length >= 1 ){

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
                console.log(productDict[newProduct.cattegory])
                const productSpecList = productDict[newProduct.cattegory];
                productSpecList.forEach(element =>{
                    console.log(element)
                    getProductDataBars[getProductDataBars.length-1].appendChild(createElements(`${element}`));
                })
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


