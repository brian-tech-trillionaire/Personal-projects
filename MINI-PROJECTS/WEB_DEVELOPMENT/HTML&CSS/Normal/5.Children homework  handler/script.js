document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.getElementById('subject-search');
  const clearButton = document.getElementById('clear-search');
  const subjectCards = Array.from(document.querySelectorAll('.subject-card'));
  const detailsText = document.querySelector('.details-text');
  const topButton = document.querySelector('.top');

  function updateDetails(subject) {
    detailsText.textContent = `Selected ${subject}. Explore lesson notes, assignment checkpoints, and useful reminders for this topic.`;
  }

  function filterSubjects(value) {
    const query = value.trim().toLowerCase();
    let visibleCount = 0;

    subjectCards.forEach((card) => {
      const subject = card.dataset.subject.toLowerCase();
      const isMatch = subject.includes(query);
      card.style.display = isMatch ? 'flex' : 'none';
      if (isMatch) {
        visibleCount += 1;
      }
    });

    if (!query) {
      detailsText.textContent = 'Select a subject card to see a quick overview and suggested activities.';
      return;
    }

    detailsText.textContent = visibleCount
      ? `Showing ${visibleCount} subject${visibleCount === 1 ? '' : 's'} matching "${value}".`
      : 'No matches found. Please try another subject name.';
  }

  searchInput.addEventListener('input', (event) => {
    filterSubjects(event.target.value);
  });

  clearButton.addEventListener('click', () => {
    searchInput.value = '';
    searchInput.focus();
    filterSubjects('');
  });

  subjectCards.forEach((card) => {
    card.addEventListener('click', () => {
      updateDetails(card.dataset.subject);
      subjectCards.forEach((item) => item.classList.remove('active'));
      card.classList.add('active');
    });
  });

  topButton.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
});
