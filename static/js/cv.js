
function contact(){
    window.location.replace("cv2.html");
}

function check(){
    const inputValue1= document.getElementById("Lmonths");
    const inputValue2= document.getElementById("Pnumber");
    if (!inputValue1.checkValidity() && !inputValue2.checkValidity()){
        document.getElementById("demo").innerHTML= inputValue1.validationMessage;
    }
    else if (inputValue1.checkValidity() && !inputValue2.checkValidity()){
        document.getElementById("demo").innerHTML= inputValue2.validationMessage;
    }
    else if (!inputValue1.checkValidity() && inputValue2.checkValidity()){
        document.getElementById("demo").innerHTML= inputValue1.validationMessage;
    }
    else{
        document.getElementById("demo").innerHTML= "All values are correct. Linking you to my LinkedIn site";
    }
}