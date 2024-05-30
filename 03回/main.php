<?php
/**
 * main.php
 *
 * @since 2018/09/18
 */
session_start();

require 'database.php';
$login_user = $_SESSION['login_user'];
$bbs_contents = $_SESSION['bbs'];
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

