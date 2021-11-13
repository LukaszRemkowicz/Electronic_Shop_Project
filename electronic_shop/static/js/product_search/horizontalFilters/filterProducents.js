const producentList = document.querySelectorAll('.producent-label span');
const rating = document.querySelectorAll('.rating-stars .tick .check');

producentList.forEach(element => {
    element.addEventListener('click', () =>{
        const filter = element.dataset.filter.split('=');
        changeUrls(filter[0], filter[1]);
        addCheckBoxes(element, producentList);
    })
})

rating.forEach(element =>{
    element.addEventListener('click', () => {
        const filter = element.dataset.filter.split('=');
        changeUrls(filter[0], filter[1]);
        addCheckBoxes(element, rating);
    })
})