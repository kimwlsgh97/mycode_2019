 var Links = {
   setColor:function(color){
//     var alist = document.querySelectorAll('a');
//     var i = 0;
//
//     while(i < alist.length){
//       alist[i].style.color = color;
//       i = i + 1;
//     }
    $('a').css("color", color);
   }
}


var Body = {
  setColor:function(body, color){
    body.style.color = color;
  },
  setBackgroundColor:function(bg, color){
    bg.style.backgroundColor = color;
  }
}

function nightDayHandler(self){
  var target = document.querySelector('body');
  if(self.value === 'night'){
    Body.setBackgroundColor(target,'black');
    Body.setColor(target,'white');
    self.value = 'day';

    Links.setColor("#efefef");
  }
  else{
    Body.setBackgroundColor(target,'white');
    Body.setColor(target,'black');
    self.value = 'night';

    Links.setColor("#4a4a4a");
  }
}
