const messageBtn = document.querySelector('.messages-div button');
const messageDFiv = document.querySelector('.messages-div');

messageBtn.addEventListener('click', () => {
    messageDFiv.classList.remove('d-flex');
    messageDFiv.classList.add('d-none')
})