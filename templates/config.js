var login = false;
var login_nom = "";


function saveLogin() {
    var passwordInput = document.getElementById('password');
    login_nom = passwordInput.value;
    console.log(login_nom)
}