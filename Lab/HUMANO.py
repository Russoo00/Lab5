from PERSONAJES import personaje

class Humano(personaje):
    def __init__(self,nombre,raza,arma,vida,damage,boni,familia):
        super().__init__(nombre,raza,arma,damage,vida,boni)
        self.__familia=familia
    def __str__(self):
        return super().__str__()+"Familia:{}".format(self.__familia)
    def Getfamilia(self,):
        return self.__familia
    def Setfamilia(self,familia):
        self.__familia=familia
    def Historia(self):
        print("Historia: Debido a un fallo en la realidad,esta atrapado en este mundo virtual")
    def Derrota(self):
        if self.__vida <=0:
            print("Ha sido derrotado")
            return True
        else:
            return False
    def Victoria(self):
        print("Has Ganado")
        return ("Nombre",self.__nombre)

    def Bono(self):
        pass
        """""
        daño_nuevo=int(input("Ingrese el daño que quiera añadir Solo se permite del +5 hasta el +15"))
        i=daño_nuevo
        while i >=5 and i <=15:
            if i!=0:
                i=daño_nuevo-1
                self.__boni=self.__damage+daño_nuevo
                print("Tu nuevo daño sera de",self.__boni)
                return True
            else:
                False

        else:
            print("INVALIDO")
            return False
            
            ESTA MALO XD
"""

    

    
