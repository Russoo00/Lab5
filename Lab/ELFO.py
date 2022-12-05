from PERSONAJES import personaje  

class Elfo(personaje):
    def __init__(self,nombre,raza,arma,vida,damage,boni,reino):
        super().__init__(nombre,raza,arma,vida,damage,boni)
        self.__reino=reino
    def __str__(self):
        return super().__str__()+"Reino:{}".format(self.__reino)
    def Getreino(self):
        return self.__reino
    def Setreino(self,reino):
        self.__reino=reino
    def Historia(self):
        print("Historia: Proveniente de los bosques magicos encantados")
    def Derrota(self):
        if self.__vida <=0:
            print("Ha sido derrotado"/self.Historia)
            return True
        else:
            return False
    def Victoria(self):
        print("Felicidades Has ganado")
        return ("Nombre",self.__nombre)
    def QuitaVida(self):
        super().SetVida(super().GetVida())



    



