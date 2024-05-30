#!c:/perl64/bin/perl

# ユーザ設定
$CHARSET = 'utf-8';
$DATAFILE = './log.txt';

# メインプログラム
readFormData();
readDatafile();
writeDatafile();
browsePage();
exit;

# フォームデータの読み込み
sub readFormData
{
  my ($buffer, $pair);

  if($ENV{'REQUEST_METHOD'} eq 'POST') {

    read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
  }
  else {
    $buffer = $ENV{'QUERY_STRING'};
  }

  foreach $pair (split(/&/, $buffer)) {
    my ($name, $value) = split(/=/, $pair);

    $value =~ tr/+/ /;
    $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/chr(hex($1))/eg;
    $value =~ s/&/&amp;/g;
    $value =~ s/</&lt;/g;
    $value =~ s/>/&gt;/g;
    $value =~ s/\x0D\x0A/<br>/g;
    $value =~ tr/\t/ /;

    $FORM{$name} = $value;
  }
}
# データファイルの読み込み
sub readDatafile
{
  open(FILE, "<$DATAFILE");
  eval{ flock(FILE, 1) };
  @DATA = <FILE>;
  close FILE;
}

# データファイルへの書き出し
sub writeDatafile
{
  if($FORM{'title'} && $FORM{'author'} && $FORM{'text'}) {
    unshift @DATA, "$FORM{'title'}\t$FORM{'author'}\t$FORM{'text'}\n";
    open(FILE, ">$DATAFILE");
    eval{ flock(FILE, 2) };
    print FILE @DATA;
    close FILE;
  }
}
# 掲示板ページの表示
sub browsePage
{
  print <<END;
Content-type: text/html; charset=$CHARSET

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
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
<p>
  ご自由に書き込んでください。
  </p>

  <form action="./bbs.cgi" method="post"><div>
    題名<input type="text" name="title" size="60"><br>
    名前<input type="text" name="author" size="20"><br>
    本文<br>
    <textarea cols="60" rows="5" name="text"></textarea><br>
    <input type="submit" value="送信">
    <input type="reset" value="リセット">
  </div></form>

  <hr>
END

  my ($i);
  for($i = "0"; $i < @DATA; ++$i) {
    my ($title, $author, $text) = split(/\t/, $DATA[$i]);
    print "<div><strong>$title</strong><br><em>$author</em><br><br>$text</div><hr>\n";
  }

  print <<END;
</body>
</html>
END
}

