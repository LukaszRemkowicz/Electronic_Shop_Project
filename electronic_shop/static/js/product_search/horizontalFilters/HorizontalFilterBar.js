const queryFilters = document.querySelectorAll('.horizontal-filters .tick span');
const producentList = document.querySelectorAll('.producent-label span');
const rating = document.querySelectorAll('.rating-stars .tick .check');


function deleteUrlParam(element){
    urlSearchParams = new URLSearchParams(window.location.search);
    params = Object.fromEntries(urlSearchParams.entries());
    urlSearchParams.delete(element.toLowerCase())
    window.history.pushState("object or string", "Title", `?${urlSearchParams}`);
}


function checkClicked(){
    urlSearchParams = new URLSearchParams(window.location.search);
    params = Object.fromEntries(urlSearchParams.entries());
    console.log('paramyyyy', params)
    for(let [param, value] of Object.entries(params)){
        console.log(param, value);
        try{
            let catchElement = document.querySelector(`[data-filter="${param}=${value}"]`);
            catchElement.firstElementChild.classList.add('newClass');
            catchElement.style.backgroundColor = '#ff503c';
        } catch(e){
            console.log(e);
        }
    }
}

checkClicked()

function addCheckBoxes(element, queryAll) {

    queryAll.forEach(el => {
        try{
            el.firstElementChild.classList.remove('newClass');
        } catch(e){
            // console.log(e);
        }
        el.style.backgroundColor = '#f8f8f8';
        checkClicked()
    });

    element.firstElementChild.classList.add('newClass');
    element.style.backgroundColor = '#ff503c';
}

function removeSelectedBoxed(element, filters){
    const filter = element.dataset.filter.split('=');
    if(element.firstElementChild.classList.contains('newClass')){
        element.firstElementChild.classList.remove('newClass');
        element.style.backgroundColor = '#f8f8f8';

        let whatToDelete = element.dataset.filter.split('=')[0];
        deleteUrlParam(whatToDelete)

    }else{
        changeUrls(filter[0], filter[1]);
        addCheckBoxes(element, filters)
    }
}


queryFilters.forEach(element => {
    element.addEventListener('click', () =>{
        removeSelectedBoxed(element, queryFilters)
        // const filter = element.dataset.filter.split('=');
        // if(element.firstElementChild.classList.contains('newClass')){
        //     element.firstElementChild.classList.remove('newClass');
        //     element.style.backgroundColor = '#f8f8f8';

        //     let whatToDelete = element.dataset.filter.split('=')[0];
        //     deleteUrlParam(whatToDelete)

        // }else{
        //     changeUrls(filter[0], filter[1]);
        //     addCheckBoxes(element, queryFilters)
        // }

    })
})

producentList.forEach(element => {
    element.addEventListener('click', () =>{
        removeSelectedBoxed(element, producentList)
        // const filter = element.dataset.filter.split('=');
        // if(element.firstElementChild.classList.contains('newClass')){
        //     element.firstElementChild.classList.remove('newClass');
        //     element.style.backgroundColor = '#f8f8f8';

        //     let whatToDelete = element.dataset.filter.split('=')[0];
        //     deleteUrlParam(whatToDelete)
        // }else{
        // changeUrls(filter[0], filter[1]);
        // addCheckBoxes(element, producentList);
        // }
    })
})

rating.forEach(element =>{
    element.addEventListener('click', () => {
        removeSelectedBoxed(element, rating)
        // const filter = element.dataset.filter.split('=');
        // if(element.firstElementChild.classList.contains('newClass')){
        //     element.firstElementChild.classList.remove('newClass');
        //     element.style.backgroundColor = '#f8f8f8';

        //     let whatToDelete = element.dataset.filter.split('=')[0];
        //     deleteUrlParam(whatToDelete)
        // }else{
        // changeUrls(filter[0], filter[1]);
        // addCheckBoxes(element, rating);
        // }
    })
})



