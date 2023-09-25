function validartodocontacto() {
    var nombre = document.getElementById('txtnombre').value;
    var correo = document.getElementById('txtcorreo').value;
    var telefono = document.getElementById('txttelefono').value;
    var mensaje = document.getElementById('txtmensaje').value;
    if (nombre=='' || correo=='' || mensaje==''){
        alert("Está todo mal");
        return;
    } else {
        alert('Se ha recuperado los siguientes datos: \n Nombre: '+nombre+'\n Correo: '+correo+'\n Telefono: '+telefono+'\n Mensaje: '+mensaje);
    }
}

function validarNombre() {
    var nombre = document.getElementById('txtnombre').value;
    alert(nombre);
}

function validarbuscar() {
    var buscar = document.getElementById('txtbuscar').value;
    alert('Se quiere buscar lo siguiente: '+buscar);
}

function validarlogin() {
    var user = document.getElementById('txtuser').value;
    var contrasena = document.getElementById('txtcontrasena').value;
    var sihaypass = "No hay texto aquí"
    if (user=='' || contrasena==''){
        alert("Está todo mal");
        return;
    } else {
        var sihaypass = "Si hay texto! Muy bien";
    }
    alert('Usuario: '+user + '\nContrasena: '+sihaypass);
}

function validarregistro() {
    var nombre = document.getElementById('txtnombre').value;
    var usuario = document.getElementById('txtusuario').value;
    var correo = document.getElementById('txtcorreo').value;
    var contrasena = document.getElementById('txtcontrasena').value
    var contrasena2 = document.getElementById('txtcontrasenaok').value;
    var sihaypass = "No hay texto aquí"
    if (nombre=='' || usuario=='' || correo=='' || contrasena=='' || contrasena2==''|| contrasena2!==contrasena){
        alert("Está todo mal");
        return;
    }
    else {
        var sihaypass = "Si hay texto! Muy bien";
    }
    alert('Nombre: '+nombre+'\Usuario: '+usuario+'\nCorreo: '+correo + '\nContrasena: '+sihaypass);
}

function recuperar_ip() {
    fetch("https://api.ipify.org?format=json")
    .then(function(response) {
        //status 200 ok, si falla
        if (response.status!=200) {
            alert ("está malo el server de ip :(");
            return;
        }
        response.json().then(function(data) {
            console.log(data);
            var ip= data.ip;
            alert("IP publica de tu dispositivo:" +ip)

        })
    })
}
