from PERSONAJES import personaje

class Enano(personaje):
    def __init__(self,nombre,raza,arma,vida,damage,boni,clan):
        super().__init__(nombre,raza,arma,vida,damage,boni)
        self.__clan=clan
    def __str__(self):
        return super().__str__()+"Clan:{}".format(self.__clan)
    def Getclan(self):
        return self.__clan
    def Setclan(self,clan):
        self.__clan=clan
    def Historia(self):
        print("Historia :Proveniente de la mitologia nordica")
    def Derrota(self):
        if self.__vida <=0:
            print("El ser Ha muerto")
            return True
        else:
            return False
    def Victoria(self):
        pass
    def AumentoVida(self):
       pass
            



