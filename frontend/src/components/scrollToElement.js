export const scrollToSection = (sectionId, isSmooth = true) => {
  const offsetTop = document.querySelector("#" + sectionId).offsetTop;
  //console.log(offsetTop);
  window.scrollTo({
    top: offsetTop - 100,
    behavior: isSmooth ? "smooth" : "auto",
  });

  return offsetTop;
};
