recentWatched = JSON.parse(getCookie('recentWatched'));

try{
    if(!recentWatched.includes(+productId)){
        if(recentWatched.length >= 10){
            recentWatched.pop()
            recentWatched.unshift(+productId)
        }else{
            recentWatched.push(+productId);
        }
        document.cookie = `recentWatched=` + JSON.stringify(recentWatched) + ";domain=;path=/"
    };
} catch(e){
    console.log('Not this site', e);
}
