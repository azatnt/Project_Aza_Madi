let getSliderIcons = document.getElementsByClassName("cart-promo");

for (let i = 0; i < getSliderIcons.length; i++) { // Берем из БД URL и вставляем в BG image
    let getUrl = getSliderIcons[i].getAttribute("data-url");
    getSliderIcons[i].style.backgroundImage =  "url(" + getUrl + ")";
}


// Дропдаун меню настройки юзера
let btnChangeUser = document.querySelector(".btn-change button");
let userInfo = document.querySelector(".profile .profile__info");
let isCheckedUser = false;

btnChangeUser.addEventListener("click", () => {
    if (userInfo.style.visibility == "hidden") {
        userInfo.style.visibility = "visible";
    }
    else {
        userInfo.style.visibility = "hidden";
    }
});



// Анимация добавления продуктов в корзину

// let addBasket = document.querySelector(".add-basket");

// addBasket.addEventListener('click', () => {
//     console.log('hello');
// });



// Обои юзеров

const wallpaperUrl = document.querySelector('.profile');

let wallpaper = wallpaperUrl.getAttribute('data-wallpaper');
wallpaperUrl.style.backgroundImage = "url(" + wallpaper +  ")";