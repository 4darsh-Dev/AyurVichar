let submit = document.getElementById('signup-btn');

submit.addEventListener('click', function(){
    let myForm = document.getElementById('my-form');
    myForm.submit();
    console.log('Submitted Successfully! ');
    
})

let input = document.getElementById('cnf-password');

input.addEventListener("keypress", function(event){
    if (event.key==="Enter"){
        // prevents the defualt options.
        event.preventDefault();

        //click the button.
        document.getElementById("signup-btn").click();

    }

})

// For Error message displaying and closing it 
let crossBtn = document.getElementById("cross-btn");
let errorMsgElem = document.getElementById("error-message");

crossBtn.addEventListener("click", function(){
    errorMsgElem.style.display = "none";

})

document.addEventListener("DOMContentLoaded", function(){

    // Setting timeout for n Seconds
    setTimeout(() => {
        if(errorMsgElem){
            errorMsgElem.style.display = "none";
        }
    }, 5000); 

    
})