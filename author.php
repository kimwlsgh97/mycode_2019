<?php
  $conn = mysqli_connect("127.0.0.1","root","KJHwhsgh1!","think");
  if(mysqli_connect_errno()) {
    printf("로그인에 실패하셨습니다. : %s\n",mysqli_connect_error());
    exit();
  }

  $article = array(
    'name'=>'',
    'profile'=>''
  );
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
    <p><a href="reset_author_id.php">reset</a></p>
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
              <td><a href="author.php?id=<?=$filtered['id']?>">update</a></td>
              <td>
                <form action="process_delete_author.php" method="post" onsubmit="if(!confirm('정말 삭제하시겠습니까?')){return false;}">
                  <input type="hidden" name="id" value="<?=$filtered['id']?>">
                  <input type="submit" value="delete">
                </form>
              </td>
            </tr>
          <?php } ?>
      </tr>
    </table>
    <?php
      $lable_submit = 'Create author';
      $form_action = 'process_create_author.php';
      $form_hidden = '';
      if(isset($_GET['id'])){
        $filtered_id = mysqli_real_escape_string($conn, $_GET['id']);
        settype($filtered_id, 'integer');
        $sql_select_id = "SELECT * FROM author WHERE id={$filtered_id}";
        $result2 = mysqli_query($conn, $sql_select_id);
        $row2 = mysqli_fetch_array($result2);
        $escaped_out_name = htmlspecialchars($row2['name']);
        $escaped_out_profile = htmlspecialchars($row2['profile']);
        $article['name'] = $escaped_out_name;
        $article['profile'] = $escaped_out_profile;
        $lable_submit = 'Update author';
        $form_action = 'process_update_author.php';
        $form_hidden = '<input type="hidden" name="id" value="'.$filtered_id.'">';
      }
     ?>
    <form action="<?=$form_action?>" method="post">
      <?=$form_hidden?>
      <p><input type="text" name="name" placeholder="name" value="<?=$article['name']?>"></p>
      <p><textarea name="profile" placeholder="profile"><?=$article['profile']?></textarea></p>
      <!-- textarea의 태그로 문자열을 감싸면, 그 문자열을 텍스트박스안에 출력한다 -->
      <p><input type="submit" value="<?=$lable_submit?>"></p>
    </form>
  </body>
</html>
