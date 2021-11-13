const appliedFilters = document.querySelectorAll('.filters-applied .close');

appliedFilters.forEach(element => {
    element.addEventListener('click', () => {
        urlSearchParams = new URLSearchParams(window.location.search);
        params = Object.fromEntries(urlSearchParams.entries());
        let param = element.parentNode.innerText;
        param = param.slice(0, param.length-2).replace(' ', '_')
        console.log(param);
        urlSearchParams.delete(param.toLowerCase())
        window.history.pushState("object or string", "Title", `?${urlSearchParams}`);
        window.location.reload();

    })
})