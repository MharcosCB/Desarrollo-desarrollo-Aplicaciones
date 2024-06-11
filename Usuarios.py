class Usuarios():    
    __id_usu=0
    __nom_usu=""
    __con_usu=0
    __id_cli=0
    __nom_cli=""
    __id_tip=0
    __nom_tip="" 

    def __init__(self):
        pass
        
    def setId_usu(self,id):
        self.__id_usu =id   
                
    def setNom_usu(self,nombre):
        self.__nom_usu=nombre
        
    def setCon_usu(self,con):
        self.__con_usu=con

    def setid_cli(self,cli):
        self.__id_cli=cli

    def setnom_cli(self,nom_cli):
        self.__nom_cli=nom_cli

    def setId_tip(self,id_tip):
        self.__id_tip=id_tip

    def setNom_tip(self,nom_tip):
        self.__nom_tip=nom_tip

    #-----------------------------------------
    def getId_usu(self):
        return self.__id_usu
                
    def getNom_usu(self):
        return self.__nom_usu
            
    def getCon_usu(self):
        return self.__con_usu

    def getid_cli(self):
        return self.__id_cli

    def getnom_cli(self):
        return self.__nom_cli

    def getId_tip(self):
        return self.__id_tip

    def getNom_tip(self):
        return self.__nom_tip