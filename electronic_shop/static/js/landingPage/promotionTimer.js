let getHour = document.querySelector('.time-hour');
let getMinutes = document.querySelector('.time-minutes');
let getSeconds = document.querySelector('.time-seconds');
let getProductId;

try{
    getProductId = document.querySelector('.sold-left .update-cart').dataset.product
} catch (e){
    getProductId = null
}

if(getProductId){
    countDownLandingPage();
}

function countDownLandingPage(){
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
        try{
            clearInterval(newIntervalLandingpage);
        } catch (e){
            console.log(e);
        }
        try{
            const buyBtn = document.querySelector('.sold-left .button');
            buyBtn.innerHTML = '';

            const newBtn = document.createElement('button');
            newBtn.classList.add('buy', 'btn-light', 'd-block');

            const newSpan = document.createElement('span');
            newSpan.innerHTML = 'Promotion ended';

            newBtn.appendChild(newSpan);
            newBtn.style.border = '1px solid rgb(204, 204, 204)';
            newBtn.style.padding = '1rem';
            newBtn.disabled = true;

            buyBtn.appendChild(newBtn);
            buyBtn.style.cursor = 'default';

            getHour.innerHTML = `00`;
            getMinutes.innerHTML = `00`;
            getSeconds.innerHTML =`00`;
        } catch (e){
            console.log(e);
        }

        fetch(`/api/product/${getProductId}/`, {
            method: 'PATCH', 
            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({
                "user_id": 1,
                "fields": {
                    "product_of_the_day": false,
                    "promotion": null
                }
            })
        })

    } else{
        // console.log(timeSeconds, timeMinutes, timeHours);
        try{
        getHour.innerHTML = `${timeHours.toString().length >= 2 ? timeHours : "0"+timeHours}`;
        getMinutes.innerHTML = `${timeMinutes.toString().length >= 2 ? timeMinutes : "0"+timeMinutes}`;
        getSeconds.innerHTML = `${timeSeconds.toString().length >= 2 ? timeSeconds : "0"+timeSeconds}`;
        } catch (e){
            console.log(e);
        }
    }
}

function resetOfferDate() {
    const futureDate = new Date();
    futureDate.setDate(futureDate.getDate() + 15);
    return futureDate;
}

let newIntervalLandingpage;

if(getProductId){
    newIntervalLandingpage = setInterval(countDownLandingPage, 1000);
}
