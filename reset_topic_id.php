<?php
  $conn = mysqli_connect("127.0.0.1","root","KJHwhsgh1!","think");
  if(mysqli_connect_errno()) {
    printf("로그인에 실패하셨습니다. : %s\n",mysqli_connect_error());
    exit();
  }

  $sql = "ALTER TABLE topic AUTO_INCREMENT=1;";
  $sql .= "SET @COUNT = 0;";
  $sql .= "UPDATE topic SET id = @COUNT:=@COUNT+1;";
  $result = mysqli_multi_query($conn,$sql);
  if($result === false){
    echo '초기화 과정에서 문제가 생겼습니다. 관리자에게 문의해주세요';
    error_log(mysqli_error($conn));
  }
  else {
    header('Location: index.php');
  }
?>
