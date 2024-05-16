function post_t(){
    var loc_url = window.localStorage.getItem('urls')
    if  ( loc_url != "0")
    {
        var loc_url = window.localStorage.getItem('urls')
        console.log(loc_url)
        document.querySelector(".iframe").innerHTML = "<iframe src=" + loc_url+  " style='width:100%; height:100%;' frameborder='0'></iframe>"
        console.log("<iframe src=" + loc_url+  "style='width:100%; height:100%;' frameborder='0'></iframe>")
        window.localStorage.setItem("urls", "0")
    }
    else
    {
        var offer_url = window.localStorage.getItem('offer_urls')
        console.log(offer_url)
        document.querySelector(".iframe").innerHTML = "<iframe src=" + offer_url +  " style='width:100%; height:100%;' frameborder='0'></iframe>"
        console.log("<iframe src=" + offer_url+  "style='width:100%; height:100%;' frameborder='0'></iframe>")
    }
}


window.setTimeout(post_t,10)


function get_id_sort(event){
    var dnd = document.querySelector('#dnd');

    var logSelected = function () {
    console.log(dnd.selectedIndex);
    };

    logSelected();
    dnd.addEventListener('change', logSelected);

    if (dnd.selectedIndex == "0"){
        filterSelection("all")
    }  

    if (dnd.selectedIndex == "1"){
        filterSelection("time")
    }  

    if (dnd.selectedIndex == "2"){
        filterSelection("odob")
    }  
    
    if (dnd.selectedIndex == "3"){
        filterSelection("otkaz")
    }  
}

function filterSelection(c) {
  var x, i;
  x = document.getElementsByClassName("filterDiv");
  if (c == "all") c = "";
  // Добавить класс "show" (display:block) к отфильтрованным элементам и удалите класс "show" из элементов, которые не выбраны
  for (i = 0; i < x.length; i++) {
    w3RemoveClass(x[i], "show");
    if (x[i].className.indexOf(c) > -1) w3AddClass(x[i], "show");
  }
}

// Показать отфильтрованные элементы
function w3AddClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    if (arr1.indexOf(arr2[i]) == -1) {
      element.className += " " + arr2[i];
    }
  }
}

// Скрыть элементы, которые не выбраны
function w3RemoveClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    while (arr1.indexOf(arr2[i]) > -1) {
      arr1.splice(arr1.indexOf(arr2[i]), 1);
    }
  }
  element.className = arr1.join(" ");
}

window.onload = function() {
    filterSelection("all")
}