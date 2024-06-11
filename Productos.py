class Productos():
    __id=0; __nombre="" ;__precio= 0
    
    def __init__(self):
        pass
    
    def setId(self,id):
        self.__id =id
            
    def setNombre(self,nom):
        self.__nombre=nom
    
    def setPrecio(self,pre):
        self.__precio=pre
    
    def getNombre(self):
        return self.__nombre
    
    def getPrecio(self):
        return self.__precio
    
    def getId(self):
        return self.__id
    