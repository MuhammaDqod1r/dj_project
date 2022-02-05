
window.addEventListener('DOMContentLoaded', function() {
    const loader = document.querySelector('.preload_page')
    setTimeout(function() {
        loader.style.opacity = '0'
        setTimeout(function() {
            loader.classList.add('none')
        }, 500)
    }, 2000)
})
