let sortData = document.querySelectorAll('.sort_items')

sortData.forEach(element =>{
    [...element.children].sort((a,b) =>  element.innerText<b.innerText?1:-1).forEach(node=>element.appendChild(node));
})