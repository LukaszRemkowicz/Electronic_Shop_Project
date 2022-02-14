const maxSize = window.matchMedia('(min-width: 1201px)');
const mediaQuery = window.matchMedia('(max-width: 1200px) and (min-width: 701px)');
const mediumQuery = window.matchMedia('(max-width: 700px) and (min-width: 600px');
const small = window.matchMedia('(max-width: 599px) and (min-width: 500px');
const extraSmall = window.matchMedia('(max-width: 300px)')

let articles = document.querySelectorAll('.blog-articles div');
// recentWatched = JSON.parse(getCookie('recentWatched'));
// const recentWatchedBoxes = document.querySelector('.boxes-watched');
// let productsWatched = [];


articles = [...articles];
const ids = articles.map(element => +element.dataset.articleid);
const url = `/api/products/[${ids}]`;

let newData;



fetch(url, {
  method: 'GET',
  headers: {
    'Content-Type': 'application/json',
    'X-CSRFToken' : csrftoken,
  }})
  .then(response => response.json())
  .then(data =>{

    // Fire queries when the page load
    runMediaQueries(data);

    mediaQuery.addEventListener('change', ()=> {
      runMediaQueries(data);
    });

    mediumQuery.addEventListener('change', ()=> {
      runMediaQueries(data);
    });

    small.addEventListener('change', () => {
      runMediaQueries(data);
    });

    maxSize.addEventListener('change', () => {
      runMediaQueries(data);
    });
  })


function getDocument(data, numSlice){
  data.forEach(element => {
    const article = document.querySelector(`[data-articleId="${element['id']}"]`);
    article.querySelector('p').innerHTML = element.content_wysiwyg.slice(0, numSlice);
  })
};

function runMediaQueries(data){

  if (mediaQuery.matches) {
    getDocument(data, 400)
  } else if(mediumQuery.matches){
    getDocument(data, 150)
  } else if(small.matches){
    getDocument(data, 100)
  } else if(maxSize.matches){
    getDocument(data, 50)
  }
};


function userLikeQuery(){
  if(extraSmall.matches){
    setTimeout(() =>{
      document.querySelector('[id^=userlike]').style.display = 'none'
    }, 3000);
    document.querySelector('.navbar .form-inline').classList.remove('border')
  }
};

extraSmall.addEventListener('change', () =>{
  userLikeQuery();
  }
);

userLikeQuery();

// TODO media for recentWatched