$(document).ready(function(){
  $('.sidenav').sidenav({edge: "right"});
  //https://stackoverflow.com/questions/36581504/materialize-carousel-slider-autoplay 
  $('.carousel').carousel({
    padding: 200    
});
autoplay();
function autoplay() {
    $('.carousel').carousel('next');
    setTimeout(autoplay, 2000);
}
});