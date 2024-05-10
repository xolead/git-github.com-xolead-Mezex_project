function create_new_applic(){
    document.querySelector(".container_all_create").classList.add("active");
    document.querySelector(".main_body_create").classList.add("active");
}


function cansel_create_applic(){
    document.querySelector(".container_all_create").classList.remove("active");
    document.querySelector(".main_body_create").classList.remove("active");
}

function send_create_applic(){
    document.querySelector(".container_all_create").classList.remove("active");
    document.querySelector(".main_body_create").classList.remove("active");
}

function delete_create(event){
    window.elem = event.target.id; 
    console.log(elem)
    document.getElementById(elem).remove();
}