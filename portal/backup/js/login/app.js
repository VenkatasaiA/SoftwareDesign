//const sign_in_btn = document.querySelector("#sign-in-btn");
//const sign_up_btn = document.querySelector("#sign-up-btn");
//const container = document.querySelector(".container");
//
//sign_up_btn.addEventListener("click", () => {
//  container.classList.add("sign-up-mode");
//});
//
//sign_in_btn.addEventListener("click", () => {
//  container.classList.remove("sign-up-mode");
//});


function loadJSON(callback) {
    var xobj = new XMLHttpRequest();
        xobj.overrideMimeType("application/json");
    xobj.open('GET', '/fuel_quote/enc_key', true);
    xobj.onreadystatechange = function () {
          if (xobj.readyState == 4 && xobj.status == "200") {
            callback(xobj.responseText);
          }
    };
    xobj.send(null);
 }

function init_file() {
 loadJSON(function(response) {
var user_name = document.getElementById('username').value;
var pass_word = document.getElementById('password').value;
alert(user_name)
alert(pass_word)
document.getElementById('username').value = user_name;
document.getElementById('password').value = pass_word;
document.getElementById("multiform").action = '/fuel_quote';
document.getElementById("multiform").submit();
return true;
 });
}



