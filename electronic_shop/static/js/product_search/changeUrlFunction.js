function changeUrls(filter, boolean){
    let url = window.location.href;
    let newParam;

    url = url.replace('#', '')

    if(url.split('&').length >= 2 || window.location.href.includes(filter)){

        let newUrl = window.location.href.replace('#', '').split('?');
        let urlSplitted = newUrl[1].split('&')

        urlSplitted.forEach((element, index) =>{
            if(element.includes(`${filter}=`)){
                urlSplitted[index] = `${filter}=${boolean}`;
            }
        });

        let urlJoined;

        if (urlSplitted.length >= 2){
            urlJoined = urlSplitted.join('&');
        } else {
            urlJoined = urlSplitted.join('?')
        };

        if (urlJoined.includes(filter) == false){
            urlJoined = urlJoined + `&${filter}=${boolean}`;
            urlJoined = newUrl[0] + '?' + urlJoined;
        } else {
            urlJoined = newUrl[0] + '?' + urlJoined;
        }

        window.history.pushState("", "", urlJoined);

    } else if(window.location.href.split('?').length >= 2){
        url = url.replace('#', '');
        window.history.pushState("object or string", "Title", `${url}&${filter}=${boolean}`);

    } else {
        window.location.replace(`${url}?grid=${boolean}`)
    }

    toogleButtons.forEach(element => {
        const buttonPage = element.getAttribute('href').split('&')[0];
        let getToogleOrFilter = window.location.href.replace('#', '').split('&')
        getToogleOrFilter = getToogleOrFilter.splice(1, getToogleOrFilter.length)

        getToogleOrFilter.forEach((element, index) => {
            if(element.includes(`${filter}=`)){
                getToogleOrFilter[index] = `${filter}=${boolean}`
            }
        })

        const newJoinedAtt = getToogleOrFilter.join('&');
        element.href = `${buttonPage}&${newJoinedAtt}`;
    })
}
