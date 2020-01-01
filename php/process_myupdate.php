<?php
  $conn = mysqli_connect("127.0.0.1","root","KJHwhsgh1!","think");
  if(mysqli_connect_errno()) {
    printf("로그인에 실패하셨습니다. : %s\n",mysqli_connect_error());
    exit();
  }

    $filtered = array(
      'id'=>mysqli_real_escape_string($conn, $_GET['id']),
      'title'=>mysqli_real_escape_string($conn, $_POST['title']),
      //$_POST를 가져와서 문자열로 변경하는 작업, mysqli를 이용하므로 로그인이 선행되어야함!
      'description'=>mysqli_real_escape_string($conn, $_POST['description'])
      //$_POST에서 받아온 정보를 어디에 저장할것인지 지정
    );
    //

    $sql = "
    UPDATE topic
    SET title='{$filtered['title']}',description='{$filtered['description']}'
    WHERE id={$filtered['id']}
    ";
        //filtered 배열의 정보를 sql문의 밸류로 사용할때는, {}로 묶는다.

    //$result=mysqli_query($conn,$sql);
    $result=mysqli_query($conn,$sql);

    if($result === false){
      echo '수정하는 과정에서 문제가 생겼습니다. 관리자에게 문의해주세요';
      error_log(mysqli_error($conn));
    }
    else {
      echo '성공했습니다. <a href="index.php">돌아가기</a>';
    }
 ?>
