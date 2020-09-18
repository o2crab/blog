<!DOCTYPE html>
<html lang="jp">
<head>
  <meta charset="utf-8">
  <title>いいね</title>
  <link rel="stylesheet" type="text/css" href="https://unpkg.com/ress/dist/ress.min.css">
  <link rel="stylesheet" href="css/style.css">
</head>

<body>
  <header class="cat-header">
    <div  class="wrapper" id="home-header-container"><!--idあとで確認-->
      <div class="header-group">
        <a href="index.html"><img class="logo" src="img/logo1trimmed.png" alt="LOGO"></a>
        <h1>セルフいいね</h1>
      </div>
      <p>左端のロゴをクリックすると、<br>ホームに戻れます。</p>
    </div>
  </header>

  <main class="wrapper">
    <h2>自分に『いいね！』しよう</h2>
    <div class="iine-member">
      <p>ウンチクん（BLOG運営者）</p>
      <input id="untikunBtn" type="button" value="いいね！">
      <p id="untikunCnt"></p>
    </div>
    <div class="iine-member">
      <p>ゲスト様</p>
      <input id="guestBtn" type="button" value="いいね！">
      <p id="guestCnt"></p>
    </div>

    <?php
    $file = 'iine.json';
    $data = file_get_contents($file);
    $obj = json_decode($data, true);
    //ユーザー毎に、ユーザ名、ボタン、いいね数　を表示
    foreach ($obj as $key => $value) {
      $block = <<<EOD
      <div id="{$key}" class="iine-member">
      <p>{$value["name"]}</p>
      <input class="iineBtn" type="button" value="いいね！">
      <p>通算「いいね！」：{$value["iine"]}件</p>
      </div>
      EOD;
      print $block;
    }
    ?>
  </main>

  <footer>
  </footer>

  <script src="script/iine.js"></script>
</body>
</html>
