<?php
ini_set( 'display_errors', 1 );
ini_set( 'error_reporting', E_ALL );
$db = new SQLite3("/var/www/html/test/test.db");

$sql = 'SELECT * FROM students';
$res = $db->query($sql);
?>
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>SQLite Test</title>
</head>
<body>
<?php
while( $row = $res->fetchArray() ) {
	echo '<p>' . var_dump($row) . '</p>';
}
?>
</body>
</html>
