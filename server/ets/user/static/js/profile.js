// var headerHeight = document.getElementById('header').getAttribute("height");
// document.getElementById('empty').setAttribute("min-height", headerHeight);
// emptyDiv.css("height", headerHeight);

// var headerHeight = document.getElementById('header').style.height;

window.onload = function(){
    var rect = document.getElementById('header').getBoundingClientRect();
    var headerHeight = rect.height;
    var emptyDiv = document.getElementById('empty');
    emptyDiv.style.marginTop=String(headerHeight)+"px";

    moveElements();
}

window.onresize = moveElements;

function moveElements(){
    var rect = document.getElementById('sidebar').getBoundingClientRect();
    var width = rect.width;

    var windowWidth = document.body.clientWidth;
    if(windowWidth<1200){
        var move = 20;
    }
    else{
        var move = width + 20;
    }

    var pageTitle = document.getElementById('pagetitle');
    pageTitle.style.marginLeft=String(move)+"px";
    var profilesection = document.getElementById('profile-section');
    profilesection.style.marginLeft=String(move)+"px";
}
