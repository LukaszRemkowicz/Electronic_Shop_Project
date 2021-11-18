const heart = document.querySelectorAll('.buy-list-view .lni-heart');
const heartLiked = document.querySelectorAll('.buy-list-view .fa-heart');

function fetchHeart (url, whatToDo){
    fetch(url, {
        method: 'POST', 
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'user_id': userId,
            'fields': {
                'likes': whatToDo
            }
        })
    })
    .then((response) => {
        return response.json()
    })
    .then(data => {
        console.log((data));
    })
}

try{
    heart.forEach(element => {
        element.addEventListener('click', (e) => {
            const url = `/api/product/${e.target.dataset.heart}/`;
            fetchHeart(url, 'add');
            element.style.display = 'none';
            const el = element.parentNode.querySelector('.fa-heart');
            el.classList.remove('d-none');
            el.style.display = 'block'
        })
    })
} catch(e) {
    console.log(e);
}



try{
    heartLiked.forEach(element => {
        element.addEventListener('click', (e) => {
            const url = `/api/product/${e.target.dataset.heart}/`;
            fetchHeart(url, 'remove');
            element.style.display = 'none';
            console.log(element.parentNode.querySelector('.lni'));
            const el = element.parentNode.querySelector('.lni');
            el.classList.remove('d-none');
            el.style.display = 'block'
        })
    })
    

}catch(e){
    console.log(e);
}