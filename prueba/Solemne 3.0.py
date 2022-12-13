import pandas as pd 
import numpy as np
import random
from Estudiante import estudiante
from Docente import docente
from pandas import ExcelWriter




Lista_E=[]
Lista_D=[]


df = pd.read_csv("Datos.csv",index_col="Id")
def Datos():
    print(df)
#Eliminar datos
def filtro():
    Filtro_Nombre=(df["Nombres"]=="TRUE")|(df["Nombres"]=="FALSE")#Filtramos los nombres true y false
    Filtro_Edad=(df["Edad"]<=1)|(df["Edad"]>120)#filtramos las edades
    nombres= df[Filtro_Nombre].index
    edad=df[Filtro_Edad].index
    df.dropna()#elimina los conjuntos vacios "NaN"
    df.drop(nombres,inplace=True)#elimina los nombres 
    df.drop(edad,inplace=True)#elimina las edades
    df.sort_values("Sueldo",ascending=True,inplace=True)#Ordenamos de mayor a menor la columna sueldo
    df.drop_duplicates("Nombres",keep="last",inplace=True)#Eliminamos todas las filas excepto la ultima
    Columna_nueva()

#Crear Columna 
def Columna_nueva():
    Rol1=["Estudiante","Docente"]
    df["Rol"]=np.random.choice(Rol1,size=21,replace=True)
    print(df)


def Docente():
    
    for Id,indice in df.iterrows():#iterar filas
        Nombre=(indice["Nombres"])
        Edad=(indice["Edad"])
        Sueldo=(indice["Sueldo"])
        Rol=(indice["Rol"])
        if Rol =="Docente":
            d=["Universidad","Basica","Media"]
            Educacion=(random.choice(d))
            D=docente(Nombre,Edad,Sueldo,Rol,Educacion,"")
            D.Asignatura()
            Lista_D.append(D.__str__())
            df2=pd.DataFrame(Lista_D)
            print(df2)


def Estudiante():
       
       for Id,indice in df.iterrows():#iterar filas y columnas
        Nombre=(indice["Nombres"])
        Edad=(indice["Edad"])
        Sueldo=(indice["Sueldo"])
        Rol=(indice["Rol"])
        if Rol =="Estudiante":
            ed=["Diurno","Vespertino","Online"]
            for i in range(1):
                Horario=(random.choice(ed))
            E=estudiante(Nombre,Edad,Sueldo,Rol,Horario,"")
            E.Actualidad()
            Lista_E.append(E.__str__())
            df1=pd.DataFrame(Lista_E)
            print(df1)
        
        
        


def Excel_E():
    df1=pd.DataFrame(Lista_E)
    df1.to_excel("Excel Estudiantes.xlsx",index=False)

def Excel_D():  
   df2=pd.DataFrame(Lista_D)
   writer=ExcelWriter("Docentes.xlsx")
   df2.to_excel(writer,"Hoja",index=False)
   #writer.save
   #Profe intente de las 2 formas pero no me funciono ninguna 


def Excel():
    Excel_E()
    Excel_D()
    print("Excel creados")

    


def menu():
    leer=int(input("Ingrese 1 Para ver el archivo sin limpieza  -Ingrese 2 para verlo limpio   (Debe limpiar el archvio para poder acceder a las otras funciones)"))
    if leer==1:
        Datos()
        return menu()
    while leer==2:
        filtro()
        L2=int(input("1.Volver al Menu principal 2.Crear lista de estudiantes 3.Crear lista de docente"))
        if L2==1:
            return menu()
        elif L2==2:
            Estudiante()
            print(Lista_E)
            L3=int(input("1-Volver 2-Finalizar"))
            if L3==1:
                menu()
            elif L3==2:
                print("Finalizado")
                break
            else:
                print("Incorrecto,Volviendo al Menu")
                menu()
        elif L2==3:
            Docente()
            print(Lista_D)
            L3=int(input("1-Volver 2-Finalizar"))
            if L3==1:
                menu()
            elif L3==2:
                print("Finalizado")
                break
            else:
                print("Incorrecto,Volviendo al Menu")
                return menu()
        else:
            print("Incorrecto,Volviendo al menu principal")
            return menu()
    else:
        print("Incorrecto")
        menu()

        

menu()
