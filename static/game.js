

function reset1(){
clearTimeout(my_time);
document.getElementById('i1').style.left= "500px";
document.getElementById('i1').style.top= "100px";
document.getElementById('i2').style.left= "500px";
document.getElementById('i2').style.top= "200px";
document.getElementById('i3').style.left= "500px";
document.getElementById('i3').style.top= "200px";
document.getElementById('i4').style.left= "500px";
document.getElementById('i4').style.top= "200px";
document.getElementById('i5').style.left= "500px";
document.getElementById('i5').style.top= "200px";
document.getElementById('i6').style.left= "500px";
document.getElementById('i6').style.top= "200px";
document.getElementById('i7').style.left= "500px";
document.getElementById('i7').style.top= "200px";
document.getElementById('i8').style.left= "500px";
document.getElementById('i8').style.top= "200px";
document.getElementById('i9').style.left= "500px";
document.getElementById('i9').style.top= "200px";
document.getElementById('i10').style.left= "500px";
document.getElementById('i10').style.top= "200px";
document.getElementById("msg").innerHTML="";

}



function move_img(str, id) {

  var x=document.getElementById(id).offsetTop;
  x= x +100;
  document.getElementById(id).style.top= x + "px";

}


function disp(id){
  var step=2; // Change this step value
  //alert("Hello");
  console.log(id)
  var y=document.getElementById(id).offsetTop;
  var x=document.getElementById(id).offsetLeft;
  if(y < 470 ){
    add = Math.random() * 30 ;
    if (Math.random() > .5) {
      add = add * -1
    }
    y= y + add;
    document.getElementById(id).style.top= y + "px"; // vertical movment
  }
  if(x < 1200){
    add = Math.random() * 30 ;
    if (Math.random() > .5) {
      add = add * -1
    }
    x= x + add;
    document.getElementById(id).style.left= x + "px"; // horizontal movment
  }
}

function timers() {
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
  my_time=setTimeout('timers()',10);
}
