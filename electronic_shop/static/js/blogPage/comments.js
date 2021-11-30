const changePic = document.querySelectorAll('.profileImage');
const reply = document.querySelectorAll('.reply');
const commentsForm = document.querySelector('.comments-form');
let newForm = document.querySelector('.newForm');
let articleId = document.querySelector('.be-comment-block').dataset.articleid


const formElement = function(id, parentId){
    console.log(`document.contains(document.querySelector('.newForm'))`, document.contains(document.querySelector('.newForm')));
    if(document.contains(document.querySelector('.newForm'))){
        console.log('wchodze do forma');
        document.querySelector('.newForm').remove();
        return ''
    } else{

    return `<form name='csrfmiddlewaretoken' ${csrftoken} class="form-block newForm" data-formId=${id} method='POST'> \
        <input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}">
        <div class="row justify-content-between mr-3"> \
            <div class="col-xs-12 col-sm-5 px-0"> \
                <div class="form-group fl_icon "> \
                    <div class="icon"><i class="fa fa-user"></i></div> \
                    <input name='name' class="form-input" type="text" placeholder="Your name"> \
                </div> \
            </div> \
            <div class="col-xs-12 col-sm-5 fl_icon px-0" >\
                <div class="form-group fl_icon"> \
                    <div class="icon"><i class="fa fa-envelope-o"></i></div> \
                    <input name='email' class="form-input" type="text" placeholder="Your email"> \
                </div> \
            </div> \
            <div class="col-xs-12 w-100"> \
                <div class="form-group"> \
                    <textarea name='content' class="form-input" required="" placeholder="Join the discussion \ and leave a comment!"></textarea> \
                </div> \
            </div> \
            <div class="col-xs-12 w-100 d-none">
                <div class="form-group">
                    <input class="form-input" name='article-id' value='${articleId}' required=""></input>
                </div>
            </div>
            <div class="col-xs-12 w-100 d-none">
                <div class="form-group">
                    <input class="form-input" name='parent' value='${parentId}' required=""></input>
                </div>
            </div>
            <button  class="btn btn-brown pull-right">submit</button> \
        </div> \
    </form>`
    }

}


/** Add bootstrap alert */
function showAlert(data, successOrNot, text){
    let showCase = document.querySelector('.another-navbar')
    showCase.insertAdjacentHTML('afterend',
    `
    <div class="alerts alert-${successOrNot} col-lg-offset-4 alert-dismissable w-100" role="alert">
        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
        <span aria-hidden="true">&times;</span>
        </button>
        <p class='mb-0'>${text}</p>
    </div>`
    );
}

/** Add "pic" to comment. */
changePic.forEach( element => {
    const name = element.dataset.ownercomment.split(' ');
    let result;

    if (name.lenght >= 2){
        result = `${name[0][0]}${name[1][0]}`
    } else{
        result = `${name[0][0]}${name[0][1]}`
    }

    element.innerHTML = result
})

/** Add newform after clicking "reply" button */
reply.forEach( element => {
    element.addEventListener('click', () => {
        const parentId = element.querySelector('.get-parent').dataset.parent;
        let newElement = element.parentElement.parentElement.parentElement;
        newElement = newElement.querySelector('.node-comment');
        const id = element.dataset.commentid;
        console.log(id);
        newElement.insertAdjacentHTML('afterend', formElement(id, parentId));
        addeventToNewForm(element);
    })
});

/** Fetch to backend API */
function fetchComment(element){
    let commentsObj = Object();
    element.forEach(element => {
        console.log(element);
        let name = element.name
        commentsObj[name] = element.value
    });

    console.log('commentsObj', commentsObj);

    if(commentsObj.parent == undefined){
        commentsObj.parent = ''
    }

    const url = `/api/blog/${commentsObj['article-id']}/comments/`;

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrftoken,
        },
        body: JSON.stringify({
            'name': commentsObj.name,
            'email': commentsObj.email,
            'comment': commentsObj.content,
            'article': commentsObj['article-id'],
            'parent': commentsObj.parent
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
          });
        if(data.comment){
            showAlert(data, 'success', 'Comment has been sent to our employee');
        }else{
            showAlert(data, 'danger', 'Opps, something wen wrong');
        }
    })
}

/** Fire main form event */
commentsForm.addEventListener('submit', (e) => {
    e.preventDefault();
    let inputs = commentsForm.querySelectorAll('.form-input');

    fetchComment(inputs);
})

/** Fire event to newForms */
function addeventToNewForm (element){
    try{
    newForm = document.querySelector('.newForm');
    newForm.addEventListener('submit', (e) => {
        const parentId = element.querySelector('.get-parent').dataset.parent;
        e.preventDefault();
        let inputs = newForm.querySelectorAll('.form-input');

        fetchComment(inputs, parentId);
        e.preventDefault();
    })
    } catch(e){
        console.log(e);
    }
}

