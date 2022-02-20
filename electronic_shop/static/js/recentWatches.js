recentWatched = JSON.parse(getCookie('recentWatched'));
const recentWatchedBoxes = document.querySelector('.boxes-watched');

let productsWatched = [];
console.log('hjestem przed ifgem');
console.log('recentWatched1', recentWatched);

if(window.screen.width <= 1080 && window.screen.width >= 980){
    recentWatched = recentWatched.splice(0, recentWatched.length-2);
    jumpOnWatched();
}else if(window.screen.width < 980 && window.screen.width >= 760){
    recentWatched = recentWatched.splice(0, recentWatched.length-5);
    jumpOnWatched();
} else{
    document.querySelector('.recentWatched').style.display = 'none'
}


function checkWatched(data){
    if(productsWatched.length >= recentWatched.length && productsWatched.every(element => element === null)){
        document.querySelector('.recentWatched').style.display = 'none'
    } else if(data.main_photo){
        let newDiv = document.createElement('div');
        let newAhref = document.createElement('a');
        newAhref.href = `/products/${data.cattegory}/${data.id}`

        let newImg = document.createElement('img');

        newImg.src = data.main_photo;
        newImg.alt = 'Product image recent watched';

        newAhref.appendChild(newImg);
        newDiv.classList.add('box', 'flex-container');
        newDiv.appendChild(newAhref);

        recentWatchedBoxes.appendChild(newDiv);
    }
}

function jumpOnWatched(){
    recentWatched.forEach(id => {

        const url = `/api/product/${id}`

        if(id){
            fetch(url, {
                method: 'GET',
                headers: {
                    'Content-type': 'application/json',
                    'X-CSRFToken': csrftoken,
                }
            })
            .then(response => response.json())
            .then(data => {

                if(data.detail != 'Not found.' || !data.main_photo){
                    productsWatched.push(data)
                } else {
                    productsWatched.push(null)
                }

                checkWatched(data);
            })
        }
    })
}




