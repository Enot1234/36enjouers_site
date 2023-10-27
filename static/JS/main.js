// Кнопка прокрутки
var button = document.querySelector('.down_arrow')

button.onclick = function() {
    window.scrollTo({
        top: 0,
        left: 0,
        behavior: 'smooth'
    });
}
