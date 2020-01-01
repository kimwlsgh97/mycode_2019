<?php
  $conn = mysqli_connect("127.0.0.1","root","KJHwhsgh1!","think");
  if(mysqli_connect_errno()) {
    printf("로그인에 실패하셨습니다. : %s\n",mysqli_connect_error());
    exit();
  }

  $topic = "SELECT * FROM topic";
  $result = mysqli_query($conn, $topic);
  while($row = mysqli_fetch_array($result)){
    $escaped_in_title = htmlspecialchars($row['title']); //태그 명령어를 문자열로 인식
    //<li><a href="index.php?id=11">MySQL</a></li>
    $list = $list."<li><a href=\"index.php?id={$row['id']}\">$escaped_in_title</a></li>";
    // $desc = $desc.$row['description']; -- 리스트형식으로 표현하는게 아니라 특정링크마다 다르게
  }; //---mysqli_fetch_array가 직접실행되어야 늘어남, $row는 불가능

  $article = array(
    'title'=>'Welcome',
    'description'=>'Hello, web'
  );

  $update_link = '';
  $delete_link = '';
  $author = '';
  if(isset($_GET['id'])){
    //url파라미터를 이용한 정보가져오기 : get방식
    $filtered_id = mysqli_real_escape_string($conn, $_GET['id']);
    $select_id = "SELECT * FROM topic LEFT JOIN author ON topic.author_id = author.id WHERE topic.id={$filtered_id}";
    //WHERE id={filtered_id} 로 지정하여도 문법에따라 먼저나온 것의 id값을 따라가나?
    //아니면 id값이 겹치지 않아서 오류없이 실행되는것인가?
    $result2 = mysqli_query($conn, $select_id);
    $row2 = mysqli_fetch_array($result2);
    // $title = $row2['title'];
    // $article = $row2['description'];
    $escaped_out_title = htmlspecialchars($row2['title']);
    $escaped_out_description = htmlspecialchars($row2['description']);
    $escaped_out_name = htmlspecialchars($row2['name']);
    $article['title'] = $escaped_out_title;
    $article['description'] = $escaped_out_description;
    $article['name'] = $escaped_out_name;

    $update_link = '<a href="update.php?id='.$filtered_id.'">update</a>';
    // $delete_link = '<a href="process_delete.php?id='.$filtered_id.'">delete</a>';
    $delete_link = '
    <form action="process_delete.php" method="post">
      <input type="hidden" name="id" value="'.$_GET['id'].'">
      <input type="submit" value="delete">
    </form>
    ';
    //폼형식으로 정보를 전달하면, 링크를 복사해서 다른곳으로 유포되는 등, 목적에 맞지않게 사용되는 경우방지
    $author = "<p>by {$article['name']}</p>";
    //중괄호가 들어가야지만 작동 - 왜 그런지는 아직 모름
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
    <p><a href="author.php">author</a></p>
    <p><a href="reset_topic_id.php">reset</a></p>
    <ol>
      <?=$list?>
     </ol>
    <a href="create.php">create</a>
    <?=$update_link?>
    <?=$delete_link?>
    <h2>
      <?=$article['title']?>
    </h2>
      <?=$article['description']?>
      <?=$author?>
      <!-- php변수 내용을 출력할때, -->
  </body>
</html>
