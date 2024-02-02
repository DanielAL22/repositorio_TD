
$(document).ready(function () {
    console.log("ready") /*probamos el funcionamiento con console.log */


    /*mediante esta función conseguimos que el botón tenga simultáneamente un tooltip y un modal, siendo que con solo bootstrap solo podemos tener una de las dos: data-bs-toggle="tooltip" o data-bs-toggle="modal"*/
    $(".btn").click(function () {
        $('#exampleModal').modal('show');
    });
    $('[data-toggle="tooltip"]').tooltip()


    /*Esta función hace que al clicar el botón de confirmar envío se muestre un toast donde se hace la confirmación*/
    $("#confirmarEnvio").click(function () {
        // Aquí debería ir el código del envio de datos

        $("#toastExito").toast('show');
    });


    $('a[href^="#"]').on('click', function (event) {
        // Asegúrate de que this.hash tenga un valor antes de anular el comportamiento predeterminado
        if (this.hash !== '') {
            // Previene el comportamiento predeterminado del enlace
            event.preventDefault();

            // Almacena el hash
            var hash = this.hash;

            // Usa jQuery animate() para hacer un desplazamiento suave a ese hash
            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 600, function () {
                // Añade el hash (#) a la URL cuando haya terminado de desplazarse (comportamiento opcional)
                window.location.hash = hash;
            });
        }
    });


});