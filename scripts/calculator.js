function clear(value){
	document.getElementById('calc_out').value=value;
}

function add_val(value){
	document.getElementById('calc_out').value+=value;
	console.log('you have entered ' + value);
}

function ev(){
	try{ 
		clear(eval(document.getElementById('calc_out').value)) 
	} 
	catch(ev) {
	  clear('Error') 
		} 
}

