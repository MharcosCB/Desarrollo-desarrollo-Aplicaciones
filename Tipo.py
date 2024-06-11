class Tipo():    
    __id_tip=0
    __nom_tip=""
    __pat_tip=""
    __mat_tip=""
    __rut_tip=""
    __id_car=0 
    __nom_car=""

    def __init__(self):
        pass
        
    def setId_tip(self,idtip):
        self.__id_tip =idtip
                
    def setNom_tip(self,nombre_tipo):
        self.__nom_tip=nombre_tipo
        
    def setPat_tip(self,pat):
        self.__pat_tip=pat

    def setMat_tip(self,mat):
        self.__mat_tip=mat
    
    def setRut_tip(self,id_tip):
        self.__rut_tip=id_tip

    def setId_car(self,id_car):
        self.__id_car=id_car

    def setnom_car(self,nom_car):
        self.__nom_car=nom_car
    #-----------------------------------------
    def getId_tip(self):
        return self.__id_tip
                    
    def getNom_tip(self):
        return self.__nom_tip
        
    def getPat_tip(self):
        return self.__pat_tip

    def getMat_tip(self):
        return self.__mat_tip
        
    def getRut_tip(self):
        return self.__rut_tip

    def getId_car(self):
        return self.__id_car

    def getnom_car(self):
        return self.__nom_car