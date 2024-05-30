<?php
$dsn = 'sqlite:/var/www/html/test/test.db';
$stid = 12345678;

try {
	$pdo = new PDO($dsn);

	$sql = "select * from students where stid = :stid";

	$stmt = $pdo->prepare($sql);

	$stmt -> bindParam(":stid", $stid);

	$stmt -> execute();

	$rec = $stmt->fetch(PDO::FETCH_ASSOC);

} catch(PDOException $e) {
	exit(mb_convert_encoding($e->getMessage(), 'UTF-8', 'SJIS-win'));
}

function printItem($str)
{
	return htmlspecialchars($str, ENT_QUOTES, 'UTF-8');
}
?>
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>select</title>
</head>
<body>

<?php foreach ($rec as $item):?>
	<?=printItem($item)?>
<?php endforeach; ?>

</body>
</html>

