from random import uniform

class Personaje:


    def __init__(self, nombre:str) -> None:
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    @staticmethod
    def aparicion_rival():
        print("""
        Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.
        Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.""")
        respuesta_usuario = input("""
            ¿Qué deseas hacer?
            1. Atacar
            2. Huir\n""")

        return respuesta_usuario

        


    #getter
    @property
    def estado(self):
        print(f'Nombre: {self.nombre} || Nivel: {self.nivel} || Experiencia: {self.experiencia}')
        return self.nombre, self.nivel, self.experiencia


    #setter
    @estado.setter
    def estado(self, experiencia_recibida):
        
        if experiencia_recibida > 0:
            experiencia_total = self.experiencia + experiencia_recibida + self.nivel * 100
            self.nivel = experiencia_total // 100
            self.experiencia = experiencia_total % 100

        elif experiencia_recibida < 0:
            experiencia_total = self.experiencia + experiencia_recibida + self.nivel * 100
            self.nivel = experiencia_total // 100
            self.experiencia = experiencia_total - (experiencia_total // 100) * 100
            if experiencia_total < 100:
                self.experiencia = 0
            if self.nivel < 1:
                self.nivel = 1

        else:
            experiencia_recibida = 0
            experiencia_total = experiencia_recibida
            self.experiencia = experiencia_recibida
            self.nivel = self.nivel


    def __lt__(self, other):
        return self.nivel < other.nivel

    def __gt__(self, other):
        return self.nivel > other.nivel

    def __eq__(self, other):
        return self.nivel == other.nivel

    # Método de instancia que retorna la probabilidad de la instancia actual de ganar respecto de otra instancia (opcional).
    def probabilidad_ganar(self, rival):
        if self.nivel < rival.nivel:
            print(f"Con tu nivel actual, tienes 33% de probabilidad de ganarle al {rival.nombre}.")
            probabilidad = 0.33
        elif self.nivel > rival.nivel:
            print(f"Con tu nivel actual, tienes 66% de probabilidad de ganarle al {rival.nombre}.")
            probabilidad = 0.66
        else:
            print(f"Con tu nivel actual, tienes 50% de probabilidad de ganarle al {rival.nombre}.")
            probabilidad = 0.5
        return probabilidad


    def pelea(self, probabilidad, rival):
        resultado_ataque = uniform(0, 1)
        if resultado_ataque <= probabilidad:
            self.estado = 50
            rival.estado = -30
            print(f"""¡Le has ganado al {rival.nombre}, felicidades!
            ¡Recibirás 50 puntos de experiencia!""")
            self.estado
            rival.estado
        else:
            self.estado = -30
            rival.estado = 50
            print(f"""¡Oh no! ¡El {rival.nombre} te ha ganado!
            ¡Has perdido 30 puntos de experiencia!""")
            self.estado
            rival.estado















personaje = Personaje("Aragorn")
personaje.estado = 150
print(personaje.estado)
personaje.estado
print(personaje)

personaje2 = Personaje("Legolas")
personaje2.estado = 250
print(personaje2.estado)

print(personaje < personaje2)
print(personaje > personaje2)
print(personaje == personaje2)









