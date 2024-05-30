<?php
session_start();

$user_name = $_SESSION['user_name'];
$phone = $_SESSION['phone'];
$address = $_SESSION['address'];
?>
<!DOCTYPE HTML>
<html lang="ja">
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
        <p><?php echo $user_name; ?></p>
        <p><?php echo $phone; ?></p>
        <p><?php echo $address; ?></p>
    </body>
</html>




