function openTab(event, tabName) {
    var i, conteudobotao, button;
    
    conteudobotao = document.getElementsByClassName("conteudobotao");
    for (i = 0; i < conteudobotao.length; i++) {
        conteudobotao[i].style.display = "none";
    }
    
    button = document.getElementsByClassName("button");
    for (i = 0; i < button.length; i++) {
        button[i].className = button[i].className.replace(" active", "");
    }
    
    document.getElementById(tabName).style.display = "block";
    event.currentTarget.className += " active";
}
