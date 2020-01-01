<?php
  $conn = mysqli_connect("127.0.0.1","root","KJHwhsgh1!","think");
  if(mysqli_connect_errno()) {
    printf("로그인에 실패하셨습니다. : %s\n",mysqli_connect_error());
    exit();
  }

  $sql_author = "SELECT * FROM author";
  $result = mysqli_query($conn, $sql_author);
  while($row = mysqli_fetch_array($result)){
    //<li><a href="index.php?id=11">MySQL</a></li>
    $escaped_in_author = htmlspecialchars($row['author']);
    $list = $list."<li><a href=\"index.php?id={$row['id']}\">$escaped_in_author</a></li>";
    // $desc = $desc.$row['description']; -- 리스트형식으로 표현하는게 아니라 특정링크마다 다르게
  }; //---mysqli_fetch_array가 직접실행되어야 늘어남, $row는 불가능

  $article = array(
    'name'=>'anonymous',
    'profile'=>'blank'
  );

  if(isset($_GET['id'])){
    $filtered_id = mysqli_real_escape_string($conn, $_GET['id']);
    $select_id_row = "SELECT * FROM author WHERE id={$filtered_id}";
    $result = mysqli_query($conn, $select_id_row);
    $row = mysqli_fetch_array($result);
    // $title = $row['title'];
    // $article = $row['description'];
    $escaped_out_name = htmlspecialchars($row['name']);
    $escaped_out_profile = htmlspecialchars($row['profile']);
    $article['name'] = $escaped_out_name;
    $article['profile'] = $escaped_out_profile;
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
    <p><a href="index.php">topic</a></p>
    <table border="1">
      <tr>
        <td>id</td><td>name</td><td>profile</td><td></td><td></td>
        <?php
          $sql = "SELECT * FROM author";
          $result = mysqli_query($conn, $sql);
          while($row = mysqli_fetch_array($result)){
            $filtered = array(
              'id'=>htmlspecialchars($row['id']),
              'name'=>htmlspecialchars($row['name']),
              'profile'=>htmlspecialchars($row['profile'])
            );
            ?>
            <tr>
              <td><?=$filtered['id']?></td>
              <td><?=$filtered['name']?></td>
              <td><?=$filtered['profile']?></td>
              <td><a href="update_author.php?id=<?=$filtered['id']?>">update</a></td>
              <td><a href="delete_author.php?id=<?=$filtered['id']?>">delete</a></td>
            </tr>
            <?php
          }
         ?>
      </tr>
    </table>
    <form action="process_update_author.php" method="post">
      <input type="hidden" name="id" value="<?=$filtered_id?>">
      <!-- 눈에 보이지않게 정보를 전송 -->
      <p><input type="text" name="name" placeholder="name" value="<?=$article['name']?>"></p>
      <!-- placeholder="title" : 여기서 입력받은 정보를 title이라는 이름으로 내보낸다 -->
      <p><textarea name="profile" placeholder="profile"><?=$article['profile']?></textarea></p>
      <!-- <textarea>내용</textarea> 으로 텍스트영역안에 글을 표시할수 있다 -->
      <p><input type="submit" value="Update"></p>
    </form>
  </body>
</html>
