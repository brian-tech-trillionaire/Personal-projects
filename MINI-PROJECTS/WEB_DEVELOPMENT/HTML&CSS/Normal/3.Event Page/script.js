// Countdown timer
const countdownElement = document.getElementById('countdown');

// Set the date we're counting down to (July 31, 2026)
const countDownDate = new Date("July 31, 2026 10:00:00").getTime();

// Update the count down every 1 second
const x = setInterval(function() {
  // Get today's date and time
  const now = new Date().getTime();

  // Find the distance between now and the count down date
  const distance = countDownDate - now;

  // Time calculations for days, hours, minutes and seconds
  const days = Math.floor(distance / (1000 * 60 * 60 * 24));
  const months = Math.floor(days / 30);
  const remainingDays = days % 30;
  const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((distance % (1000 * 60)) / 1000);

  // Display the result in the element
  countdownElement.innerHTML = months + "mo " + remainingDays + "d " + hours + "h " + minutes + "m " + seconds + "s ";

  // If the count down is finished, write some text
  if (distance < 0) {
    clearInterval(x);
    countdownElement.innerHTML = "EXPIRED";
  }
}, 1000);

// Smooth scroll for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    document.querySelector(this.getAttribute('href')).scrollIntoView({
      behavior: 'smooth'
    });
  });
});

// Form submission (placeholder)
document.querySelector('.register-form').addEventListener('submit', function(e) {
  e.preventDefault();
  alert('Registration submitted! (This is a placeholder)');
});