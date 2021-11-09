const filterParameter = document.querySelector('.product-filter-parameter');
const urlSearchParams = new URLSearchParams(window.location.search);
const params = Object.fromEntries(urlSearchParams.entries());
// const URL = '/api/product-dict/';

const filterParam = document.querySelectorAll('.product-filter-parameters input');

filterParam.forEach(element => {
    element.addEventListener('click', () => {
        const parameters = window.location.href.replace('#', '').split('&');
        let newValue = element.value

        console.log(parameters);
        if (parameters.length >= 2 || window.location.href.includes('filter')){
            let newUrl = window.location.href.replace('#', '').split('?');
            let newUrlTwo = newUrl[1].split('&')


            newUrlTwo.forEach((element, index) => {
                if (element.includes('filter=')){
                    newUrlTwo[index] = `filter=${newValue}`;
                }})

            console.log('newurl', newUrlTwo);
            let urlJoined
            if(newUrlTwo.length >= 2){
                 urlJoined = newUrlTwo.join('&');
            } else {
                urlJoined = newUrlTwo
            }

            console.log('param po joinu ', urlJoined);

            if (!urlJoined.includes('filter')){
                urlJoined = urlJoined + `&filter=${element.value}`;
                urlJoined = newUrl[0] + '?' + urlJoined
            } else {
                urlJoined = newUrl[0] + '?' + urlJoined
            };

            console.log('po joinu', urlJoined);
            window.location.replace(urlJoined)
        } else if(window.location.href.split('?').length >= 2){
            console.log('elif');
            console.log(window.location.href.split('?'));
            window.location.replace(`${url}&filter=${element.value}`)
        } else {
            console.log('else');
            window.location.replace(`${url}?filter=${element.value}`)
        }
    })
})

// filterParameter.addEventListener('change', function(){
//         const parameters = window.location.href.replace('#', '').split('&');
//         console.log(parameters)
//         let newValue = this.value

//         if (parameters.length >= 2){
//             let newUrl = window.location.href.replace('#', '').split('filter=');


//             parameters.forEach((element, index) => {
//                 if (element.includes('filter=')){
//                     parameters[index] = `filter=${newValue}`;
//                 }
//             })

//             let urlJoined = parameters.join('&');

//             if (!urlJoined.includes('filter')){
//                 urlJoined += `&filter=${this.value}`;
//             }

//             console.log('po joinu', urlJoined);
//             window.location.replace(urlJoined)
//         } else{
//             window.location.replace(`${url}&filter=${this.value}`)
//         }
//         // fetch(URL, {
//         //     method: 'POST',
//         //     headers: {
//         //         'Content-Type': 'application/json',
//         //         'X-CSRFToken' : csrftoken,
//         //     },
//         //     body: JSON.stringify({
//         //         'filter': this.value,
//         //         'cattegory': params.cattegory,
//         //         "productId": null,
//         //     })
//         // })
//         // .then(response =>{
//         //     return response.json()
//         // })
//         // .then((data) => {
//         //     console.log(data)
//         // })
//     })
