
$(document).ready(function () {
    console.log("ready") /*probamos el funcionamiento con console.log */

    //Evento
    $("#enviarCorreo").click(function () {
        console.log("click enviar por correo")   /*probamos el funcionamiento del click del botón con console.log */
        alert("El correo fue enviado correctamente")
    });

    //Selectores de clase
    $('.card-title').click(function () {
        console.log("click titulo tarjeta")   /*probamos el funcionamiento del click del botón con console.log */
        $('.card-text').toggle();
    });

    // Defino variable que valida si el titulo es rojo
    var isRed = false;
    // Selecciono el ID y le asigno el evento  
    $("#Ingrediente").on("dblclick", function () {
        console.log("db click ingrediente")
        // Validamos el color actual y se ajusta en función de ello.
        if (isRed) {
            $(this).css("color", "");
            //Pruebo el codigo
            console.log(this);

        } else {
            $(this).css("color", "red");
        }
        // Se invierte el color para el proximo doble click.
        isRed = !isRed;
    });
    // Con esta sintaxis deja el titulo en red pero no lo retorna a su color original luego.
    //     $(this).css("color","red");
    //     console.log(this);
    // });

    $("#Preparacion").on("dblclick", function () {
        console.log("db click ingrediente")
        // Validamos el color actual y se ajusta en función de ello.
        if (isRed) {
            $(this).css("color", "");
            //Pruebo el codigo
            console.log(this);

        } else {
            $(this).css("color", "red");
        }
        // Se invierte el color para el proximo doble click.
        isRed = !isRed;
    });


});

