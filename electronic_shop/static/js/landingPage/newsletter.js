const newsletterForm = document.querySelector('.newsletter-form');

newsletterForm.addEventListener('submit', (e) =>{
    e.preventDefault();
    let email = newsletterForm.querySelector('input').value;

    const url = '/api/newsletter/'

    fetch(url, {
        method: "POST",
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'email': email
        })
    })
    .then(response => response.json())
    .then(data => {

        newsletterForm.insertAdjacentHTML('beforebegin',
            `
            <div class="alert-success col-lg-offset-4 alert-dismissable w-100 " role="alert">
                <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                <span aria-hidden="true">&times;</span>
                </button>
                <p class=''>Thank you, your mail has been saved in our database</p>
            </div>`
            );
    })
})