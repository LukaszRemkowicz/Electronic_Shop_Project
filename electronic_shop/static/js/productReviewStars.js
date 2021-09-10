const starsReviewForm = document.querySelectorAll('.stars-review-form')

let numClicked = 0

starsReviewForm.forEach(element =>{
    element.addEventListener('click', ()=>{
        let valueOfStars = event.target.dataset.numofstars
        numClicked = valueOfStars;
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
    
    let newI = document.createElement('i');
    newI.classList.add('fas');
    newI.classList.add('fa-star');
    newI.classList.add('font-red');
    newI.classList.add('fa-3x');

    for(let i = 1; i < (+numClicked+1); i++){

        parentElement.append(newI);
        
        
    }  
    
    

    
}



