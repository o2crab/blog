document.addEventListener('DOMContentLoaded', function () {

  // let txt = 'abcdefghijklmnopqrstuvwxyz';
  let txt = 'abcdefg';
  let display = document.getElementById('display');
  display.textContent = txt;
  document.addEventListener('keydown', function (e) {
    if (e.key === display.textContent[0]) {
      let p = /(.)(.*)/;
      display.textContent = display.textContent.replace(p, '$2');
      if (display.textContent.length < 4) {
        display.textContent = 'Congraturation!';
      }
    }
  }, false);

  let startbtn = document.getElementById('startbtn');
  startbtn.addEventListener('click', function () {
    display.textContent = txt;
    let timer = setTimeout(function () {
      addLetter(15000, 500);
    }, 1000);
  }, false);

  function randomAbc() {
    return randomInt(10, 35).toString(36);

    function randomInt(min, max) {
      return Math.floor((Math.random() * (max - min + 1)) + min);
    }
  }

  function addLetter(dur, interval) {
    let start = Date.now();
    let timer = setInterval(function () {
      let timePassed = Date.now() - start;
      if (display.textContent === 'Congraturation!') {
        clearInterval(timer);
        return;
      }
      if (timePassed >= dur) {
        clearInterval(timer);
        display.textContent = 'GAME OVER';
        return;
      }
      display.textContent = display.textContent.concat(randomAbc());
    }, interval);
  }

}, false);
