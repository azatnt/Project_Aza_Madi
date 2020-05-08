let searchFood = document.getElementsByName("search-food")[0];
let getInfo = searchFood.value;

searchFood.addEventListener("mouseleave", () => {
    let searchIcon = document.querySelector(".search-icon");
    searchIcon.style.display = "block";
});

searchFood.addEventListener("mousemove", () => {
    let searchIcon = document.querySelector(".search-icon");
    if (getInfo.length > 0) {
        searchIcon.style.display = "none";
    }

});
