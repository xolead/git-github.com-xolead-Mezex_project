
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