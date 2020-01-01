<?php
// $mysqli = mysqli_connect("example.com", "user", "password", "database");
// $res = mysqli_query($mysqli, "SELECT 'Please, do not use ' AS _msg FROM DUAL");
// $row = mysqli_fetch_assoc($res);
// echo $row['_msg'];

$conn=mysqli_connect("127.0.0.1","root","KJHwhsgh1!","think");
//mysqli_query($conn,"USE think") -- 위에서 어떤데이터베이스를 사용할건지 지정해놓음;
if (mysqli_connect_errno()) {
  printf("Connect failed: %s\n", mysqli_connect_error());
  exit();
}
//Connect failed: Access denied for user 'root'@'localhost' (using password: YES)
//mysqli_connect_error()는 mysql 로그인과정 에서 발생한 오류의 내용을 가르키는 표현식


$sql="
  INSERT INTO topic
    (title, description, created)
  VALUE(
      'MySQL',
      'MySQL is...',
      NOW()
    )
"; //한문장이 끝날때 마다 ;으로 마무리 짓는것 까먹지말기 - php문장끝을 표기
$result = mysqli_query($conn, $sql);
if($result === false){
  echo mysqli_error($conn);
}
 ?>
