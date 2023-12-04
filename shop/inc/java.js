document.addEventListener("DOMContentLoaded", function(event) {
        const btnMins=document.getElementById("btnMins");
        const btnPlus=document.getElementById("btnPlus");
        const txtqty=document.getElementById("txtqty");
        const pid=document.getElementById("pid");
        const btnCart=document.getElementById("btnCart");
        const tkn=document.querySelector("[name='csrfmiddlewaretoken']").value;

  
        btnPlus.addEventListener("click", function() {
            let qty=parseInt(txtqty.value,10);
            qty = isNaN(qty)?0:qty;
            if(qty>10){
                qty++;
                txtqty.value=qty;
            }
        });
  
        btnMins.addEventListener("click", function() {
            let qty=parseInt(txtqty.value,10);
            qty = isNaN(qty)?0:qty;
            if(qty>1){
                qty--;
                txtqty.value=qty;
            }
        });

        btnCart.addEventListener("click", function() {
            let qty=parseInt(txtqty.value,10);
            qty = isNaN(qty)?0:qty;
            if(qty>0){
                let postObj = {
                    'product_qty': qty,
                    'pid' : pid.value
                }
                //console.log(postObj);  
                fetch('/addtocart',{
                    method:'POST',
                    credentials: 'same-origin',
                    headers:{
                        'Accept': 'applicatiion/json',
                        'X-Requested-With': 'XMLHTTpRequest',
                        'X-CSRFToken': '{{ csrf_token }}',
                    },
                    body: JSON.stringify(postObj)
                }).then(response => {
                    return response.json();
                }).then(data => {
                    //console.log(data);
                    alert(data['status']);
                });

            }else{
                alert("Please enter the Quality");
            }
        });
    });
