document.addEventListener('DOMContentLoaded', function() {
  let table = document.getElementById('table');
  let file = '../kanji.json';
  $.getJSON(file, function(data) {
    let prefs = data.prefectures;
    $.each(prefs, function(index, pref) {
      let tr = document.createElement('tr');
      for (let prop of ["kanji", "kana", "prefecture"]) {
        let td = document.createElement('td');
        let text = document.createTextNode(pref[prop]);
        td.appendChild(text);
        tr.appendChild(td);
      }
      table.appendChild(tr);
    })
  })

}, false);