from persona1 import Persona
class docente(Persona):
    def __init__(self, Nombre, Edad, Sueldo,Rol,Educacion,Asignatura):
        super().__init__(Nombre, Edad, Sueldo,Rol)
        self.__Eduacion=Educacion
        self.__Asignatura=Asignatura
        self.__Nombre=Nombre
        self.__Edad=Edad
        self.__Sueldo=Sueldo
        self.__Rol=Rol


    def __str__(self):
        return "Nombre:{},  Edad:{}  Sueldo:{},  Rol:{} Educacion:{},  Asignatura:{} ".format(self.__Nombre,self.__Edad,self.__Sueldo,self.__Rol,self.__Eduacion,self.__Asignatura)
    
    def setEduacion(self,Eduacion):
        self.__Eduacion=Eduacion
    def setHorario(self,Asignatura):
        self.__Asignatura=Asignatura

    def getEduacion(self):
        return self.__Eduacion

    def getAsignatura(self):
        return self.__Asignatura


    def Asignatura(self):
        if str(self.__Edad)<"50":
            Asignatura="Educacion Fisica"
        else:
             Asignatura="Matematicas"
        self.__Asignatura=Asignatura


        

