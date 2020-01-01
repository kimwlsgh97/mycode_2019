<?php
$conn = mysqli_connect("127.0.0.1","root","KJHwhsgh1!","think");
if(mysqli_connect_errno()) {
  printf("로그인에 실패하셨습니다. : %s\n",mysqli_connect_error());
  exit();
}
echo '<h1>single row</h1>';
$sql = "select * from topic where id=12 limit 10";
$result = mysqli_query($conn, $sql);
//var_dump($result->num_rows);
$row = mysqli_fetch_array($result); //데이터베이스 정보를, php 배열형태로 표현함
//print_r($row);
// echo $row[0]; //배열
// echo $row['title']; //연관배열
echo '<h2>'.$row['title'].'</h2>';
echo $row['description'];

echo '<h1>multi rows</h1>';
$sql = "select * from topic";
$result = mysqli_query($conn, $sql);

while($row = mysqli_fetch_array($result)){
  //mysql_fetch_array는 참조할때마다 1씩 증가한다. 다음항으로 넘어간다, 표시할 값이없으면 NULL이된다.
  echo '<h2>'.$row['title'].'</h2>';
  echo $row['description'];
}


// $row = mysqli_fetch_array($result);
// var_dump($row);
 ?>
