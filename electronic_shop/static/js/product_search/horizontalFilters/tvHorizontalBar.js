let producentFilter = document.querySelector('.checkchecked');
const curved = document.querySelector('.curved');
const smartTv = document.querySelector('.smart')


function addEventToProducentLists(){
    producentFilter.addEventListener('click', () => {

        const producent = document.querySelector('.producentsFilters').innerText.toString()
        console.log('jestem w evencie');
        let producentsFilter = document.querySelector('.producentFilters');

        if(producentsFilter.checked){

            changeUrls('producent', producent);
            location.reload();
        }
    })


}

addEventToProducentLists();

function addCheckBoxes(elementToSplit){
    let status = document.querySelector(`.tick .check .${elementToSplit}Div`);

    if (window.location.href.includes(elementToSplit)){
        const splitted = window.location.href.split('&');
        splitted.forEach(element => {

            if (element.includes(elementToSplit)){

                if (element.split(`${elementToSplit}=`)[1] == 'Yes'){

                    status.classList.add('newClass');
                    status.parentNode.style.backgroundColor = '#ff503c';

                } else {

                    status.classList.remove('newClass');
                    status.parentNode.style.backgroundColor = '#f8f8f8';
                }
            }
        })

    }
}

addCheckBoxes('curved');
addCheckBoxes('smart');

function checkClicked(elementToSplit, bool, opositeBool){
    let status = document.querySelector(`.tick .check .${elementToSplit}Div`);

    if(status.classList.value === `${elementToSplit}Div`){
        changeUrls(elementToSplit, bool);
        status.classList.add('newClass');
        status.parentNode.style.backgroundColor = '#ff503c';
        location.reload();
    } else{
        changeUrls(elementToSplit, opositeBool);
        status.classList.remove('newClass');
        status.parentNode.style.backgroundColor = '#f8f8f8';
        location.reload();
    }
}


curved.addEventListener('click', () =>{
    checkClicked('curved', 'Yes', 'No');
});
smartTv.addEventListener('click', () =>{
    checkClicked('smart', 'Yes', 'No');
})
