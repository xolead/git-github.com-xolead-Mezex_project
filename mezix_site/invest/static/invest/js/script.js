function opense() {
    if  (document.getElementById("popup").style.zIndex=="1") 
    {
        document.getElementById("button-block-applications").style.marginRight = "-8px";
        document.getElementById("popup").style.zIndex = "-1";
        document.getElementById("strelka-vlevo").style.rotate = "90deg";
        document.getElementById("strelka-vlevo").style.marginLeft = "0px";
    }
        
    else 

    {
        document.getElementById("button-block-applications").style.marginRight = "365px";
        document.getElementById("popup").style.zIndex = "1";
        document.getElementById("strelka-vlevo").style.rotate = "270deg";
        document.getElementById("strelka-vlevo").style.marginLeft = "2px";
    }
}
