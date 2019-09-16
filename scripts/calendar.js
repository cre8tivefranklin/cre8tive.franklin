function cal(){
	
}

var d = new Date();//global
var n = d.getDate();//global
var day;//global
var month;//global
var daily_msg;

window.onload = function() {
	switch (new Date().getDay()) {
		case 0:
			day = "Sunday";
			daily_msg = "Hello World"
		break;
		case 1:
			day = "Monday";
			daily_msg = "Who has the Monday blues?";
		break;
		case 2:
			day = "Tuesday";
			daily_msg = "Yaay! It's Tuesday!!"
		break;
		case 3:
			day = "Wednesday";
			daily_msg = "Happy hump day";
		break;
		case 4:
			day = "Thursday";
			daily_msg = "Thirsty Thursday!!"
		break;
		case 5:
			day = "Friday";
			daily_msg = "TGIF!!!"
		break;
		case 6:
			day = "Saturday";
			daily_msg = "Party time!!"
	}
	
	switch (new Date().getMonth()) {
		case 0:
			month = "January";
		break;
		case 1:
			month = "February";
		break;
		case 2:
			month = "March";
		break;
		case 3:
			month = "April";
		break;
		case 4:
			month = "May";
		break;
		case 5:
			month = "June";
		break;
		case 6:
			month = "July";
		break;		
		case 7:
			month = "August";
		case 8:
			month = "September";
		break;
		case 9:
			month = "October";
		break;
		case 10:
			month = "November";
		break;
		case 11:
			month = "December";

	}
	
	document.getElementById('msg').innerHTML = daily_msg;
	document.getElementById('da').innerHTML = n;
	document.getElementById('d').innerHTML = day;
	document.getElementById('m').innerHTML = month;
}
	