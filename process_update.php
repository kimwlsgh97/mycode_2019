<?php
  $conn = mysqli_connect("127.0.0.1","root","KJHwhsgh1!","think");
  if(mysqli_connect_errno()) {
    //마지막 연결 호출에서 발생한 오류코드를 가지고 있다. 없을땐 false
    printf("로그인에 실패하셨습니다. : %s\n",mysqli_connect_error());
    exit(); //php문 탈출 = die('~~');
  }

  settype($_POST['id'], "integer");
  //$_POST['id']를 정수로 바꾸어준다.
  $filtered = array(
    'id'=>mysqli_real_escape_string($conn, $_POST['id']),
    'title'=>mysqli_real_escape_string($conn, $_POST['title']),
    //$_POST를 가져와서 문자열로 변경하는 작업, mysqli를 이용하므로 로그인이 선행되어야함!
    'description'=>mysqli_real_escape_string($conn, $_POST['description'])
    //$_POST에서 받아온 정보를 어디에 저장할것인지 지정
  );

    $sql = "
      UPDATE topic
      SET
        title='{$filtered['title']}',
        description='{$filtered['description']}'
      WHERE id={$filtered['id']}
    ";
        //filtered 배열의 정보를 sql문의 밸류로 사용할때는, {}로 묶는다.

    //$result=mysqli_query($conn,$sql);
    $result=mysqli_query($conn,$sql);

    if($result === false){
      echo '수정하는 과정에서 문제가 생겼습니다. 관리자에게 문의해주세요';
      error_log(mysqli_error($conn));
      //mysqli_error는 가장 최근에 발생한 에러내용을 가지고 있다.
    }
    else {
      echo '수정했습니다. <a href="index.php">돌아가기</a>';
    }
 ?>
