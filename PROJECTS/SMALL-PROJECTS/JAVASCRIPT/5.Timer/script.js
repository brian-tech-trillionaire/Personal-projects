let timer = null;
let seconds = 0;

function updateDisplay () {
  let min = Math.floor(seconds/60);
  let sec = seconds%60

  document.getElementById('display').textContent =
  String(min).padStart(2,'0') + ':' +
  String(sec).padStart(2,'0');
}

function startTimer () {
  if (!timer == null) return;

  timer = setInterval(() => {
    seconds++;
    updateDisplay();
  },1000); 
}

function pauseTimer() {
  clearInterval(timer);
  timer = null;
}

function resetTimer () {
  pauseTimer();
  seconds = 0;
  updateDisplay();
}