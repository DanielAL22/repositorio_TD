class Usuario():
    def __init__(self, nombre: str, apellido: str, email: str, genero: str) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.genero = genero

    def __str__(self) -> str:
        return f"{self.nombre} - {self.apellido} - {self.email} - {self.genero}"