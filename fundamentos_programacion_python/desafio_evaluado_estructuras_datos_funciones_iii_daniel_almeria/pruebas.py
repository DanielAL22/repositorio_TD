preguntas_basicas = {
    'pregunta_1': {'enunciado':['Enunciado básico 1'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]},
    'pregunta_2': {'enunciado':['Enunciado básico 2'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]},
    
'pregunta_3': {'enunciado':['Enunciado básico 3'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]}
}

# print(preguntas_basicas['pregunta_1']['alternativas'].index(['alt_2', 1]))


print(preguntas_basicas['pregunta_1']['alternativas'][1][1])

# if [0][eleccion][1] == 1:
#     print('Respuesta Correcta')
#     correcto = True
# else:
#     print('Respuesta Incorrecta')
#     correcto = False