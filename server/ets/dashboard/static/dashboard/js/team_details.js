var ele_list = document.getElementsByClassName("change-category");
for (var i=0; i < ele_list.length; i++) {
        ele_list[i].addEventListener("click", function(i){
            //change display
            var bool = this.classList.toggle("bi-toggle-on");
            this.classList.toggle("bi-toggle-off");
            var str;
            if(!bool){
                this.innerHTML="&nbsp;&nbsp;&nbsp;Unproductive";
                str="0";
            }
            else{
                this.innerHTML="&nbsp;&nbsp;&nbsp;Productive";
                str="1";
            }
            
            //API call to save category setting in database
            const data={
                prod:str
            };
            fetch('http://127.0.0.1:8000/toggle-prod-category', {
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
        });
};