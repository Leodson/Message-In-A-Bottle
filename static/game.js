

function reset1(){
clearTimeout(my_time);
document.getElementById('i1').style.left= "1200px";
document.getElementById('i1').style.top= "100px";
document.getElementById('i2').style.left= "400px";
document.getElementById('i2').style.top= "200px";
document.getElementById('i3').style.left= "800px";
document.getElementById('i3').style.top= "430px";
document.getElementById('i4').style.left= "340px";
document.getElementById('i4').style.top= "510px";
document.getElementById('i5').style.left= "675px";
document.getElementById('i5').style.top= "90px";
document.getElementById('i6').style.left= "600px";
document.getElementById('i6').style.top= "500px";
document.getElementById('i7').style.left= "610px";
document.getElementById('i7').style.top= "260px";
document.getElementById('i8').style.left= "1100px";
document.getElementById('i8').style.top= "300px";
document.getElementById('i9').style.left= "1500px";
document.getElementById('i9').style.top= "190px";
document.getElementById('i10').style.left= "100px";
document.getElementById('i10').style.top= "350px";
document.getElementById("msg").innerHTML="";

}



function move_img(str, id) {

  var x=document.getElementById(id).offsetTop;
  x= x +100;
  document.getElementById(id).style.top= x + "px";

}


function disp(id){
  var step=1; // Change this step value
  //alert("Hello");
  console.log(id)
  var y=document.getElementById(id).offsetTop;
  var x=document.getElementById(id).offsetLeft;
  if(y < 700){
    add = Math.random() * 20 ;
    if (Math.random() > .5) {
      add = add * -1
    }
    y= y + add;
    document.getElementById(id).style.top= y + "px"; // vertical movment
  }
  if(x < 2000){
    add = Math.random() * 20 ;
    if (Math.random() > .5) {
      add = add * -1
    }
    x= x + add;
    document.getElementById(id).style.left= x + "px"; // horizontal movment
  }
}
function startGame(){
  animationFrame()
  startTimer()
  document.getElementById("music").play()
}
function animationFrame() {
  disp('i1')
  disp('i2')
  disp('i3')
  disp('i4')
  disp('i5')
  disp('i6')
  disp('i7')
  disp('i8')
  disp('i9')
  disp('i10')
  my_time=setTimeout('animationFrame()',10);
}
function startTimer() {
  var timeleft = 10;
  var downloadTimer = setInterval(function(){
    document.getElementById("countdown").innerHTML = timeleft + " SECONDS REMAINING";
    timeleft -= 1;
    if(timeleft <= 0){
      clearInterval(downloadTimer);
      document.getElementById("countdown").innerHTML = "TIME IS UP!"
      reset1()
    }
  }, 1000);
}
