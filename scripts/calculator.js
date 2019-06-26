function calc(num1, num2, num3, num4, num5, num6, num7, num8, num9, num0){
  // when id one is clicked, variable input1 is executed with an addEventListener
  var input1 = document.getElementById('one').addEventListener('click', function(){
    document.getElementById('calc_out').value = num1;
  });
  var input2 = document.getElementById('two').addEventListener('click', function(){
    document.getElementById('calc_out').value = num2;
  });
  var input3 = document.getElementById('three').addEventListener('click', function(){
    document.getElementById('calc_out').value = num3;
  });
  var input4 = document.getElementById('four').addEventListener('click', function(){
    document.getElementById('calc_out').value = num4;
  });
  var input5 = document.getElementById('five').addEventListener('click', function(){
    document.getElementById('calc_out').value = num5;
  });
  var input6 = document.getElementById('six').addEventListener('click', function(){
    document.getElementById('calc_out').value = num6;
  });
  var input7 = document.getElementById('seven').addEventListener('click', function(){
    document.getElementById('calc_out').value = num7;
  });
  var input8 = document.getElementById('eight').addEventListener('click', function(){
    document.getElementById('calc_out').value = num8;
  });
  var input9 = document.getElementById('nine').addEventListener('click', function(){
    document.getElementById('calc_out').value = num9;
  });
  var input0 = document.getElementById('zero').addEventListener('click', function(){
    document.getElementById('calc_out').value = num0;
  });
}
var num = calc(1,2,3,4,5,6,7,8,9,0);
