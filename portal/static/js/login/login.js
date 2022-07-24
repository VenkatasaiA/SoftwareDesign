const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});

function init_file() {
var user_name = document.getElementById('username').value;
var pass_word = document.getElementById('password').value;
if (user_name.trim() === '')
     {
       document.getElementById("lb_login_username").className = '';
       document.getElementById('lb_login_username').innerHTML = 'Username is required!';
       return false;
    }
    else
    {
       document.getElementById("lb_login_username").className = 'error_r';
       document.getElementById('lb_login_username').innerHTML = '';
    }
    if (pass_word.trim() === '')
     {
       document.getElementById("lb_login_password").className = '';
       document.getElementById('lb_login_password').innerHTML = 'Password is required!';
       return false;
    }
    else
    {
       document.getElementById("lb_login_password").className = 'error_r';
       document.getElementById('lb_login_password').innerHTML = '';
    }

document.getElementById("multiform").action = '/fuel_quote';
document.getElementById("multiform").submit();
return true;
}

function init_register()
{
    var reg_username = document.getElementById('reg_username');
    var reg_email = document.getElementById('reg_email');
    var reg_password = document.getElementById('reg_password');
    var confi_reg_password = document.getElementById('conf_password');

    document.getElementById("lb_Username").className = 'error_r';
    document.getElementById("lb_email").className = 'error_r';
    document.getElementById("lb_password").className = 'error_r';
    document.getElementById("lb_conf_password").className = 'error_r';

    const usernameValue = reg_username.value.trim();
    const emailValue = reg_email.value.trim();
    const passwordValue = reg_password.value.trim();
    const password2Value = confi_reg_password.value.trim();

    if (usernameValue === '')
     {
       document.getElementById("lb_Username").className = '';
       document.getElementById('lb_Username').innerHTML = 'Username is required!';
       return false;
    }
    else
    {
       document.getElementById("lb_Username").className = 'error_r';
       document.getElementById('lb_Username').innerHTML = '';
    }
    if (emailValue === '') {
     document.getElementById("lb_email").className = '';
     document.getElementById('lb_email').innerHTML = 'Email is required!';
     return false;
    }
    else if (!isValidEmail(emailValue)) {
        document.getElementById("lb_email").className = '';
        document.getElementById('lb_email').innerHTML = 'Provide a valid email address!';
        return false;
    }
    else {
        document.getElementById("lb_email").className = 'error_r';
        document.getElementById('lb_email').innerHTML = '';
    }

    if (passwordValue === '') {
        document.getElementById("lb_password").className = '';
        document.getElementById('lb_password').innerHTML = 'Password is required!';
        return false;
    } else if (passwordValue.length < 8) {
        document.getElementById("lb_password").className = '';
        document.getElementById('lb_password').innerHTML = 'Password must be at least 8 character.';
        return false;
    }
    else {
        document.getElementById("lb_password").className = 'error_r';
        document.getElementById('lb_password').innerHTML = '';
    }
    if (password2Value === '') {
        document.getElementById("lb_conf_password").className = '';
        document.getElementById('lb_conf_password').innerHTML = 'Please confirm your password.';
        return false;
    }
    else if (password2Value !== passwordValue) {
        document.getElementById("lb_conf_password").className = '';
        document.getElementById('lb_conf_password').innerHTML = "Passwords doesn't match";
        return false;
    }
    else {
       document.getElementById("lb_conf_password").className = 'error_r';
        document.getElementById('lb_conf_password').innerHTML = '';
    }

    var check_list={'reg_username':reg_username.value,"reg_email":reg_email.value}
    $.ajax({
                url: '/fuel_quote/check',
                data: JSON.stringify(check_list),
                type: 'POST',
                contentType: "application/json",
                dataType: 'json',
                success: function (data)
                {
                    console.log(data['msg']);
                     if (data["msg"]=='user_name'){
                         document.getElementById("lb_Username").className = '';
                         document.getElementById('lb_Username').innerHTML = 'Username is already taken!';
                         return false
                      }
                      else{
                        document.getElementById("lb_Username").className = 'error_r';
                         document.getElementById('lb_Username').innerHTML = '';
                      }
                      if(data["msg"]=='email_id'){
                          document.getElementById("lb_email").className = '';
                         document.getElementById('lb_email').innerHTML = 'Email is already taken!';
                         return false
                      }
                      else{
                          document.getElementById("lb_email").className = 'error_r';
                         document.getElementById('lb_email').innerHTML = '';
                      }
                    var final_bills_request={"reg_username":reg_username.value,"reg_email":reg_email.value,"reg_password":reg_password.value};
                    $.ajax({
                                url: '/fuel_quote/client_registration',
                                data: JSON.stringify(final_bills_request),
                                type: 'POST',
                                contentType: "application/json",
                                dataType: 'json',
                                success: function (data1)
                                {
                                    console.log(data1['status']);
                                    if (data1["status"]=='User name is too long')
                                       {
                                             document.getElementById("lb_Username").className = '';
                                             document.getElementById('lb_Username').innerHTML = 'Username is is too long!';
                                             return false
                                       }
                                      else{
                                         document.getElementById("lb_Username").className = 'error_r';
                                         document.getElementById('lb_Username').innerHTML = '';
                                      }
                                      if(data1["status"]=='Invalid Gmail'){
                                          document.getElementById("lb_email").className = '';
                                         document.getElementById('lb_email').innerHTML = 'Invalid Gmail!';
                                         return false
                                      }
                                      else{
                                          document.getElementById("lb_email").className = 'error_r';
                                         document.getElementById('lb_email').innerHTML = '';
                                      }
                                    if(data1['status']=="successfully registered")
                                    {
                                       alert(data1['status'])
                                       window.location.href = "/fuel_quote/"
                                    }
                                    else{
                                        alert(data1['status'])
                                        return false;
                                    }

                                },
                                error: function(data1)
                                {
                                    console.log(data1);
                                    return false;
                                }
                        });

                },
                error: function(data)
                {
                    console.log(data);
                    return false;
                }
        });

}



//const password2 = document.getElementById('password2');

const isValidEmail = email => {
            const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
            return re.test(String(email).toLowerCase());
        }




