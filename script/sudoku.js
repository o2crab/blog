document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('message').addEventListener('mouseover', function(){
    this.innerHTML = '\u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b \u222b';
  }, false);
  document.getElementById('message').addEventListener('mouseleave', function(){
    this.textContent = '';
  }, false);

// sudokuの内容表示
  let ref = {
    A: 'intsin.svg',
    B: 'intcos.svg',
    C: 'inttansq.svg',
    D: 'intlog.svg',
    E: 'e.svg',
    F: 'f.svg',
    G: 'g.svg',
    H: 'ring.svg',
  }
  let display = document.getElementById('display');
  let imgary = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'];
  for (let i=0, len=imgary.length; i<len; i++) {
    let letter = imgary[i];
    let nodes = document.getElementsByClassName('sudoku' + letter)
    for (let i=0, len=nodes.length; i<len; i++) {
      let node = nodes[i];
      node.addEventListener('click', function() {
        display.innerHTML = `<h4>アルファベット${letter}の内容:</h4><img id="${'img'+letter}" src="sudoku/${ref[letter]}" alt="error">`;
        if (letter === 'F') {
          let anchor = document.createElement('a');
          anchor.href="#";
          anchor.id = "fclue";
          let text = document.createTextNode("ヒント");
          anchor.appendChild(text);
          display.appendChild(anchor);

          let br = document.createElement('br');
          display.appendChild(br);

          let fclue = document.getElementById('fclue');
          fclue.addEventListener('click', function(e) {
            let img = document.createElement('img');
            img.src = "sudoku/fclue.svg";
            img.id = "fclueimg";
            display.appendChild(img);
            e.preventDefault();
          }, false);
        }
      }, false);
    }
  }

  let Is = document.getElementsByClassName('sudokuI');
  for (let i=0, len=Is.length; i<len; i++) {
    let I = Is[i];
    I.addEventListener('click', function() {
      display.innerHTML = `
      <h4>アルファベットIの内容:</h4>
      <p>1,2,3,4の4文字で4x4マス(2x2区切り)のナンプレを作る。このとき、最小で何マス埋まっていれば一通りに解けるか？<br><br>例：</p>
      <div id="iex">
        <div class="iexblock">
          <p>1</p>
          <p></p>
          <p></p>
          <p>2</p>
        </div>
        <div class="iexblock">
          <p>4</p>
          <p></p>
          <p></p>
          <p>3</p>
        </div>
        <div class="iexblock">
          <p></p>
          <p></p>
          <p></p>
          <p>4</p>
        </div>
        <div class="iexblock">
          <p>3</p>
          <p></p>
          <p></p>
          <p></p>
        </div>
      </div>
      6マス埋まっている上のナンプレは解ける
      <div id="iex">
        <div class="iexblock">
          <p>1</p>
          <p>3</p>
          <p>4</p>
          <p>2</p>
        </div>
        <div class="iexblock">
          <p>4</p>
          <p>2</p>
          <p>1</p>
          <p>3</p>
        </div>
        <div class="iexblock">
          <p>2</p>
          <p>1</p>
          <p>3</p>
          <p>4</p>
        </div>
        <div class="iexblock">
          <p>3</p>
          <p>4</p>
          <p>2</p>
          <p>1</p>
        </div>
      </div>`;
    }, false);
  }

}, false);
