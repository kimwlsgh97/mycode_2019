<?php
  $conn = mysqli_connect('127.0.0.1','root','KJHwhsgh1!');
  if(mysqli_connect_errno()){
    printf("로그인 정보가 올바르지 않습니다.");
    die(mysqli_connect_error());
  }

  $sql = "CREATE TABLE author(
    id INT(11) unsigned NOT NULL,
    author VARCHAR(30) NULL,
    profile VARCHAR(100) NULL,
    PRIMARY KEY(id)
  );"
  mysqli_query
 ?>
