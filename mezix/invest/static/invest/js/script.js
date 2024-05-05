function opense() {
    if  (document.getElementById("popup").style.zIndex=="1") 
    {
        document.getElementById("button-block-applications").style.marginRight = "-8px";
        document.getElementById("popup").style.zIndex = "-1";
        document.getElementById("strelka-vlevo").style.rotate = "360deg";
    }
        
    else 

    {
        document.getElementById("button-block-applications").style.marginRight = "365px";
        document.getElementById("popup").style.zIndex = "1";
        document.getElementById("strelka-vlevo").style.rotate = "180deg";
    }
}

window.pre_elem = "0"

function get_id_delete(event){
    window.elem = event.target.id; 
    document.getElementById(elem).style.cursor = "default";

    if  (document.getElementById("popup").style.zIndex=="-1")
    {
        document.getElementById("button-block-applications").style.marginRight = "365px";
        document.getElementById("popup").style.zIndex = "1";
        document.getElementById("strelka-vlevo").style.rotate = "180deg";
    }

    if (pre_elem != elem)
    {   
        if (pre_elem != "0"){
            document.getElementById(pre_elem).style.cursor = "pointer";
            document.getElementById(elem).style.cursor = "default";
        }
    }

    pre_elem = elem;
    return elem
}

function deletes() {
    document.getElementById(elem).remove();
    pre_elem = "0"
}