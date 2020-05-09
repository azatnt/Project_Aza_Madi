let getSliderIcons = document.getElementsByClassName("cart-promo");

for (let i = 0; i < getSliderIcons.length; i++) { // Берем из БД URL и вставляем в BG image
    let getUrl = getSliderIcons[i].getAttribute("data-url");
    getSliderIcons[i].style.backgroundImage =  "url(" + getUrl + ")";
}

