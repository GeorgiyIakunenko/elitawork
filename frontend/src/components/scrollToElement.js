export const scrollToSection = (sectionId) => {
  const offsetTop = document.querySelector("#" + sectionId).offsetTop;
  console.log(offsetTop);
  window.scrollTo({
    top: offsetTop - 100,
    behavior: "smooth",
  });
};
