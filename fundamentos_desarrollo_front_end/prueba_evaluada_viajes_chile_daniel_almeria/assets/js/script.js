
$(document).ready(function () {
    console.log("ready") /*probamos el funcionamiento con console.log */


    /*mediante esta función conseguimos que el botón tenga simultáneamente un tooltip y un modal, siendo que con solo bootstrap solo podemos tener una de las dos: data-bs-toggle="tooltip" o data-bs-toggle="modal"*/
    $(".btn").click(function () {
        $('#exampleModal').modal('show');
    });
    $('[data-toggle="tooltip"]').tooltip()


    /*Esta función hace que al clicar el botón de confirmar envío se muestre un toast donde se hace la confirmación y se limpia el formulario*/
    $("#confirmarEnvio").click(function () {
        // Aquí debería ir el código del envio de datos



        //Esta función visualiza el toast de exito en el envío
        $("#toastExito").toast('show');
        //Esta función resetea el formulario
        $("#idFormulario")[0].reset();
    });


    /*Esta función genera el smooth scroll*/
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


    var formularioValidado = $('#idFormulario').validate({

        // Specify validation rules

        rules: {

            // The key name on the left side is the name attribute

            // of an input field. Validation rules are defined

            // on the right side

            nombre: {
                required: true,
                pattern: /^[a-zA-Z]+$/
            },
            apellido: {
                required: true,
                pattern: /^[a-zA-Z]+$/
            },

            mensaje: "required",
        },

        // Specify validation error messages

        messages: {

            nombre: {
                required: "Por favor, introduzca su nombre",
                pattern: "Por favor, ingrese solo letras en el nombre"
            },
            apellido: {
                required: "Por favor, introduzca su apellido",
                pattern: "Por favor, ingrese solo letras en el apellido"
            },
            mensaje: "Por favor, introduzca su mensaje",

        },


        invalidHandler: function (event, validator) {
            // Deshabilitar el botón de envío si hay errores
            $('#confirmarEnvio1').prop('disabled', true);
        },
        submitHandler: function (form) {
            console.log("Formulario válido. Enviando...");
            form.submit();

        }

    });
    // Deshabilitar el botón de envío al cargar la página
    $('#confirmarEnvio1').prop('disabled', true);

    // Monitorear cambios en el formulario
    var valorNombre = $('#idNombre').val();
    var valorApellido = $('#idApellido').val();
    var valorMensaje = $('#idMensaje').val();

    console.log('Nombre:', valorNombre);
    console.log('Apellido:', valorApellido);
    console.log('Mensaje:', valorMensaje);

    $('#idFormulario input').on('input', function () {
        // Verificar si el formulario es válido
        if (formularioValidado.form()) {
            // Habilitar el botón de envío si el formulario es válido
            $('#confirmarEnvio1').prop('disabled', false);
        } else {
            // Deshabilitar el botón de envío si el formulario no es válido
            $('#confirmarEnvio1').prop('disabled', true);
        }
    });


});

