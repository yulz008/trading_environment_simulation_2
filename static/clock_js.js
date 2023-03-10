const secDiv = document.getElementById('sec');
const minDiv = document.getElementById('min');
const hourDiv = document.getElementById('hour');

setInterval(updateClock, 1000);



function updateClock(){

	//get simulation_current time
    var dateTimeString = document.getElementById("simulation_time").innerHTML;

    // Use the JavaScript Date object to parse the date and time input
    var dateTime = new Date(dateTimeString);

    // Convert the date and time to a timestamp in milliseconds
    var timestamp1 = dateTime.getTime();
    //alert(timestamp1);

	let date = new Date(timestamp1);
	let sec = date.getSeconds() / 60;
	let min = (date.getMinutes() + sec) / 60;
	let hour = (date.getHours() + min) / 12;

	//secDiv.style.transform = "rotate(" + (sec * 360) + "deg)";
	minDiv.style.transform = "rotate(" + (min * 360) + "deg)";
	hourDiv.style.transform = "rotate(" + (hour * 360) + "deg)";
}

updateClock();