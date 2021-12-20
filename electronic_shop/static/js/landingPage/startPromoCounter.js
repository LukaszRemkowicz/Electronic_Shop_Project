const promoDate = document.querySelector('.hourBaseHtml').dataset.promotime;
const baseProductId = document.querySelector('.baseId').dataset.productid;
let newInterval;

function countDown(){

    const oldDate = new Date(promoDate);
    let newDate = new Date(promoDate);
    const now = new Date();
    newDate.setDate(newDate.getDate()+1);
    const offerTime = newDate - now;

    let timeSeconds = Math.floor((offerTime / 1000) % 60);
    let timeMinutes = Math.floor((offerTime / (1000 * 60) % 60));
    let timeHours = Math.floor((offerTime / (1000 * 60 * 60) % 24));

    console.log(timeSeconds, timeMinutes, timeHours);

    if(timeHours >= 0 && timeMinutes >= 0 && timeSeconds >= 0){
    } else {

        clearInterval(newInterval);
        if(baseProductId){
            fetch(`/api/product/${baseProductId}/`, {
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
        }
    }
}

function resetOfferDate() {
    const futureDate = new Date();
    futureDate.setDate(futureDate.getDate() + 15);
    return futureDate;
}


newInterval = setInterval(countDown, 50000);
countDown();




