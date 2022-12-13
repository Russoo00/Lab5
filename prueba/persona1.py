class Persona():
    def __init__(self,Nombre,Edad,Sueldo,Rol):
        self.__Nombre=Nombre
        self.__Edad=Edad
        self.__Sueldo=Sueldo
        self.__Rol=Rol
    
    def __str__(self):
        return "Nombre:{},  Edad:{}  Sueldo:{},  Rol:{} ".format(self.__Nombre,self.__Edad,self.__Sueldo,self.__Rol)
        
    
    def setNombre(self,Nombre):
        self.__Nombre=Nombre
    def setEdad(self,Edad):
        self.__Edad=Edad
    def setSueldo(self,Sueldo):
        self.__Sueldo=Sueldo
    def setRol(self,Rol):
        self.__Rol=Rol
    



    def getNombre(self):
        return self.__Nombre
    def getEdad(self):
        return self.__Edad
    def getSueldo(self):
        return self.__Sueldo
    def getRol(self):
        return self.__Rol
    





 