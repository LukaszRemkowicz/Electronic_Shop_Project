let childProductData = document.querySelectorAll('.spec-product-data')
let specProductData = document.querySelectorAll('.active-product-content')
let productData = {}


childProductData.forEach(element =>{
    element.addEventListener('click', () =>{
        let newArr = [...specProductData].map(element => element.parentNode)
        // let news = newArr.filter(elements => !elements.isEqualNode(element.parentNode));
        const newData = element.innerText.replaceAll('/n', '').trim()
        productData['productClicked'] = {'type' : newData,
                                            'divId': element.parentNode.dataset.name}
        url =  window.location.href.split('/')
        productData['productId'] = url[url.length-2]
        productData['itemsId'] = JSON.parse(productIds)

        // news.forEach(element => {
        //     productData[element.id] = [...element.children].map(elements => elements.innerText)
        // })

        const urlProduct = '/api/get-product/'

        fetch(urlProduct, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken' : csrftoken,
            },
            body : JSON.stringify({
                'productData' : productData,
            })
        })

        .then(response =>{
            return response.json()
        })

        .then(data =>{
            data = JSON.parse(data);
            window.location.href = `/product/${+data}/`;
        })
    })
})



