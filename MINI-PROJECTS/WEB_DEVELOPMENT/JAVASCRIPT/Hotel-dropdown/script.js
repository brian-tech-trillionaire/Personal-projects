document.addEventListener('DOMContentLoaded', () => {
  const hotel = document.getElementById('Hotel-menu');
  const drop = document.getElementById('list');
  if (!hotel || !drop) return;

  hotel.addEventListener('click', () => {
    const isHidden = window.getComputedStyle(drop).display === 'none';
    drop.style.display = isHidden ? 'block' : 'none';
  });
});