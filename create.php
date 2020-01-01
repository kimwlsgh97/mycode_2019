<?php
  $conn = mysqli_connect("127.0.0.1","root","KJHwhsgh1!","think");
  if(mysqli_connect_errno()) {
    printf("로그인에 실패하셨습니다. : %s\n",mysqli_connect_error());
    exit();
  }

  $topic = "SELECT * FROM topic limit 10";
  $result = mysqli_query($conn, $topic);
  while($row = mysqli_fetch_array($result)){
    //<li><a href="index.php?id=11">MySQL</a></li>
    $escaped_in_title = htmlspecialchars($row['title']);
    $list = $list."<li><a href=\"index.php?id={$row['id']}\">$escaped_in_title</a></li>";
    // $desc = $desc.$row['description']; -- 리스트형식으로 표현하는게 아니라 특정링크마다 다르게
  }; //---mysqli_fetch_array가 직접실행되어야 늘어남, $row는 불가능

  $author = "SELECT * FROM author";
  $result2 = mysqli_query($conn,$author);
  //print_r($result2);되고 echo $result2는 안돼?
  $select_form = '<select name="author_id">';
  while($row2 = mysqli_fetch_array($result2)){
    $select_form .= '<option value="'.$row2['id'].'">'.$row2['name'].'</option>';
  };
  $select_form .= '</select>';
  //$select_form = $select_form.'</select>';

 ?>

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <h1><a href="index.php">WEB</a></h1>
    <p><a href="index.php">topic</a></p>
    <ol>
      <?=$list?>
     </ol>
    <form action="process_create.php" method="post">
      <p><input type="text" name="title" placeholder="title"></p>
      <!-- placeholder="title" : 여기서 입력받은 정보를 title이라는 이름으로 내보낸다 -->
      <p><textarea name="description" placeholder="description"></textarea></p>
      <?=$select_form?>
      <p><input type="submit"></p>
    </form>
    <!-- placeholder는 데이터를 어느곳에 저장할것인지 지정해준다 -->
  </body>
</html>
