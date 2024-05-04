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
