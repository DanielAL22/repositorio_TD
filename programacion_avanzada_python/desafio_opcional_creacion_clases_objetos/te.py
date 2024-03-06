class Te:
    #atributos estáticos o de clase
    duracion: int = 365
    #formato: list = [300, 500]
    #precio: dict = {"300": 3000, "500": 5000}

    #metodo de instancias, debe recibir self
    def set_nombre(self, nombre_te_num:int):
        if nombre_te_num == 1:
            self.nombre = "Té Negro"
        elif nombre_te_num == 2: 
            self.nombre = "Té Verde"
        else:
            self.nombre = "Agua de hierbas"
    

    #método estático
    @staticmethod
    def set_tiempo_recomendacion(nombre_te_num:int):
        if nombre_te_num == 1:
            tiempo = 3
            recomendacion = "desayuno"
            return tiempo, recomendacion
        elif nombre_te_num == 2:
            tiempo = 5
            recomendacion = "medio dia"
            return tiempo, recomendacion
        else:
            tiempo = 6
            recomendacion = "atarceder"
            return tiempo, recomendacion

    def set_formato_precio(formato_te_num:int):
        if formato_te_num == 1:
            formato = 300
            precio = 3000
            return formato, precio
        else:
            formato = 500
            precio = 5000
            return formato, precio













    # def set_atributos(self, tiempo:int = None, recomendacion:str = ""):
    #     #atributos no estáticos o de instancia
    #     #con el self hacemos referencia a la instancia
    #     self.tiempo = tiempo
    #     self.recomendacion = recomendacion

    # sabor_ingresado = 1

    # #método estático
    # @staticmethod
    # def set_tiempo_recomendacion(sabor:int = sabor_ingresado):
    #     if sabor == 1:


