function select_menu(option){
		document.getElementById("dashboard").className =  ""
		document.getElementById("user").className =  ""
		document.getElementById("profile").className =  ""
		document.getElementById("institutions").className =  ""
		document.getElementById("establishment").className =  ""
		document.getElementById("national").className =  ""
		document.getElementById("international").className =  ""
		document.getElementById("poll").className =  ""
		document.getElementById("medicine").className =  ""
		document.getElementById("history").className =  ""
		document.getElementById("td").className =  ""
		document.getElementById("observation").className =  ""
		document.getElementById("state").className =  ""

		document.getElementById(option).className +=  "active"
		if (option=='establishment' || option=='institutions' ||  option=='national' || option=='international') {
			document.getElementById("submenu_1").style.display ="block"
		}
}
 

function view_modal(){
	document.getElementById('myModal').className +=  " active"
	}