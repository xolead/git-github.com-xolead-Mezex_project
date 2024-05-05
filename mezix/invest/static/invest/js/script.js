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
    document.getElementById(elem).style.cssText = "cursor: default; background-color:#21CC4E;"
        
   // if  (document.getElementById("popup").style.zIndex=="-1")
    //{

    //открытие блока
        document.getElementById("button-block-applications").style.marginRight = "365px";
        document.getElementById("popup"+ elem).style.zIndex = "1";
        document.getElementById("strelka-vlevo").style.rotate = "180deg";
    //}

    if (pre_elem != elem)
    {   
        if (pre_elem != "0"){
            document.getElementById(pre_elem).style.cursor = "pointer";

            var found = document.querySelectorAll(".tr-white:nth-child(2n+1)")
            for (x of found){
                if (x.id == pre_elem){
                    document.getElementById(pre_elem).style.cssText = "cursor: pointer; background-color:#ffffff;"
                    document.getElementById("popup"+ pre_elem).style.zIndex = "-1";
                }
                else{
                    document.getElementById(pre_elem).style.cssText = "cursor: pointer; background-color:##EEF4EA;"
                    document.getElementById("popup"+ pre_elem).style.zIndex = "-1";
                }
            }
            
        }
    }

    pre_elem = elem;
    return elem
}

function deletes() {
    document.getElementById(elem).remove();
    document.getElementById("button-block-applications").style.marginRight = "-8px";
    document.getElementById("popup"+elem).style.zIndex = "-1";
    document.getElementById("strelka-vlevo").style.rotate = "360deg";
    pre_elem = "0"
   
}

// var aboba = document.querySelectorAll(".tr-white:nth-child(2n+1)")
// for (x of aboba) console.log(x.id)