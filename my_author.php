<?php
  $conn = mysqli_connect("127.0.0.1","root","KJHwhsgh1!","think");
  if(mysqli_connect_errno()) {
    printf("로그인에 실패하셨습니다. : %s\n",mysqli_connect_error());
    exit();
  }

  $author = "SELECT * FROM author";
  $result = mysqli_query($conn,$author);
  $table_form = '<table><tr><td>name</td><td>profile</td>';
  while($row = mysqli_fetch_array($result)){
    $table_form .= '<th>'.$row['name'].'</th><th>'.$row['profile'].'</th><';
  };
  $table_form .= '</tr></table>';
}
 ?>

 <!DOCTYPE html>
 <html>
   <head>
     <meta charset="utf-8">
     <title></title>
   </head>
   <body>
     <h1>author</h1>
     <?=$table_form?>
   </body>
 </html>
