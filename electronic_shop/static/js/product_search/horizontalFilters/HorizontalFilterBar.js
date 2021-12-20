const queryFilters = document.querySelectorAll('.horizontal-filters .form-inline');
// const queryFilters = document.querySelectorAll('.horizontal-filters .tick span');
// const producentList = document.querySelectorAll('.producent-label span');
const producentList = document.querySelectorAll('.producentFilters .form-inline');
// const rating = document.querySelectorAll('.rating-stars .tick .check');
const rating = document.querySelectorAll('.rating-stars .form-inline');


function deleteUrlParam(element){
    urlSearchParams = new URLSearchParams(window.location.search);
    params = Object.fromEntries(urlSearchParams.entries());
    urlSearchParams.delete(element.toLowerCase())
    window.history.pushState("object or string", "Title", `?${urlSearchParams}`);
}


function checkClicked(){
    urlSearchParams = new URLSearchParams(window.location.search);
    params = Object.fromEntries(urlSearchParams.entries());
    for(let [param, value] of Object.entries(params)){
        try{
            let catchElement = document.querySelector(`[data-filter="${param}=${value}"]`);
            catchElement.firstElementChild.classList.add('newClass');
            catchElement.style.backgroundColor = '#ff503c';
        } catch(e){
            // console.log(e);
        }
    }
}

checkClicked()

function addCheckBoxes(element, queryAll, rating=false) {

    queryAll.forEach(el => {
        if(rating){
            queryElement = el.querySelector('.tick .check');
        } else {
            queryElement = el.querySelector('.tick span');
        }
        try{
            queryElement.firstElementChild.classList.remove('newClass');
        } catch(e){
            // console.log(e);
        }
        queryElement.style.backgroundColor = '#f8f8f8';
    });

    checkClicked();
    element.firstElementChild.classList.add('newClass');
    element.style.backgroundColor = '#ff503c';
}

function removeSelectedBoxed(element, filters, event, rating){
    event.preventDefault()
    console.log(element);
    console.log(element.firstElementChild.classList.contains('newClass'));

    const filter = element.dataset.filter.split('=');
    if(element.firstElementChild.classList.contains('newClass')){
        element.firstElementChild.classList.remove('newClass');
        element.style.backgroundColor = '#f8f8f8';

        let whatToDelete = element.dataset.filter.split('=')[0];
        deleteUrlParam(whatToDelete)

    }else{
        changeUrls(filter[0], filter[1]);
        addCheckBoxes(element, filters, rating)
    }
}


queryFilters.forEach(element => {
    element.addEventListener('click', function(event) {
        element = element.querySelector('.tick span');
        removeSelectedBoxed(element, queryFilters, event)

    })
})

producentList.forEach(element => {
    element.addEventListener('click', function(event){
        element = element.querySelector('.tick span');
        removeSelectedBoxed(element, producentList, event)
    })
})

rating.forEach(rateDiv =>{
    console.log('rating list', rateDiv);
    rateDiv.addEventListener('click', function(event) {
        console.log('rating', rateDiv);
        element = rateDiv.querySelector('.tick .check');
        removeSelectedBoxed(element, rating, event, true)
    })
})
