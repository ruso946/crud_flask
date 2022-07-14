function guardar() {

    let n = document.getElementById("txtNombre").value
    let a = document.getElementById("txtApellido").value
    let d = parseInt(document.getElementById("txtDni").value)

    let paciente = {
        nombre: n,
        apellido: a,
        dni: d
    }
    let url = "'https://crud-flaskk.herokuapp.com/'"
    var options = {
        body: JSON.stringify(paciente),
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
       // redirect: 'follow'
    }
    fetch(url, options)
        .then(function () {
            window.location.href = "index.html";

            // Handle response we get from the API
        })
        .catch(err => {
            //this.errored = true
            alert("Error al grabar" )
            console.error(err);
        })
}