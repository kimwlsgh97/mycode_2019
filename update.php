<?php
  $conn = mysqli_connect("127.0.0.1","root","KJHwhsgh1!","think");
  if(mysqli_connect_errno()) {
    printf("로그인에 실패하셨습니다. : %s\n",mysqli_connect_error());
    exit();
  }

  $topic = "SELECT * FROM topic";
  $result = mysqli_query($conn, $topic);
  while($row = mysqli_fetch_array($result)){
    //<li><a href="index.php?id=11">MySQL</a></li>
    $escaped_in_title = htmlspecialchars($row['title']);
    $list = $list."<li><a href=\"index.php?id={$row['id']}\">$escaped_in_title</a></li>";
    // $desc = $desc.$row['description']; -- 리스트형식으로 표현하는게 아니라 특정링크마다 다르게
  }; //---mysqli_fetch_array가 직접실행되어야 늘어남, $row는 불가능

  $article = array(
    'title'=>'Welcome',
    'description'=>'Hello, web'
  );

  if(isset($_GET['id'])){
    $filtered_id = mysqli_real_escape_string($conn, $_GET['id']);
    $select_id = "SELECT * FROM topic WHERE id={$filtered_id}";
    $result2 = mysqli_query($conn, $select_id);
    $row2 = mysqli_fetch_array($result2);
    // $title = $row2['title'];
    // $article = $row2['description'];
    $escaped_out_title = htmlspecialchars($row2['title']);
    $escaped_out_description = htmlspecialchars($row2['description']);
    $article['title'] = $escaped_out_title;
    $article['description'] = $escaped_out_description;
  }
  else{
    echo "에러코드 44303 : 페이지 주소를 확인하세요";
    exit();
  }
 ?>


<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <h1><a href="index.php">WEB</a></h1>
    <ol>
      <?=$list?>
     </ol>
    <form action="process_update.php" method="post">
      <input type="hidden" name="id" value="<?=$filtered_id?>">
      <!-- 눈에 보이지않게 정보를 전송 -->
      <p><input type="text" name="title" placeholder="title" value="<?=$article['title']?>"></p>
      <!-- placeholder="title" : 여기서 입력받은 정보를 title이라는 이름으로 내보낸다 -->
      <p><textarea name="description" placeholder="description"><?=$article['description']?></textarea></p>
      <!-- <textarea>내용</textarea> 으로 텍스트영역안에 글을 표시할수 있다 -->
      <p><input type="submit"></p>
    </form>
    <!-- placeholder는 데이터를 어느곳에 저장할것인지 지정해준다 -->
  </body>
</html>
