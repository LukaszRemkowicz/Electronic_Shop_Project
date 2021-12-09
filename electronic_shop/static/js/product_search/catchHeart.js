const heart = document.querySelectorAll('.lni-heart');
const heartLiked = document.querySelectorAll('.fa-heart');
const wishlistNav = document.querySelector('.likesNum');

function fetchHeart (url, whatToDo){
    fetch(url, {
        method: 'PATCH',
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
        if(whatToDo == 'add'){
        try{
            wishlistNav.innerText = +wishlistNav.innerText + 1;
        } catch(e){
            console.log(e);
        }} else {
            try{
                wishlistNav.innerText = +wishlistNav.innerText - 1;
            } catch(e){
                console.log(e);
            }
        }

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
            el.style.display = 'inline-block'
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
            el.style.display = 'inline-block'
        })
    })


}catch(e){
    console.log(e);
}