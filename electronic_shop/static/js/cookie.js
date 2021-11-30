function getCookie(name) {
    // Split cookie string and get all individual name=value pairs in an array
    const cookieArr = document.cookie.split(";");

    // Loop through the array elements
    for(let i = 0; i < cookieArr.length; i++) {
        const cookiePair = cookieArr[i].split("=");

        /* Removing whitespace at the beginning of the cookie name
        and compare it with the given string */
        if(name == cookiePair[0].trim()) {
            // Decode the cookie value and return
            return decodeURIComponent(cookiePair[1]);
        }
    }

    // Return null if not found
    return null;
}

// Create cookie

let cart = JSON.parse(getCookie('cart'));
let recentWatched = JSON.parse(getCookie('recentWatched'));

const createCookie = (cookieEl, cookieName) => {
    if (cookieEl === null){
        if(cookieName == 'cart'){
            cookieEl = {}
        } else {
            cookieEl = []
        }
        console.log(`${cookieName} was created`)
        document.cookie = `${cookieName}=` + JSON.stringify(cookieEl) + ";domain=;path=/"
    }
};

createCookie(cart, 'cart');
createCookie(recentWatched, 'recentWatched');


console.log("Cart: ", cart);
console.log("recentWatched: ", recentWatched);
