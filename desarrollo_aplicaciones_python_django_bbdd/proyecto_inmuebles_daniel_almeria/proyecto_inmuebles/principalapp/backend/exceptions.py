class ServiceException(Exception):
    """se lanza cada vez que hay una excepcion en el service"""
    def __init__(self, mensaje) -> None:
        self.mensaje = mensaje
        
        
class RepositoryException(Exception):
    def __init__(self, mensaje) -> None:
        self.mensaje = mensaje