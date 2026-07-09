const userinput = document.querySelector(".user input");
const userClearButton = document.querySelector(".user button");

userinput.addEventListener("input", (event) =>
  userClearButton.classList.toggle("visible", event.target.value)
);

userClearButton.addEventListener("click", (event) => {
  event.stopImmediatePropagation();
  event.preventDefault();
  userClearButton.classList.remove("visible");
  userinput.value = "";
});

const search = document.querySelector(".search input");
const searchSearchButton = document.querySelector(".search button");
const searchIcon = document.querySelector(".search .icon");
const searchSpinner = document.querySelector(".search .spinner");

searchSearchButton.addEventListener("click", function s(){
  search.focus();
  s.stopImmediatePropagation();
  searchIcon.classList.add("hidden");
  searchSpinner.classList.add("visible");

  console.log("works");

  setTimeout(() => {
    searchIcon.classList.remove("hidden");
    searchSpinner.classList.remove("visible");
    search.value = "";
    search.blur();
  }, 1000);
});

function togglePopup() {
    const overlay = document.getElementById('popupOverlay');
    overlay.classList.toggle('show');
}