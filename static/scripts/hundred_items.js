const descBody = document.getElementById("id-desc-body-container");
const idOpenedIcon = document.getElementById("id-desc-header-is-opened-icon");

idOpenedIcon.style.backgroundImage = "url(/static/icons/arrow_left.png)";

let isDescOpened = false;

document.getElementById("id-desc-open-button").addEventListener('click', () => {
    if (isDescOpened) {
        descBody.style.display = "none";
        idOpenedIcon.style.backgroundImage = "url(/static/icons/arrow_left.png)";
    }
    else {
        descBody.style.display = "block";
        idOpenedIcon.style.backgroundImage = "url(/static/icons/arrow_down.png)";
    }
    isDescOpened = !isDescOpened;
});

document.onload = () => {
    idOpenedIcon.style.backgroundImage = "url(/static/icons/arrow_left.png)";
}