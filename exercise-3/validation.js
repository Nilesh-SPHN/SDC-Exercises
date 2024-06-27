function verifyPassword() {  
    var password = document.getElementById("password").value;
    var rpassword = document.getElementById("rpassword").value;
   //minimum & maximum password length validation  
    if(password.length < 8  || password.length > 15) {  
       document.getElementById("message").innerHTML = "**Password length must be atleast 8 characters & atmost 15 characters long";  
       return false;  
    }
    if(password != rpassword){
        document.getElementById("message").innerHTML = "Passwords not matching...";   
        return false;
    }  
  }  