import preguntas as p

def print_pregunta(enunciado, alternativas):
    
    # Imprimir enunciado y alternativas
    ###############################################################
    # print(f'''
    # {enunciado[0]}\n
    # A. Alternativa {alternativas[0][0][-1]}
    # B. Alternativa {alternativas[1][0][-1]}
    # C. Alternativa {alternativas[2][0][-1]}
    # D. Alternativa {alternativas[3][0][-1]}
    # ''')

    print(f'''
    {enunciado[0]}\n
    A. {alternativas[0][0]}
    B. {alternativas[1][0]}
    C. {alternativas[2][0]}
    D. {alternativas[3][0]}
    ''')
    
    ###############################################################
        
if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    
    # Enunciado básico 1

    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4