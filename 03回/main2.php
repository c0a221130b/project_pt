<?php
/**
 * main.php
 *
 * @since 2018/09/18
 */
session_start();

require 'database2.php';
$login_user = [];
$bbs_contents = [];
$user_name = "";

// エラーを格納する変数
$err = [];

// 「送信」ボタンが押されて、POST通信のとき
if (filter_input(INPUT_SERVER, 'REQUEST_METHOD') === 'POST') {
    $user_name = filter_input(INPUT_POST, 'user_name');
    $article_title = filter_input(INPUT_POST, 'article_title');
    $article_comments = filter_input(INPUT_POST, 'article_comments');

    if ($article_title === '') {
        $err['article_title'] = '題名は入力必須です。';
    }
    if ($article_comments === '') {
        $err['article_comments'] = '本文は入力必須です。';
    }

    // エラーがないとき
    if (count($err) === 0) {

        // DB接続
        $pdo = connect();

        // ステートメント
        $stmt = $pdo->prepare('INSERT INTO `BBSlog` (`id`, `article_title`, `user_name`, `article_comments`) VALUES (null, ?, ?, ?)');

        // パラメータ設定
        $params = [];
        $params[] = $article_title;
        $params[] = $user_name;
        $params[] = $article_comments;

        // SQL実行
        $success = $stmt->execute($params);

        // ステートメント
        $stmt2 = $pdo->prepare('SELECT * FROM BBSlog');

        // SQL実行
        $stmt2->execute();

        // レコードセットを取得
        $bbs_contents = $stmt2->fetchAll();
    }
} else {
    $login_user = $_SESSION['login_user'];
    $bbs_contents = $_SESSION['bbs'];
    $user_name = $login_user['user_name'];
}
?>
<!DOCTYPE HTML>
<html lang="ja">
    <head>
        <meta charset="UTF-8">
        <title>掲示板サンプル</title>
        <style type="text/css">
        <!--
            h1 { color: green }
            strong { color: blue; font-size: large }
            em { font-style: italic }
        -->
        </style>
    </head>
    <body>
        <h1>私の掲示板</h1>

        <p>ご自由に書き込んでください。</p>

        <form action="" method="post">
            <div>
                <?php if (isset($err['article_title'])) : ?>
                    <p class="error"><?php echo h($err['article_title']); ?></p>
                <?php endif; ?>
                <label for="article_title">題名</label><input type="text" name="article_title" size="60"><br>
                <input type="hidden" name="user_name" value="<?php echo $user_name; ?>"><br>
                <?php if (isset($err['article_comments'])) : ?>
                    <p class="error"><?php echo h($err['article_comments']); ?></p>
                <?php endif; ?>
                <label for="">本文</label><br>
                <textarea cols="60" rows="5" name="article_comments"></textarea><br>
                <button type="submit">送信</button>
                <button type="reset">リセット</button>
            </div>
        </form>

        <hr>
        <?php foreach ($bbs_contents as $bbs_content) : ?>
            <div>
            <?php for ($i = 0; $i < count($bbs_content); $i++) : ?>
                <?php list($key, $var) = each($bbs_content); ?>
                <?php if ($i == 1) : ?>
                    <strong><?php echo h($var); ?></strong><br>
                <?php endif; ?>
                <?php if ($i == 2) : ?>
                    <em><?php echo h($var); ?></em><br><br>
                <?php endif; ?>
                <?php if ($i == 3) : ?>
                    <?php echo h($var); ?>
                <?php endif; ?>
            <?php endfor; ?>
            </div><hr>
        <?php endforeach; ?>
    </body>
</html>

