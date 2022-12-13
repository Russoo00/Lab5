from persona1 import Persona

class estudiante(Persona):
    def __init__(self,Nombre,Edad,Sueldo,Rol,Horario,Laburo):
        super().__init__(Nombre,Edad,Sueldo,Rol)
        self.__Horario=Horario
        self.__Laburo=Laburo
        self.__Edad=Edad
        self.__Nombre=Nombre
        self.__Sueldo=Sueldo
        self.__Rol=Rol


    def __str__(self):
       return "Nombre:{},  Edad:{}  Sueldo:{},  Rol:{} Horario:{},  Actualidad:{} ".format(self.__Nombre,self.__Edad,self.__Sueldo,self.__Rol,self.__Horario,self.__Laburo)

    def setLaburo(self,Laburo):
        self.__Laburo=Laburo
    def setHorario(self,Horario):
        self.__Horario=Horario

    def getLaburo(self):
        return self.__Laburo
    def getHorario(self):
        return self.__Horario


    def Laburo(self):
        if str(self.__Edad)<"40":
            Laburo="Estudiando PostGrado"
        else:
            Laburo="Dueño de una empresa"
        self.__Laburo=Laburo



