// var headerHeight = document.getElementById('header').getAttribute("height");
// document.getElementById('empty').setAttribute("min-height", headerHeight);
// emptyDiv.css("height", headerHeight);

// var headerHeight = document.getElementById('header').style.height;
var rect = document.getElementById('header').getBoundingClientRect();
var headerHeight = rect.height;
var emptyDiv = document.getElementById('empty');
emptyDiv.style.marginTop=String(headerHeight)+"px";

window.onresize = movePageTitleDiv;

function movePageTitleDiv(){
    var rect = document.getElementById('sidebar').getBoundingClientRect();
    var width = rect.width;
    var left = rect.left;
    var move = width + left;
    var pageTitle = document.getElementById('pagetitle');
    pageTitle.style.marginLeft=String(move)+"px";
}
