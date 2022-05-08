const tables = document.querySelectorAll('#specification .spec__table p:nth-child(1)');
const tablesSecondP = document.querySelectorAll('#specification .spec__table p:nth-child(2)');
const tablesh6 = document.querySelectorAll('#specification h6');


tables.forEach(element => {
    element.classList.add('font-light-grey');
    element.style.fontWeight = 400;
    element.style.fontHeight = 1.5;
    element.style.fontSize = '0.9rem'
});

tablesSecondP.forEach(element => {
    element.style.fontSize = '0.9rem'
});

tablesh6.forEach(element => {
    element.style.fontSize = '0.9rem'
});
