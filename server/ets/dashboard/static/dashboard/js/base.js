document.getElementById('toggle-sidebar-btn').onclick = toggleFunc;
document.getElementById('menu-break').onclick = selectBreakFunction;

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


function selectBreakFunction(){
    var ele = document.querySelector("#menu-break span");
    var str='0';
    //Break time
    if (ele.innerHTML==="Break"){
        document.querySelector('#menu-break div').classList.remove("options");
        ele.innerHTML = "Resume";
        str="0";
    }
    //Break ends, start tracking
    else{
        document.querySelector('#menu-break div').classList.add("options");
        ele.innerHTML = "Break";
        str="1";
    }

    const data={
        track:str
    };
    var url = "http://localhost:8000/toggle-break";
    fetch('http://127.0.0.1:8000/toggle-break', {
        method: 'POST', 
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
        mode: 'same-origin',
    })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}
