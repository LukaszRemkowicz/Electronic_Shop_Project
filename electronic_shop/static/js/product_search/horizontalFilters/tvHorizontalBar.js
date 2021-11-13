const tvFilters = document.querySelectorAll('.tv-filters .tick span');


function checkClicked(){
    urlSearchParams = new URLSearchParams(window.location.search);
    params = Object.fromEntries(urlSearchParams.entries());
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
            console.log(e);
        }
        el.style.backgroundColor = '#f8f8f8';
        checkClicked()
    });

    element.firstElementChild.classList.add('newClass');
    element.style.backgroundColor = '#ff503c';
    window.location.reload();
}

tvFilters.forEach(element => {
    element.addEventListener('click', () =>{
        const filter = element.dataset.filter.split('=');
        changeUrls(filter[0], filter[1]);
        addCheckBoxes(element, tvFilters)
    })
})





