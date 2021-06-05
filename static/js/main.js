function myFunction() {
    var x = document.getElementById("dropdown");
    if(x.style.display == 'flex'){
        x.style.display = 'none';
    }else {
        x.style.display = 'flex';                    
    }
  }


// Count clicked

var cnt=0;
function CountFun(){
    cnt=parseInt(cnt)+parseInt(1);
    var divData=document.getElementById("shopping-cart");
    divData.value = cnt;
    // divData.innerHTML="Number of Downloads: ("+cnt +")";//this part has been edited
}
