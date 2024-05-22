console.log("hola mundo")


$(document).ready(function () {
    console.log("ready")
    //**************************FUNCIONES***************************





    // ********GPT**********
    $('.carousel-item img').each(function() {
        console.log("function1")
        // Obtener el tamaño original de la imagen
        var anchoOriginal = $(this).prop('naturalWidth');
        var altoOriginal = $(this).prop('naturalHeight');
        
        console.log(anchoOriginal)
        console.log(altoOriginal)

        // Calcular la relación de aspecto
        var relacionAspecto = anchoOriginal / altoOriginal;

        console.log('relacion/aspecto', relacionAspecto)

        // Establecer el tamaño fijo para mantener la proporción de aspecto
        $(this).css('width', (600 / relacionAspecto) + 'px'); // Ancho fijo deseado
        $(this).css('height', (600 / relacionAspecto) + 'px'); // Calcular la altura proporcional
    });


    //**************************EVENTOS***************************





})