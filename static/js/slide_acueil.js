window.addEventListener('load', function() {
    var slideshow = document.getElementById('slideshow');
    var slides = slideshow.getElementsByTagName('li');
    var currentSlide = 0;
    var slideInterval = setInterval(nextSlide, 3500); // Change slide every 2 seconds
  
    function nextSlide() {
      slides[currentSlide].style.display = 'none';
      currentSlide = (currentSlide + 1) % slides.length;
      slides[currentSlide].style.display = 'block';
    }
  });