import app.obtencion_datos as obtencion_datos
from string import Template


def app(n_aves):
    # for index in range(0, n_aves):
    #     print(obtencion_datos.obtener_photos(index))
    #     print(obtencion_datos.obtener_name_spanish(index))
    #     print(obtencion_datos.obtener_name_english(index))
    lista_fotos = [obtencion_datos.obtener_photos(index) for index in range(0, n_aves)]
    lista_name_spanish = [obtencion_datos.obtener_name_spanish(index) for index in range(0, n_aves)]
    lista_name_english = [obtencion_datos.obtener_name_english(index) for index in range(0, n_aves)]

    # img_template = Template('img src = "$urlImagen" /')
    # name_spanish_template = Template('<h2> $urlSpanishName </h2>')
    # name_english_template = Template('<h2> $urlEnglishName </h2>')

    img_template = Template('''
                                <h4> Nombre en español: $spanishName </h4>
                                <h4> Nombre en inglés: $englishName </h4>
                                <img src = "$urlImagen" style="width: 30; height: 20;"/>
                                <hr>
                            ''')


    html_template = Template('''
                                <!DOCTYPE html>
                                <html lang="en">
                                <head>
                                    <meta charset="UTF-8">
                                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                    <title>Aves de Chile</title>
                                </head>
                                <body>
                                    <h1>AVES DE CHILE</h1>
                                    $body
    
                                </body>
                                </html>
                            ''')


    texto_img = ""
    for url_foto, spanish_name, english_name in zip(lista_fotos, lista_name_spanish, lista_name_english):
        texto_img += img_template.substitute({"urlImagen": url_foto, "spanishName": spanish_name, "englishName": english_name}) + "\n"
    #print(texto_img)

    html = html_template.substitute(body = texto_img)
    #print(html)
    

    with open('aves.html', 'w', encoding="utf-8") as f:
        f.write(html)

    f.close() #es una buena practica cerrar el archivo

        



if __name__ == '__main__':
    n_aves=2
    app(n_aves)




