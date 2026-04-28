// Get elements
const images = document.querySelectorAll('.image img');
const lightbox = document.getElementById('lightbox');
const lightboxImg = document.getElementById('lightbox-img');
const caption = document.getElementById('caption');
const closeBtn = document.querySelector('.close');

// Add click event to each image
images.forEach(img => {
  img.addEventListener('click', () => {
    lightboxImg.src = img.src;
    caption.textContent = img.getAttribute('data-caption');
    lightbox.classList.add('show');
  });
});

// Close lightbox
closeBtn.addEventListener('click', () => {
  lightbox.classList.remove('show');
});

// Close lightbox when clicking outside the image
lightbox.addEventListener('click', (e) => {
  if (e.target === lightbox) {
    lightbox.classList.remove('show');
  }
});