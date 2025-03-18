const contours = document.querySelectorAll(".contour");

contours.forEach((element) => {
  element.addEventListener("click", () => {
    contours.forEach((elem) => {
      elem[0].style.border = "2.5px solid black";
      elem.style.transform = "scale(1.01)";
      elem.style.transition = "transform 0.8s, border 0.8s";
    });
  });
});

console.log("Hello world");
