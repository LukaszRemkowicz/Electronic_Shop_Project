const welcomeBtn = document.querySelector('.my-welcome-modal-btn');
const myModal = document.querySelector('.my-welcome-modal');

welcomeBtn.addEventListener('click', ()=> {
    setCookie('welcomemodal','1',7);
    myModal.style.display = 'none';
})


function checkCookie() {
    console.log('cookie', !getCookie('welcomemodal'))
    if (getCookie('welcomemodal')) {
        myModal.classList.add("d-none");
        myModal.classList.remove("d-block");
    } else {
        myModal.classList.remove("d-none");
        myModal.classList.add("d-block");
    }
}

checkCookie()