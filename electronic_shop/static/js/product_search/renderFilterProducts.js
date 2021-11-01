const filterParameter = document.querySelector('.product-filter-parameter');
const urlSearchParams = new URLSearchParams(window.location.search);
const params = Object.fromEntries(urlSearchParams.entries());
// const URL = '/api/product-dict/';

filterParameter.addEventListener('change', function(){
        const parameters = window.location.href.replace('#', '').split('&');
        console.log(parameters)
        let newValue = this.value

        if (parameters.length >= 2){
            let newUrl = window.location.href.replace('#', '').split('filter=');


            parameters.forEach((element, index) => {
                if (element.includes('filter=')){
                    parameters[index] = `filter=${newValue}`;
                }
            })

            let urlJoined = parameters.join('&');

            if (!urlJoined.includes('filter')){
                urlJoined += `&filter=${this.value}`;
            }

            console.log('po joinu', urlJoined);
            window.location.replace(urlJoined)
        } else{
            window.location.replace(`${url}&filter=${this.value}`)
        }
        // fetch(URL, {
        //     method: 'POST',
        //     headers: {
        //         'Content-Type': 'application/json',
        //         'X-CSRFToken' : csrftoken,
        //     },
        //     body: JSON.stringify({
        //         'filter': this.value,
        //         'cattegory': params.cattegory,
        //         "productId": null,
        //     })
        // })
        // .then(response =>{
        //     return response.json()
        // })
        // .then((data) => {
        //     console.log(data)
        // })
    })
