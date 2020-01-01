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
              <td><a href="process_delete_author.php?id=<?=$filtered['id']?>">delete</a></td>
            </tr>
            <?php
          }
         ?>
      </tr>
    </table>
    <form class="" action="process_create_author.php" method="post">
      <p><input type="text" name="name" placeholder="name"></p>
      <p><textarea name="profile" placeholder="profile"></textarea></p>
      <!-- placehoder는 검색창이나 텍스트창안에 설명을 붙여준다 -->
      <p><input type="submit" value="Create author"></p>
    </form>
  </body>
</html>
