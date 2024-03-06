# preguntas_basicas = {
#     'pregunta_1': {'enunciado':['Enunciado básico 1'],
#     'alternativas': [['alt_1', 0], 
#                      ['alt_2', 1], 
#                      ['alt_3', 0], 
#                      ['alt_4', 0]]},
#     'pregunta_2': {'enunciado':['Enunciado básico 2'],
#     'alternativas': [['alt_1', 0], 
#                      ['alt_2', 1], 
#                      ['alt_3', 0], 
#                      ['alt_4', 0]]},
    
# 'pregunta_3': {'enunciado':['Enunciado básico 3'],
#     'alternativas': [['alt_1', 0], 
#                      ['alt_2', 1], 
#                      ['alt_3', 0], 
#                      ['alt_4', 0]]}
# }

# preguntas_intermedias = {
#     'pregunta_1': {'enunciado':['Enunciado intermedio 1'],
#     'alternativas': [['alt_1', 0], 
#                      ['alt_2', 1], 
#                      ['alt_3', 0], 
#                      ['alt_4', 0]]},
#     'pregunta_2': {'enunciado':['Enunciado intermedio 2'],
#     'alternativas': [['alt_1', 0], 
#                      ['alt_2', 1], 
#                      ['alt_3', 0], 
#                      ['alt_4', 0]]},
    
# 'pregunta_3': {'enunciado':['Enunciado intermedio 3'],
#     'alternativas': [['alt_1', 0], 
#                      ['alt_2', 1], 
#                      ['alt_3', 0], 
#                      ['alt_4', 0]]}
# }

# preguntas_avanzadas = {
#     'pregunta_1': {'enunciado':['Enunciado avanzado 1'],
#     'alternativas': [['alt_1', 0], 
#                      ['alt_2', 1], 
#                      ['alt_3', 0], 
#                      ['alt_4', 0]]},
#     'pregunta_2': {'enunciado':['Enunciado avanzado 2'],
#     'alternativas': [['alt_1', 0], 
#                      ['alt_2', 1], 
#                      ['alt_3', 0], 
#                      ['alt_4', 0]]},
    
# 'pregunta_3': {'enunciado':['Enunciado avanzado 3'],
#     'alternativas': [['alt_1', 0], 
#                      ['alt_2', 1], 
#                      ['alt_3', 0], 
#                      ['alt_4', 0]]}
# }

preguntas_basicas = {
    'pregunta_1': {'enunciado': ['¿Cuál es el río más largo del mundo?'],
                   'alternativas': [['Nilo', 0],
                                    ['Amazonas', 1],
                                    ['Yangtsé', 0],
                                    ['Misisipi', 0]]},
    'pregunta_2': {'enunciado': ['¿Cuál es el metal más abundante en la corteza terrestre?'],
                   'alternativas': [['Hierro', 0],
                                    ['Aluminio', 1],
                                    ['Cobre', 0],
                                    ['Oro', 0]]},
    'pregunta_3': {'enunciado': ['¿Quién pintó la Mona Lisa?'],
                   'alternativas': [['Pablo Picasso', 0],
                                    ['Leonardo da Vinci', 1],
                                    ['Vincent van Gogh', 0],
                                    ['Claude Monet', 0]]}
}

preguntas_intermedias = {
    'pregunta_1': {'enunciado': ['¿Cuál es el país más grande del mundo por territorio?'],
                   'alternativas': [['Canadá', 0],
                                    ['Rusia', 1],
                                    ['China', 0],
                                    ['Estados Unidos', 0]]},
    'pregunta_2': {'enunciado': ['¿Quién escribió "Don Quijote de la Mancha"?'],
                   'alternativas': [['Gabriel García Márquez', 0],
                                    ['Miguel de Cervantes', 1],
                                    ['William Shakespeare', 0],
                                    ['Fyodor Dostoevsky', 0]]},
    'pregunta_3': {'enunciado': ['¿En qué año comenzó la Guerra del Pacífico?'],
                   'alternativas': [['1812', 0],
                                    ['1879', 1],
                                    ['1898', 0],
                                    ['1915', 0]]}
}

preguntas_avanzadas = {
    'pregunta_1': {'enunciado': ['¿Cuál es el autor de la obra "El principito"?'],
                   'alternativas': [['Jorge Luis Borges', 0],
                                    ['Antoine de Saint-Exupéry', 1],
                                    ['Franz Kafka', 0],
                                    ['Ernest Hemingway', 0]]},
    'pregunta_2': {'enunciado': ['¿Qué famoso científico formuló la teoría de la relatividad?'],
                   'alternativas': [['Isaac Newton', 0],
                                    ['Albert Einstein', 1],
                                    ['Stephen Hawking', 0],
                                    ['Galileo Galilei', 0]]},
    'pregunta_3': {'enunciado': ['¿Quién fue el primer presidente de Estados Unidos?'],
                   'alternativas': [['Thomas Jefferson', 0],
                                    ['George Washington', 1],
                                    ['Abraham Lincoln', 0],
                                    ['John Adams', 0]]}
}



pool_preguntas = {'basicas': preguntas_basicas,
                  'intermedias': preguntas_intermedias,
                  'avanzadas': preguntas_avanzadas}