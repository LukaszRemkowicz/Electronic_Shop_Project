const searchQuery = document.querySelectorAll('.getCategorry');
const queryForm = document.querySelector('.search-query');

searchQuery.forEach(element => {
    element.addEventListener('click', (e) =>{
        e.preventDefault();

        console.log(element.name);
        console.log('sdwqedwd');
        const mainDrop = document.querySelector('.drop-main');
        const mainDropText = mainDrop.innerHTML;

        const choosen = element.name

        mainDrop.innerHTML = choosen;

    })
})

queryForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const searchParam = document.querySelector('.drop-main').innerHTML;
    changeUrls('param', searchParam);
    const query = queryForm.querySelector('input').value
    changeUrls('search_query', query);

    window.location.href = `/search/result/${window.location.search}`
        

})
