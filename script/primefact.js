
document.addEventListener('DOMContentLoaded', function () {

  let input = document.getElementById('prime-in');
  let output = document.getElementById('prime-out');

  input.addEventListener('change', function () {
    let orinum = Number.parseInt(input.value);
    if (orinum >= 2) {
      let num = orinum;
      let ary = [];
      while (num > 1) {
        for (let i = 2; i <= num; i++) {
          if (num % i === 0) {
            ary.push(i);
            num /= i;
            break;
          }
        }
      }

      if (ary.length === 1) {
        output.textContent = `${orinum}は素数です！`;
      } else {
        output.textContent = `${orinum} = ${ary.join('×')}`;
      }
    } else if (orinum === 1) {
      output.textContent = '1は素数ではありません。'
    } else {
      output.textContent = '入力を確認してください。';
    }

  }, false);
}, false);