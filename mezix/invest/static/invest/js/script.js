function opense() {
    if  (document.getElementById("popup"+elem).style.zIndex=="1") 
    {
        document.getElementById("button-block-applications").style.marginRight = "-8px";
        document.getElementById("popup"+elem).style.zIndex = "-1";
        document.getElementById("strelka-vlevo").style.rotate = "360deg";
    }
        
    else 

    {
        document.getElementById("button-block-applications").style.marginRight = "365px";
        document.getElementById("popup" +elem).style.zIndex = "1";
        document.getElementById("strelka-vlevo").style.rotate = "180deg";
    }
}

window.pre_elem = "0"

function get_id_delete(event){
    window.elem = event.target.id; 

    console.log(elem)

    document.getElementById(elem).classList.add('click_now');
        
        document.getElementById("button-block-applications").style.marginRight = "365px";
        document.getElementById("popup"+ elem).style.zIndex = "1";
        document.getElementById("strelka-vlevo").style.rotate = "180deg";


    if (pre_elem != elem)
    {   
        if (pre_elem != "0"){

            document.getElementById(pre_elem).classList.remove('click_now');
            document.getElementById("popup" +pre_elem).style.zIndex = "-1";
        }
    }
    pre_elem = elem;
    
    return elem
}

function deletes() {
    document.getElementById(elem).remove();
    document.getElementById("popup" + elem).remove();
    document.getElementById("button-block-applications").style.marginRight = "-8px";
    document.getElementById("strelka-vlevo").style.rotate = "360deg";
    pre_elem = "0"
    //всегда в конце
    document.getElementById("popup" +elem).style.zIndex = "-1";
}

function info(){
    window.localStorage.setItem("urls", "'/static/invest/"+elem+".pdf'")
}

function offers(event){
    window.aboba = event.target.id; 
    window.localStorage.setItem("offer_urls", "'/static/invest/"+aboba+".pdf'")
}

function accept(){
    var modal = document.querySelector('.container-modal');
    
    modal.classList.remove("active");
        document.querySelector(".overlay_for_buttons").classList.remove('active');
        document.querySelector(".th-white").classList.remove('active');
        document.querySelector(".section-container-applications").classList.remove('active');
        var tr_all = document.querySelectorAll(".tr-white");

        for (var i = 0, tr_each; (tr_each = tr_all[i]); i++){
            tr_each.classList.remove('active');
    }

    document.getElementById(elem).remove();
    document.getElementById("popup" + elem).remove();
    document.getElementById("button-block-applications").style.marginRight = "-8px";
    document.getElementById("strelka-vlevo").style.rotate = "360deg";
    pre_elem = "0"
    document.getElementById("popup" +elem).style.zIndex = "-1";
}

function btn(){
    var modal = document.getElementById('modal' + elem );
    console.log(modal)

    document.querySelector(".overlay_for_buttons").classList.add('active');
    


    modal.classList.add("active");

    document.querySelector(".section-container-applications").classList.add('active');
    document.querySelector(".th-white").classList.add('active');

    var tr_all = document.querySelectorAll(".tr-white");

    for (var i = 0, tr_each; (tr_each = tr_all[i]); i++){
        tr_each.classList.add('active');
    }

    document.getElementById(elem).classList.remove('active');
    pre_elem = elem;
    
}

function btn_close(){
    var modal = document.getElementById('modal' + elem );
    
    modal.classList.remove("active");
        document.querySelector(".overlay_for_buttons").classList.remove('active');
        document.querySelector(".th-white").classList.remove('active');
        document.querySelector(".section-container-applications").classList.remove('active');
        var tr_all = document.querySelectorAll(".tr-white");

        for (var i = 0, tr_each; (tr_each = tr_all[i]); i++){
            tr_each.classList.remove('active');
    }

}

window.onclick = function (event) {
    var modal = document.getElementById('modal' + elem )
    modal_out = document.querySelector('.overlay_for_buttons')
    if (event.target == modal_out) {
        modal.classList.remove("active");
        document.querySelector(".overlay_for_buttons").classList.remove('active');
        document.querySelector(".th-white").classList.remove('active');
        document.querySelector(".section-container-applications").classList.remove('active');
        var tr_all = document.querySelectorAll(".tr-white");

        for (var i = 0, tr_each; (tr_each = tr_all[i]); i++){
            tr_each.classList.remove('active');
    }
    }
}