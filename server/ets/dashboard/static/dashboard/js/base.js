document.getElementById('toggle-sidebar-btn').onclick = toggleFunc;

function toggleFunc(){
    var rect = document.getElementById('sidebar').getBoundingClientRect();
    var width = rect.width;
    var strWidth = String(width)+"px";
    // alert(String(rect.style.marginLeft));

    var target = document.getElementById("sidebar");
    var style= window.getComputedStyle(target) || target.currentStyle
    var strMarginLeft = String(style.marginLeft)
    // if(strMarginLeft=="0px" || strMarginLeft==strWidth ){
    // target.style.display="None";

    var val = target.classList.toggle("toggle-temp");
    if(val){
        target.style.marginLeft="-"+strWidth;
    }
    else{
        var windowWidth = document.body.clientWidth;
        target.style.left="-"+strWidth;
        target.style.marginLeft=strWidth;
    }
};

window.onresize = function(){
    var windowWidth = document.body.clientWidth;
    var target = document.getElementById("sidebar");
    if(windowWidth>1200){
        target.classList.remove("toggle-temp");
        target.style.left="0px";
        target.style.marginLeft="0px";
    }
}

