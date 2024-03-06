


estimulos = input('¿Responde a estímulos?\n')

if estimulos == 'si':
    print('Valorar la necesidad de llevarlo al hospital más cercano')
    print('Fin')
else:
    print('Abrir la vía aérea')
    respiracion = input('¿Respira?\n')
    if respiracion == 'si':
        print('Permitirle posición de suficiente ventilación')
        print('Fin')
    else:
        print('Administrar 5 ventilaciones y llamar a Ambulancia')
        ambulancia = 'no'
        while ambulancia == 'no': 
            signos_vitales = input('¿Signos de vida?\n')
            if signos_vitales == 'si':
                print('Reevaluar a la espera de la Ambulancia')
            else:
                print('Administrar Compresiones Torácicas hasta que llegue la ambulancia')
            ambulancia = input('¿Llegó la Ambulancia?\n')
        print('Fin')
        
