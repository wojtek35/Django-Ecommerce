const mediaQuery = '800px'
let navButton = document.querySelector(".nav-button")
let navModal = document.querySelector(".nav-modal")
const opacityTransition = 400;
navModal.style.transition = `all ${opacityTransition}ms`

let navIcons = document.querySelectorAll("#main-nav ul i")
function myFunction(mobileScreen) {
    if (mobileScreen.matches) { // If media query matches
        navIcons.forEach(function(icon) {
            icon.classList.add("fa-xl")
        });
        navModal.style.display="none"
    } else {
        navIcons.forEach(function(icon) {
            icon.classList.remove("fa-xl")
        });
        navModal.style.display="block"
        
        
    }
  }
  
var mobileScreen = window.matchMedia(`(max-width: ${mediaQuery})`)
myFunction(mobileScreen) // Call listener function at run time
mobileScreen.addListener(myFunction) // Attach listener function on state changes


if (mobileScreen) {
    modalToggler()
}
function modalToggler() {
    $(navButton).hover(
        function(){ 
            $(navModal).toggleClass("visibleDisplay")
            setTimeout(function() {
                $(navModal).toggleClass("visibleOpacity")
            }, 1)
        },
        function(){ 
            $(navModal).toggleClass("visibleOpacity")
            setTimeout(function() {
                $(navModal).toggleClass("visibleDisplay")
            }, opacityTransition+1)
        },
    )
}

// Side menu
function openSlideMenu() {
    document.getElementById('side-menu').style.width = "250px"
}
function closeSlideMenu() {
    document.getElementById('side-menu').style.width = "0"
}