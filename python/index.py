#!C:\Python27\python.exe
#-*- coding:utf-8 -*-
print("content-type: text/html; charset=utf-8\n")
print('''
<!doctype html>
<html>
<head>
    <title>{title1}</title>
    <meta name="description" content="인터넷상 사람들의 주요한 관심사가 무엇인지 알수있도록 하는 페이지">
    <meta name="keywords" content="people, attention, data">
    <meta name="author" content="MindHunt">
    <link rel="stylesheet" href="style.css">
    <link href="https://fonts.googleapis.com/css?family=Nanum+Gothic&display=swap&subset=korean" rel="stylesheet">
    <link rel="shortcut icon" type="image⁄x-icon" href="title.jpg">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="colors.js"></script>
</head>

<body>
  <h1><a href="index.py">{title1}</a></h1>
  <h2>[ {title2} ]</h2>
  <div id = "main_menu">
    <h3><a href="article.py?id=방향">방향</a></h3>
    <h3><a href="article.py?id=방법">방법</a></h3>
    <h3><a href="article.py?id=본질">본질</a></h3>
  </div>
<body>
''').format(title1='순위의모든것',title2='소셜랭킹')
