let menu = document.querySelector("#menu-btn");
let navbar = document.querySelector(".navbar");

menu.onclick = () => {
  menu.classList.toggle("fa-times");
  navbar.classList.toggle("active");
};

window.onscroll = () => {
  menu.classList.remove("fa-times");
  navbar.classList.remove("active");
};

document.querySelector("#search-icon").onclick = () => {
  document.querySelector("#search-form").classList.toggle("active");
};
document.querySelector("#close").onclick = () => {
  document.querySelector("#search-form").classList.remove("active");
};

var swiper = new Swiper(".home-slider", {
  spaceBetween: 30,
  centeredSlides: true,
  autoplay: {
    delay: 7500,
    disableOnInteraction: false,
  },
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  loop: true,
  grabCursor:true,
   loop:true,
   centeredSlides:true,
   navigation: {
     nextEl: ".swiper-button-next",
     prevEl: ".swiper-button-prev",
   },
});
var swiper = new Swiper(".food-slider", {
  grabCursor: true,
  loop: true,
  centeredSlides: true,
  spaceBetween: 20,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    700: {
      slidesPerView: 2,
    },
    1000: {
      slidesPerView: 3,
    },
  },
});

let previewContainer = document.querySelector(".food-preview-container");
let previewBox = previewContainer.querySelectorAll(".food-preview");

document.querySelectorAll(".food .slide").forEach((food) => {
  food.onclick = () => {
    previewContainer.style.display = "flex";
    let name = food.getAttribute("data-name");
    previewBox.forEach((preveiw) => {
      let target = preveiw.getAttribute("data-target");
      if (name == target) {
        preveiw.classList.add("active");
      }
    });
  };
});

previewContainer.querySelector("#close-preview").onclick = () => {
  previewContainer.style.display = "none";
  previewBox.forEach((close) => {
    close.classList.remove("active");
  });
};

var swiper = new Swiper(".reviews-slider", {
  grabCursor: true,
  loop: true,
  centeredSlides: true,
  autoHeight: true,
  spaceBetween: 20,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    700: {
      slidesPerView: 2,
    },
    1000: {
      slidesPerView: 3,
    },
  },
});
var swiper = new Swiper(".blogs-slider", {
  grabCursor:true,
  loop:true,
  centeredSlides:true,
  autoHeight:true,
  spaceBetween: 20,
  pagination: {
     el: ".swiper-pagination",
     clickable: true,
  },
  breakpoints: {
     0: {
       slidesPerView: 1,
     },
     700: {
       slidesPerView: 2,
     },
     1000: {
       slidesPerView: 3,
     },
  },
});
