const producentsList = document.querySelector('#country');


function changeCountry (producent){
    producent = producent.split(',');
    console.log(producent);
    let oldProducent = document.querySelector('.producentsFilters');
    oldProducent.innerHTML = producent[0];

    const newInput = document.createElement('input');
    newInput.type = 'checkbox';
    newInput.name = 'country';
    newInput.classList.add('producentFilters')
    newInput.value = producent[0];


    const newSpan = document.createElement('span');
    newSpan.classList.add('check');

    oldProducent.appendChild(newInput);
    oldProducent.appendChild(newSpan);


    let oldProducentNumber = document.querySelector('.countProducents');
    oldProducentNumber.innerHTML = producent[1]
    producentFilter = document.querySelector('.producentsFilters');
    addEventToProducentLists();
}

producentsList.addEventListener('change',  (e)=> {
        changeCountry(e.target.value);
    })
