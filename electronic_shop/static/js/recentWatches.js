recentWatched = JSON.parse(getCookie('recentWatched'));
const recentWatchedBoxes = document.querySelector('.boxes-watched');

recentWatched.forEach(id => {

    const url = `/api/product/${id}`


    fetch(url, {
        method: 'GET',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        }
    })
    .then(response => { return response.json()})
    .then(data => {

        let newDiv = document.createElement('div');
        let newAhref = document.createElement('a');
        let newImg = document.createElement('img');

        newImg.src = data.img;
        newImg.alt = 'Product image recent watched';

        newAhref.appendChild(newImg);
        newDiv.classList.add('box', 'flex-container');
        newDiv.appendChild(newAhref);

        recentWatchedBoxes.appendChild(newDiv);
    })
})


