function createSoldOutButton(element, text){
    element.innerHTML = '';

    const newBtn = document.createElement('button');
    newBtn.classList.add('buy', 'btn-light', 'd-block');

    const newSpan = document.createElement('span');
    newSpan.innerHTML = text;

    newBtn.appendChild(newSpan);
    newBtn.style.border = '1px solid rgb(204, 204, 204)';
    newBtn.style.padding = '1rem';
    newBtn.disabled = true;

    element.appendChild(newBtn);
    element.style.cursor = 'default';
}