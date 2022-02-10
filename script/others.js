document.addEventListener('DOMContentLoaded', function() {
  let table = document.getElementById('table');
  let file = `{
  "prefectures": [
      { "code": 1, "prefecture": "北海道", "kanji": "足寄", "kana": "あしょろ"},
      { "code": 2, "prefecture": "青森県", "kanji": "艫作崎", "kana": "へなしざき"},
      { "code": 3, "prefecture": "岩手県", "kanji": "束稲山", "kana": "たばしねやま"},
      { "code": 4, "prefecture": "宮城県", "kanji": "登米市　登米町", "kana": "とめし　とよままち"},
      { "code": 5, "prefecture": "秋田県", "kanji": "象潟", "kana": "きさかた"},
      { "code": 6, "prefecture": "山形県", "kanji": "飯豊", "kana": "いいで"},
      { "code": 7, "prefecture": "福島県", "kanji": "桑折", "kana": "こおり"},
      { "code": 8, "prefecture": "茨城県", "kanji": "潮来", "kana": "いたこ"},
      { "code": 9, "prefecture": "栃木県", "kanji": "五十里湖", "kana": "いかりこ"},
      { "code": 10, "prefecture": "群馬県", "kanji": "掃部ヶ岳", "kana": "かもんがたけ"},
      { "code": 11, "prefecture": "埼玉県", "kanji": "蕨", "kana": "わらび"},
      { "code": 12, "prefecture": "千葉県", "kanji": "我孫子", "kana": "あびこ"},
      { "code": 13, "prefecture": "東京都", "kanji": "福生", "kana": "ふっさ"},
      { "code": 14, "prefecture": "神奈川県", "kanji": "不入斗", "kana": "いりやまず"},
      { "code": 15, "prefecture": "新潟県", "kanji": "新発田", "kana": "しばた"},
      { "code": 16, "prefecture": "富山県", "kanji": "今生津", "kana": "いもず"},
      { "code": 17, "prefecture": "石川県", "kanji": "松任", "kana": "まっとう"},
      { "code": 18, "prefecture": "福井県", "kanji": "左右", "kana": "そう"},
      { "code": 19, "prefecture": "山梨県", "kanji": "忍野", "kana": "おしの"},
      { "code": 20, "prefecture": "長野県", "kanji": "麻績", "kana": "おみ"},
      { "code": 21, "prefecture": "岐阜県", "kanji": "各務原", "kana": "かかみがはら"},
      { "code": 22, "prefecture": "静岡県", "kanji": "内匠", "kana": "たくみ"},
      { "code": 23, "prefecture": "愛知県", "kanji": "国閑町", "kana": "かいごちょう"},
      { "code": 24, "prefecture": "三重県", "kanji": "度会町　注連指", "kana": "わたらいちょう　しめさす"},
      { "code": 25, "prefecture": "滋賀県", "kanji": "膳所", "kana": "ぜぜ"},
      { "code": 26, "prefecture": "京都府", "kanji": "旅籠町", "kana": "はたごまち"},
      { "code": 27, "prefecture": "大阪府", "kanji": "毛人谷", "kana": "えびたに"},
      { "code": 28, "prefecture": "兵庫県", "kanji": "八鹿", "kana": "ようか"},
      { "code": 29, "prefecture": "奈良県", "kanji": "入之波", "kana": "しおのは"},
      { "code": 30, "prefecture": "和歌山県", "kanji": "永穂", "kana": "なんご"},
      { "code": 31, "prefecture": "鳥取県", "kanji": "車尾", "kana": "くずも"},
      { "code": 32, "prefecture": "島根県", "kanji": "温泉津", "kana": "ゆのつ"},
      { "code": 33, "prefecture": "岡山県", "kanji": "美作", "kana": "みまさか"},
      { "code": 34, "prefecture": "広島県", "kanji": "胡町", "kana": "えびすちょう"},
      { "code": 35, "prefecture": "山口県", "kanji": "日置", "kana": "へき"},
      { "code": 36, "prefecture": "徳島県", "kanji": "大歩危", "kana": "おおぼけ"},
      { "code": 37, "prefecture": "香川県", "kanji": "塩飽諸島", "kana": "しわくしょとう"},
      { "code": 38, "prefecture": "愛媛県", "kanji": "松前", "kana": "まさき"},
      { "code": 39, "prefecture": "高知県", "kanji": "波介", "kana": "はげ"},
      { "code": 40, "prefecture": "福岡県", "kanji": "直方", "kana": "のおがた"},
      { "code": 41, "prefecture": "佐賀県", "kanji": "厳木", "kana": "きゅうらぎ"},
      { "code": 42, "prefecture": "長崎県", "kanji": "父ヶ岳", "kana": "ててがたけ"},
      { "code": 43, "prefecture": "熊本県", "kanji": "和水", "kana": "なごみ"},
      { "code": 44, "prefecture": "大分県", "kanji": "万年山", "kana": "はねやま"},
      { "code": 45, "prefecture": "宮崎県", "kanji": "可愛岳", "kana": "えのだけ"},
      { "code": 46, "prefecture": "鹿児島県", "kanji": "俣川洲", "kana": "またごし"},
      { "code": 47, "prefecture": "沖縄県", "kanji": "保栄茂", "kana": "びん"}]
  }`;
  $.post("others.html", file, function(data) {
    let prefs = data.prefectures;
    $.each(prefs, function(index, pref) {
      let tr = document.createElement('tr');
      for (const prop of ["kanji", "kana", "prefecture"]) {
        let td = document.createElement('td');
        let text = document.createTextNode(pref[prop]);
        td.appendChild(text);
        tr.appendChild(td);
      }
      table.appendChild(tr);
    })
  })

}, false);
