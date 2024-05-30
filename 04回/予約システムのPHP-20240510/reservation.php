<?php
ini_set('display_errors', true);
error_reporting(E_ALL);

function h($string)
{
    return htmlspecialchars($string, ENT_QUOTES, 'utf-8');
}

session_start();

// エラーを格納する変数
$err = [];

// 「ログイン」ボタンが押されて、POST通信のとき
if (filter_input(INPUT_SERVER, 'REQUEST_METHOD') === 'POST') {
    $user_name = filter_input(INPUT_POST, 'user_name');
    $phone = filter_input(INPUT_POST, 'phone');
    $address = filter_input(INPUT_POST, 'address');

    if ($user_name === '') {
        $err['user_name'] = 'ユーザー名は入力必須です。';
    }
    if ($phone === '') {
        $err['phone'] = '電話番号は入力必須です。';
    }
    if ($address === '') {
        $err['address'] = '住所は入力必須です。';
    }

    // エラーがないとき
    if (count($err) === 0) {
        $_SESSION['user_name'] = $user_name;
        $_SESSION['phone'] = $phone;
        $_SESSION['address'] = $address;
        header('Location:reservation_main.php');
        return;
    }
}
?>
<!DOCTYPE HTML>
<html lang="ja">
    <head>
        <meta charset="UTF-8">
        <title>予約</title>
        <style type="text/css">
            .error {
                color: red;
            }
        </style>
    </head>
    <body>
        <div id="wrapper">
            <form action="" method="post">
                <p>
                    <label for="">ユーザー名</label>
                    <input id="user_name" name="user_name" type="text" />
                    <?php if (isset($err['user_name'])) : ?>
                        <p class="error"><?php echo h($err['user_name']); ?></p>
                    <?php endif; ?>
                </p>
                <p>
                    <label for="">電話番号</label>
                    <input id="phone" name="phone" type="text" />
                    <?php if (isset($err['phone'])) : ?>
                        <p class="error"><?php echo h($err['phone']); ?></p>
                    <?php endif; ?>
                </p>
                <p>
                    <label for="">住所</label>
                    <input id="address" name="address" type="text" />
                    <?php if (isset($err['address'])) : ?>
                        <p class="error"><?php echo h($err['address']); ?></p>
                    <?php endif; ?>
                </p>
                <p>
                    <button type="submit">送信</button>
                </p>
            </form>
        </div>
    </body>
</html>

