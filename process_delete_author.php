<?php
  $conn = mysqli_connect("127.0.0.1","root","KJHwhsgh1!","think");
  if(mysqli_connect_errno()) {
    printf("로그인에 실패하셨습니다. : %s\n",mysqli_connect_error());
    exit();
  }

    $filtered_id = mysqli_real_escape_string($conn, $_POST['id']);


    $sql = "
    DELETE FROM author
    WHERE id={$filtered_id}
    ";
    $result=mysqli_query($conn,$sql);

    if($result === false){
      echo '삭제하는 과정에서 문제가 생겼습니다. 관리자에게 문의해주세요';
      error_log(mysqli_error($conn));
    }
    else {
      header('Location: author.php');
    }
 ?>
