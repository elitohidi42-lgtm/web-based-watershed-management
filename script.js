//Sound with pin 1 //

var a = document.getElementById("myAudio1"); 

function playAudio() { 
  a.play(); 
} 

function pauseAudio() { 
  a.pause(); 
} 


var playing = false;
function toggleAudio1() {
  if(playing==false) {
    playing = true;
    a.play(); 
    var element = document.getElementById("tooltip-1");
    element.classList.toggle("hide");
  } else {
    playing = false;
     a.pause();
    var element = document.getElementById("tooltip-1");
    element.classList.toggle("hide");
  }
}

//Sound with pin 2 //

var b = document.getElementById("myAudio2"); 

function playAudio() { 
  b.play(); 
} 

function pauseAudio() { 
  b.pause(); 
} 


var playing = false;
function toggleAudio2() {
  if(playing==false) {
    playing = true;
    b.play(); 
    var element = document.getElementById("tooltip-2");
    element.classList.toggle("hide");
  } else {
    playing = false;
     b.pause();
    var element = document.getElementById("tooltip-2");
    element.classList.toggle("hide");
  }
}

//Sound with pin 3 //

var c = document.getElementById("myAudio3"); 

function playAudio() { 
  c.play(); 
} 

function pauseAudio() { 
  c.pause(); 
} 


var playing = false;
function toggleAudio3() {
  if(playing==false) {
    playing = true;
    c.play(); 
    var element = document.getElementById("tooltip-3");
    element.classList.toggle("hide");
  } else {
    playing = false;
     c.pause();
    var element = document.getElementById("tooltip-3");
    element.classList.toggle("hide");
  }
}

//Sound with pin 4//

var d = document.getElementById("myAudio4"); 

function playAudio() { 
  d.play(); 
} 

function pauseAudio() { 
  d.pause(); 
} 


var playing = false;
function toggleAudio4() {
  if(playing==false) {
    playing = true;
    d.play(); 
    var element = document.getElementById("tooltip-4");
    element.classList.toggle("hide");
  } else {
    playing = false;
     d.pause();
    var element = document.getElementById("tooltip-4");
    element.classList.toggle("hide");
  }
}



var canadamap = document.getElementById("khuzestan-map"),
	provinceInfo = document.getElementById("provinceInfo"),
	allProvinces = canadamap.querySelectorAll("g");
	canadamap.addEventListener("click", function(e){ 
		var province = e.target.parentNode;
		if(e.target.nodeName == "path") {
		for (var i=0; i < allProvinces.length; i++) {
			allProvinces[i].classList.remove("active");
		}
		province.classList.add("active");
		var provinceName = province.querySelector("title").innerHTML,
		provincePara = province.querySelector("desc p");
		sourceImg = province.querySelector("img"),
		imgPath = "https://s3-us-west-2.amazonaws.com/s.cdpn.io/4273/";
		provinceInfo.innerHTML = "";
		provinceInfo.insertAdjacentHTML("afterbegin", "<img src="+imgPath + sourceImg.getAttribute('xlink:href')+" alt='"+sourceImg.getAttribute('alt')+"'><h1>"+provinceName+"</h1><p>"+provincePara.innerHTML+"</p>");
		provinceInfo.classList.add("show");
		}
	})