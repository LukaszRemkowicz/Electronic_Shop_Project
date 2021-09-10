let starsReviewForm = document.querySelectorAll('.stars-review-form')

let numClicked = 0

starsReviewForm.forEach(element =>{
    element.addEventListener('click', ()=>{
        let valueOfStars = event.target.dataset.numofstars
        numClicked = +valueOfStars;
        let parent = element.parentNode
        colourStars(parent)

    })
})

function colourStars(parentElement){

    // let parent = parentElement.parentNode

    parentElement.innerHTML = ''

    console.log('parentnode: ', parentElement)

    let newDiv = document.createElement('div');
    newDiv.classList.add('stars-in-review')
    

    for(let i = 1; i < (numClicked+1); i++){

        let newI = document.createElement('i');
        newI.classList.add('fas');
        newI.classList.add('fa-star');
        newI.classList.add('font-red');
        newI.classList.add('stars-review-form');
        newI.classList.add('fa-3x');
        newI.setAttribute('data-numofstars', `${i}`);
        console.log('wchodze: ', i);

        parentElement.append(newI);
        
    }  

    for(let i = (numClicked +1); i > numClicked && i <= 5; i++){
        let newI = document.createElement('i');
        newI.classList.add('far');
        newI.classList.add('fa-star');
        newI.classList.add('stars-review-form');
        newI.classList.add('fa-3x');
        newI.setAttribute('data-numofstars', `${i}`);
        
        console.log('wchodze: ', i);

        parentElement.append(newI);
    }
    
    starsReviewForm = [];
    starsReviewForm = document.querySelectorAll('.stars-review-form');

    starsReviewForm.forEach(element =>{
        element.addEventListener('click', ()=>{
            let valueOfStars = event.target.dataset.numofstars
            numClicked = +valueOfStars;
            let parent = element.parentNode
            colourStars(parent)
    
        })
    })
    
}



