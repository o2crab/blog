document.addEventListener(
  "DOMContentLoaded",
  function () {
    let storage = localStorage;
    let iineMembers = ["untikun", "guest"]; //localStorage内のカウンタ名

    //storageのカウンタを初期化
    for (let i = 0, len = iineMembers.length; i < len; i++) {
      let mem = iineMembers[i];
      if (storage[mem] === undefined) {
        storage[mem] = 0;
      }
      text = "通算「いいね！」：" + storage[mem] + "件";
      document.getElementById(mem + "Cnt").textContent = text;
    }

    //clickされたらカウンタをインクリメントする
    for (let i = 0, len = iineMembers.length; i < len; i++) {
      let mem = iineMembers[i];
      let iineBtn = document.getElementById(mem + "Btn");
      iineBtn.addEventListener("click", function () {
        storage[mem] = storage[mem] - 0 + 1; //-0で Number型に
        text = "通算「いいね！」：" + storage[mem] + "件";
        document.getElementById(mem + "Cnt").textContent = text;
      });
    }

    let btns = document.getElementsByClassName("iineMember");
    for (let i = 0, len = btns.length; i < len; i++) {
      console.log('Hi');
    }

    console.log("Hi");
  },
  false
);
