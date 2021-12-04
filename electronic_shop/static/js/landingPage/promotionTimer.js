let getHour = document.querySelector('.time-hour');
let getMinutes = document.querySelector('.time-minutes');
let getSeconds = document.querySelector('.time-seconds');

countDown();

function countDown(){
    const promoDate = document.querySelector('.hour').dataset.promotime

    const oldDate = new Date(promoDate);
    let newDate = new Date(promoDate);
    const now = new Date();

    newDate.setDate(newDate.getDate()+1);

    // if (now.getSeconds() == newDate.getSeconds()) {
    //     newDate = resetOfferDate();
    // }

    const offerTime = newDate - now;

    let timeSeconds = Math.floor((offerTime / 1000) % 60);
    let timeMinutes = Math.floor((offerTime / (1000 * 60) % 60));
    let timeHours = Math.floor((offerTime / (1000 * 60 * 60) % 24));

    if(timeHours <= 0 && timeMinutes <= 0 && timeSeconds <= 0){
        clearInterval(countDown);
        const buyBtn = document.querySelector('.sold-left .button');
        buyBtn.innerHTML = '';

        const newBtn = document.createElement('button');
        newBtn.classList.add('buy', 'btn-light', 'd-block');

        const newSpan = document.createElement('span');
        newSpan.innerHTML = 'Sold all';

        newBtn.appendChild(newSpan);
        newBtn.style.border = '1px solid rgb(204, 204, 204)';
        newBtn.style.padding = '1rem';
        newBtn.disabled = true;

        buyBtn.appendChild(newBtn);
        buyBtn.style.cursor = 'default';

    }

    // console.log(timeSeconds, timeMinutes, timeHours)

    getHour.innerHTML = `${timeHours.toString().length >= 2 ? timeHours : "0"+timeHours}`;
    getMinutes.innerHTML = `${timeMinutes.toString().length >= 2 ? timeMinutes : "0"+timeMinutes}`;
    getSeconds.innerHTML = `${timeSeconds.toString().length >= 2 ? timeSeconds : "0"+timeSeconds}`;
}

function resetOfferDate() {
    const futureDate = new Date();
    futureDate.setDate(futureDate.getDate() + 15);
    return futureDate;
}

setInterval(countDown, 1000);
