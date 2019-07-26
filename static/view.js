// When the user clicks on <div>, open the popup

function myFunction(event) {
  event.currentTarget.lastElementChild.classList.toggle("show");
  console.log("Called!")
}


const containers = document.querySelectorAll('.container');
console.log(containers)
containers.forEach((container) => {
  container.addEventListener('click', myFunction);
  console.log(container)
});
