<?php
  $conn = mysqli_connect("127.0.0.1","root","KJHwhsgh1!","think");
  if(mysqli_connect_errno()) {
    printf("로그인에 실패하셨습니다. : %s\n",mysqli_connect_error());
    exit();
  }

    $filtered_id = mysqli_real_escape_string($conn, $_POST['id']);


    $sql = "
    DELETE FROM topic
    WHERE id={$filtered_id}
    ";
        //filtered 배열의 정보를 sql문의 밸류로 사용할때는, {}로 묶는다.

    //$result=mysqli_query($conn,$sql);
    $result=mysqli_query($conn,$sql);

    if($result === false){
      echo '삭제하는 과정에서 문제가 생겼습니다. 관리자에게 문의해주세요';
      error_log(mysqli_error($conn));
    }
    else {
      echo '삭제했습니다. <a href="index.php">돌아가기</a>';
    }
 ?>
