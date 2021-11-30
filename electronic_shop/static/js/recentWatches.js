try{
    if(!recentWatched.includes(productId)){
        recentWatched.push(+productId)
        document.cookie = `recentWatched=` + JSON.stringify(recentWatched) + ";domain=;path=/"
    };
} catch(e){
    console.log('Not this site');
}

recentWatched = JSON.parse(getCookie('recentWatched'));

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
        console.log(data);
    })
})


