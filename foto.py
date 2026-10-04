from error import DimensionError

class Foto:
    MAX = 2500  

    def __init__(self, ancho, alto, ruta):
        self.ancho = ancho
        self.alto = alto
        self.ruta = ruta

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
       
        if ancho < 1 or ancho > Foto.MAX:
            raise DimensionError("Error al modificar el ancho", dimension=ancho, maximo=Foto.MAX)
      
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        
        if alto < 1 or alto > Foto.MAX:
            raise DimensionError("Error al modificar el alto", dimension=alto, maximo=Foto.MAX)
        
        self._alto = alto