const getImages = document.querySelectorAll('.mini-images-section > img');
const mainPhoto = document.querySelector('.main-img-div > img')


getImages.forEach( element => {
    element.addEventListener('click', (e) => {
        const imageName = e.target.dataset.imageName;
        const URL = '/api/product-dict/';

        fetch(URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken' : csrftoken,
            },
            body: JSON.stringify({
                'productId': productId,
            })
        })
        .then(response => {
            return response.json();
        })
        .then(data => {
            const newImage = JSON.parse(data)[`${imageName}`];
            let urlList = element.src.split('/')
            let newUrl = urlList.slice(0, urlList.length-2);
            newUrl.push(newImage);
            newUrl = newUrl.join('/');
            mainPhoto.src = newUrl;
            console.log(element);
            element.classList.remove('mini-img');
            element.classList.add('active-product-content');

            getImages.forEach( el => {
                if(el !== element){
                    el.classList.add('mini-img')
                }
            })
        })
    })
})