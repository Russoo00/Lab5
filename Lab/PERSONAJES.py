class personaje():

    def __init__(self,nombre,raza,arma,vida,damage,boni):
        self.__nombre=nombre
        self.__raza=raza
        self.__arma=arma
        self.__vida=vida
        self.__damage=damage
        self.__boni=boni
    def __str__(self):
        return "Nombre:{},Raza:{},Arma:{}Vida:{},Damage:{},bonificacion:{}".format(self.__nombre,self.__raza,self.__arma,self.__vida,self.__damage,self.__boni)
    def GetNombre(self):
        return self.__nombre
    def SetNombre(self,nombre):
        self.__nombre=nombre
    def GetRaza (self):
        return self.__raza
    def SetRaza(self,raza):
        self.__raza=raza
    def GetArma(self):
        return self.__arma
    def SetArma(self,arma):
        self.__arma=arma
    def GetVida(self):
        return self.__vida
    def SetVida(self,vida):
        self.__vida=vida
    def GetDamage(self):
        return self.__damage
    def SetDamage(self,damage):
        self.__damage=damage
    def GetBoni(self):
        return self.__boni
    def SetBoni(self,boni):
        self.__boni
    def Historia(self):
        pass
    def Combate(self,):
        pass
    def Victoria(self):
        pass
    def Derrota(self):
        pass
    def Mensaje_inicio(self):
        pass
   






    
    
   
        
        
        
        