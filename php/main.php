<!DOCTYPE html>
<html>
  <head>
    <title>무엇을 원해?</title>
  </head>
  <body>
    <h1>무엇을 원해?</h1>
    <ol>
      <li><a href="main.php?title=chaos">혼돈</a></li>
      <li><a href="main.php?title=rule">질서</a></li>
    </ol>
    <?php
      echo $_GET['title']
     ?>
  </body>
</html>
