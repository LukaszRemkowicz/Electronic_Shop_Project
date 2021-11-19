const catchBtnAcceptFilter = document.querySelector('.filter-btn');
const observeDiv = catchBtnAcceptFilter.parentElement


setTimeout(() => {
    window.scrollTo({top: 0, behavior: 'smooth'});
    }, 500)


catchBtnAcceptFilter.addEventListener('click', () => {
    /** Accept applied filters */

    document.location.reload(true);
})


const observer = new IntersectionObserver( ([e]) => {
    /** Observe if "Filter" button is on sticky position */

    e.target.classList.toggle("is-pinned", e.intersectionRatio < 1)
}, {
    threshold: [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
});

observer.observe(observeDiv);
