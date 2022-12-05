from ELFO import Elfo
from ENANO import Enano
from HUMANO import Humano


humano=Humano("","","","","","","")
elfo=Elfo("","","","","","","")
enano=Enano("","","","","","","")
lista_p1=[]
lista_p2=[]

def player1():
    p1=int(input("Eliga el Personaje que quiere/1.Humano /2.Elfo /3.Enano:"))
    if p1 == 1:
        humano.SetNombre=("Peter")
        humano.SetRaza=("Humano")
        humano.SetArma=("Pistola")
        humano.SetVida=(100)
        humano.SetDamage=(12)
        humano.SetBoni=("Mas Daño")
        humano.Setfamilia=("Familia")
        humano.Historia()
        lista_p1.append(humano)
        print("Estadisticas:")
        print("Nombre :",humano.SetNombre,"/   Raza :",humano.SetRaza,"/   Arma :",humano.SetArma,"/   Vida :",humano.SetVida,"/   Daño :",humano.SetDamage,"/   Proveniente de la tribu:",humano.Setfamilia)
        
    elif p1 == 2:
        elfo.SetNombre=("Messi")
        elfo.SetRaza=("Elfo")
        elfo.SetArma=("Daga")
        elfo.SetVida=(85)
        elfo.SetDamage=(10)
        elfo.SetBoni=("Quita el 10% De daño al rival")
        elfo.Setreino=("Reino")
        elfo.Historia()
        lista_p1.append(elfo)
        print("Estadisticas:")
        print("Nombre :",elfo.SetNombre,"/   Raza :",elfo.SetRaza,"/   Arma :",elfo.SetArma,"/   Vida :",elfo.SetVida,"/   Daño :",elfo.SetDamage,"/   Proveniente de la tribu:",elfo.Setreino)
    elif p1 == 3:
        enano.SetNombre="r9"
        enano.SetRaza="Enano"
        enano.SetArma="Navaja"
        enano.SetVida=90
        enano.SetDamage=8
        enano.SetBoni="Aumenta Su vida"
        enano.Setclan="Clan"
        enano.Historia()
        lista_p1.append(enano)
        print("Estadisticas:")
        print("Nombre :",enano.SetNombre,"/   Raza :",enano.SetRaza,"/   Arma :",enano.SetArma,"/   Vida :",enano.SetVida,"/   Daño :",enano.SetDamage,"Proveniente de la tribu:",enano.Setclan)
    else:
        print("Seleccione Personaje Valido")
        return player1()
    lista_p1=[p1]


def player2():
    p2=int(input("Eliga el Personaje que quiere/1.Humano /2.Elfo /3.Enano:"))
    if p2 == 1:
        humano.SetNombre=("Peter")
        humano.SetRaza=("Humano")
        humano.SetArma=("Pistola")
        humano.SetVida=(100)
        humano.SetDamage=(12)
        humano.SetBoni=("Mas Daño")
        humano.Setfamilia=("Familia")
        humano.Historia()
        lista_p2.append(humano)
        print("Estadisticas:")
        print("Nombre :",humano.SetNombre,"/   Raza :",humano.SetRaza,"/   Arma :",humano.SetArma,"/   Vida :",humano.SetVida,"/   Daño :",humano.SetDamage,"/   Proveniente de la tribu:",humano.Setfamilia)
        
    elif p2 == 2:
        elfo.SetNombre=("Messi")
        elfo.SetRaza=("Elfo")
        elfo.SetArma=("Daga")
        elfo.SetVida=(85)
        elfo.SetDamage=(10)
        elfo.SetBoni=("Quita el 10% De daño al rival")
        elfo.Setreino=("Reino")
        elfo.Historia()
        lista_p2.append(elfo)
        print("Estadisticas:")
        print("Nombre :",elfo.SetNombre,"/   Raza :",elfo.SetRaza,"/   Arma :",elfo.SetArma,"/   Vida :",elfo.SetVida,"/   Daño :",elfo.SetDamage,"/   Proveniente de la tribu:",elfo.Setreino)
    elif p2 == 3:
        enano.SetNombre=("r9")
        enano.SetRaza=("Enano")
        enano.SetArma=("Navaja")
        enano.SetVida=(90)
        enano.SetDamage=(8)
        enano.SetBoni=("Aumenta Su vida")
        enano.Setclan=("Clan")
        enano.Historia()
        lista_p2.append(enano)
        print("Estadisticas:")
        print("Nombre :",enano.SetNombre,"/   Raza :",enano.SetRaza,"/   Arma :",enano.SetArma,"/   Vida :",enano.SetVida,"/   Daño :",enano.SetDamage,"Proveniente de la tribu:",enano.Setclan)
    lista_p2=[p2]
   
def AumentoVida(self):
        vida_nueva=int(input("Ingrese los puntos de vida que quiere sumar del 1 al 50"))
        if vida_nueva >=50 and vida_nueva<=100:
            enano.SetBoni=vida_nueva+self.__vida
            print("Su vida nueva es",enano.SetBoni)
            return True
        else:
            return False

"""""
def turnos():
    lista_p1
"""""  




def cambiar_arma(self):
    opcion=int(input("Cambiar el arma/ 1-Daga +10 daño  /2-Navaja +8  /3-Pistola +12 daño "))
    if opcion==1:
        humano.SetDamage=10
    if opcion==2:
        humano.SetDamage=8
    elif opcion==3:
        humano.SetDamage=15
    else:
        print("No valido")

