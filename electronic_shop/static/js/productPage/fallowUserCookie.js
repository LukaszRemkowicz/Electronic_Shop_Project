recentWatched = JSON.parse(getCookie('recentWatched'));

try{
    if(recentWatched.indexOf(+productId) == -1){
        if(recentWatched.length >= 5){
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
