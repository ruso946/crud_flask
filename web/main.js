if (document.getElementById("app")) {
    const app = new Vue({
        el: "#app",
        data: {
            pacientes: [],
            errored: false,
            loading: true
        },
        created() {
            /*var url = 'http://localhost:5000/pacientes'*/
            var url = 'https://crud-flaskk.herokuapp.com/'
            this.fetchData(url)
        },
        methods: {
            fetchData(url) {
                fetch(url)
                    .then(response => response.json())
                    .then(data => {
                        this.pacientes = data;
                        this.loading = false;
                    })
                    .catch(err => {
                        this.errored = true
                    })
            },
            eliminar(paciente) {
                const url = 'https://crud-flaskk.herokuapp.com/' + paciente;
                var options = {
                    method: 'DELETE',
                }
                fetch(url, options)
                    .then(res => res.text()) // or res.json()
                    .then(res => {
                        location.reload();
                    })
            }
        }
    })
}
