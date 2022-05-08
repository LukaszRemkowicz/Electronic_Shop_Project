let starsReviewForm = document.querySelectorAll('.stars-review-form');
let getstarsParent = document.querySelector('.stars-in-review');
let baseClass = []

let numClicked = 0;
let active;


/* clear stars after moving the mouse from parent DIV */

const clearAllStarsEvent = (parentDiv, stars) => {
    parentDiv.parentNode.addEventListener('mouseleave', () => {
            for(let i = 0; i < stars.length; i++ ){
                if(baseClass.includes(stars[i]) === false ){
                    stars[i].className = 'far fa-star fa-2x stars-review-form';
                }
            }
        }
)
}

clearAllStarsEvent(getstarsParent, starsReviewForm)


/* clear stars after moving mouse outsite <i> element */

const clearStarsOnHoverEvent = (stars, clickedElement = '') => {
    stars.forEach(element => {
        element.addEventListener('mouseleave', () => {
                let loop;
                if(clickedElement){
                    loop = +clickedElement;
                } else {
                    loop = active-1;
                }

                for(let i = loop; i < starsReviewForm.length; i++ ){
                    starsReviewForm[i].className = 'far fa-star fa-2x stars-review-form';
                }
            }
        )
    })
}

clearStarsOnHoverEvent(starsReviewForm)


/* colour the stars on mouse hover */

const colourStarsEvent = (stars) => {
    stars.forEach(element =>{
        element.parentElement.addEventListener('mouseover', ()=>{

            let valueOfStars = event.target.dataset.numofstars;
            active = valueOfStars

            for (let i = 0; i< valueOfStars; i++){
                starsReviewForm[i].className = 'fas fa-star font-red fa-2x stars-review-form';
            };
        })
    })
}

colourStarsEvent(starsReviewForm)


/* Colour the stars on click event */

starsReviewForm.forEach(element =>{
    element.addEventListener('click', ()=>{
        let valueOfStars = event.target.dataset.numofstars
        numClicked = +valueOfStars;
        let parent = element.parentNode
        baseClass = [];
        colourStars(parent);
        starsReviewForm = document.querySelectorAll('.stars-review-form');
        clearStarsOnHoverEvent(starsReviewForm, valueOfStars);
        colourStarsEvent(starsReviewForm);
    })
})


function colourStars(parentElement){

    // let parent = parentElement.parentNode

    parentElement.innerHTML = ''

    let newDiv = document.createElement('div');
    newDiv.className = 'stars-in-review w-100 text-left pl-4'


    for(let i = 1; i < (numClicked+1); i++){

        let newI = document.createElement('i');
        newI.className = 'fas fa-star font-red fa-2x stars-review-form'
        newI.setAttribute('data-numofstars', `${i}`);

        parentElement.append(newI);
        baseClass.push(newI);

    }

    for(let i = (numClicked +1); i > numClicked && i <= 5; i++){
        let newI = document.createElement('i');
        newI.className = 'far fa-star fa-2x stars-review-form'
        newI.setAttribute('data-numofstars', `${i}`);

        parentElement.append(newI);
    }

    starsReviewForm = [];
    starsReviewForm = document.querySelectorAll('.stars-review-form');
    clearAllStarsEvent(getstarsParent, starsReviewForm);

    starsReviewForm.forEach(element =>{
        element.addEventListener('click', ()=>{
            let valueOfStars = event.target.dataset.numofstars
            numClicked = +valueOfStars;
            let parent = element.parentNode
            colourStars(parent);
            clearStarsOnHoverEvent(starsReviewForm, valueOfStars);
            colourStarsEvent(starsReviewForm);

        })
    })

}



