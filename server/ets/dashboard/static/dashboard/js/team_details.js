var ele_list = document.getElementsByClassName("change-category");
for (var i=0; i < ele_list.length; i++) {
        ele_list[i].addEventListener("click", function(i){
            var bool = this.classList.toggle("bi-toggle-on");
            this.classList.toggle("bi-toggle-off");
            if(!bool){
                this.innerHTML="&nbsp;&nbsp;&nbsp;Unproductive";
            }
            else{
                this.innerHTML="&nbsp;&nbsp;&nbsp;Productive";
            }
        });
};