class Clientes():
        
    __id_cli=0
    __nom_cli=str
    __pat_cli=str
    __mat_cli=str
    __rut_cli=str
    __id_com=0
    __nom_com=str

    def __init__(self):
        pass
        
    def setId_cli(self,idcli):
        self.__id_cli =idcli
                
    def setNom_cli(self,nomcli):
        self.__nom_cli=nomcli
        
    def setCon_cli(self,patcli):
        self.__pat_cli=patcli

    def setid_cli(self,matcli):
        self.__mat_cli=matcli

    def setnom_cli(self,rutcli):
        self.__rut_cli=rutcli

    def setId_tip(self,idcom):
        self.__id_com=idcom

    def setNom_tip(self,nomcom):
        self.__nom_com=nomcom

#-----------------------------------------------------------
    def __init__(self):
        pass
        
    def getId_cli(self):
        return self.__id_cli 
                
    def getNom_cli(self):
        return self.__nom_cli
        
    def getCon_cli(self):
        return self.__pat_cli

    def getid_cli(self):
        return self.__mat_cli

    def getnom_cli(self):
        return self.__rut_cli

    def getId_tip(self):
        return self.__id_com

    def getNom_tip(self):
        return self.__nom_com