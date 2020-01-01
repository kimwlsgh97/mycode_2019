<?php
  $conn = mysqli_connect("127.0.0.1","root","KJHwhsgh1!","think");
  if(mysqli_connect_errno()) {
    printf("로그인에 실패하셨습니다. : %s\n",mysqli_connect_error());
    exit();
  }

    $filtered = array(
      'name'=>mysqli_real_escape_string($conn, $_POST['name']),
      //$_POST를 가져와서 문자열로 변경하는 작업, mysqli를 이용하므로 로그인이 선행되어야함!
      'profile'=>mysqli_real_escape_string($conn, $_POST['profile'])
      //$_POST에서 받아온 정보를 어디에 저장할것인지 지정
    );
    //

    $sql = "
    INSERT INTO author
      (name, profile)
    VALUES(
      '{$filtered['name']}',
      '{$filtered['profile']}'
        )";

    //$result=mysqli_query($conn,$sql);
    $result=mysqli_query($conn,$sql);
    // php안에서 sql문 실행
    if($result === false){
      echo '저장하는 과정에서 문제가 생겼습니다. 관리자에게 문의해주세요';
      error_log(mysqli_error($conn));
    }
    else {
      header('Location: author.php');
      // 리다이렉션
    }
 ?>
