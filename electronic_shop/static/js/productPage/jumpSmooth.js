const jumpElements = document.querySelectorAll('.jump-smooth');

jumpElements.forEach(element => {
    element.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute("href")).scrollIntoView({
            behavior: 'smooth'
        })
    })
})