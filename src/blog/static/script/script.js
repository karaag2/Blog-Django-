// const contours = document.querySelectorAll(".contour");
// document.querySelector(".container form").addEventListener("click", () => {
//   contours.forEach((elem) => {
//     elem.style.border = "1px solid #b3b1b1";
//     elem.style.transform = "none";
//   });
// });
// contours.forEach((element) => {
//   element.addEventListener("click", () => {
//     // Réinitialiser tous les éléments (optionnel si tu veux désélectionner les autres)
//     contours.forEach((elem) => {
//       elem.style.border = "1px solid #b3b1b1";
//       elem.style.transform = "none";
//     });

//     // Appliquer les styles uniquement à l'élément cliqué
//     element.style.border = "2.5px solid black";
//     element.style.transform = "scale(1.01)";
//     element.style.transition = "transform 0.8s, border 0.8s";
//   });
// });

// console.log("Hello world");

const contours = document.querySelectorAll(".contour");

// Fonction pour réinitialiser les styles
function resetStyles() {
  contours.forEach((elem) => {
    elem.style.border = "1px solid #b3b1b1";
    elem.style.transform = "scale(1)";
  });
}

// Ajouter l'événement sur chaque élément `.contour`
contours.forEach((element) => {
  element.addEventListener("click", (event) => {
    // Empêcher la propagation du clic pour éviter de déclencher le reset immédiatement
    event.stopPropagation();
    
    // Réinitialiser tous les contours avant d'appliquer les styles au sélectionné
    resetStyles();
    
    // Appliquer le style au contour cliqué
    element.style.border = "2.5px solid black";
    element.style.transform = "scale(1.01)";
    element.style.transition = "all 0.2s";
  });
});

// Ajouter un écouteur d'événements sur `document` pour réinitialiser au clic hors d'un `.contour`
document.addEventListener("click", resetStyles);
