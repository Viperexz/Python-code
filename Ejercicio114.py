#
## UVa 114 Solucion   
#
#
#Importa la clase Numpy
import numpy as np
from numpy.core.fromnumeric import shape

#Se define la clase pared 
class Pared:
    def __init__(self,x=0,y=0,valor=0,costo=0):
        self.x=x
        self.y=y
        self.valor=valor
        self.costo=costo
    def nuevaPared(self,x=0,y=0,valor=0,costo=0):
        nuevaPared = x , y, valor,costo
        self.x=x
        self.y=y
        self.valor=valor
        self.costo=costo
        print("Se agregaron los datos")
        return nuevaPared
#Se define la clase pelora
class Pelota:
    def __init__(self,x=0,y=0,direccion=0,lifetime=0):
        self.x=x
        self.y=y
        self.direccion=direccion
        self.lifetime=lifetime

def añadir_objeto (arreglo,objeto):
    arreglo.append(objeto)
    print("Añadido")
#Se crean un arreglo bidimensional como cuadricula
cuadricula =np.zeros(shape=(3,3))
#Ingresa m
m = int(input("Ingrese datos para m: "))
#Ingresa n
n = int(input("Ingrese datos para n: "))
#Ingresa costo_pared
costo_pared = int(input("Ingrese datos para costo_pared: "))
#ingreso p
p = int(input("Ingrese datos para p: "))

#Crea el vector paredes para almacenar las paredes del juego 
vecParedes=[Pared]
for varContador in range(p):
    X = int(input("X: "))
    Y = int(input("Y: "))
    añadir_objeto(vecParedes,Pared(X,Y,int(input("Valor: ")),int(input("Costo: "))))
    print( varContador )
    cuadricula[X,Y] = varContador
#Se crea una variable con la estructura con el numero de pelotas creadas.
numero_pelotas = 0
vecPelotas=[Pelota]
for varContador in range(p):
    X = int(input("X: "))
    Y = int(input("Y: "))
    añadir_objeto(vecPelotas,Pelota(X,Y,int(input("Direccion: ")),int(input("Lifetime: "))))
    print(varContador)
    cuadricula[X,Y] = varContador
    numero_pelotas+1
#Se instancias la variable puntaje total con inicializacion en 0;
puntaje_total = 0

for varContador in range(numero_pelotas):
    puntaje= 0
    #Se crea un while con la vida de la pelota hasta que 0 
    while vecPelotas[varContador].lifetime>0 :
        posicion_x = vecPelotas[varContador].x
        posicion_y = vecPelotas[varContador].y
        if(vecPelotas[varContador].direccion==1):
            posicion_x+1
        if(vecPelotas[varContador].direccion==1):
            posicion_y+1
        if(vecPelotas[varContador].direccion==1):
            posicion_x-1
        if(vecPelotas[varContador].direccion==1):
            posicion_y-1
        else:
            break
        turn = False
        if(posicion_x <1 or posicion_x > m or posicion_y<1 or posicion_y >n):
            turn = True
            vecPelotas[varContador].lifetime = vecPelotas[varContador].lifetime - costo_pared

        if cuadricula[posicion_y][posicion_x] != 0 :
            turn = True
            vecPelotas[varContador].lifetime = vecPelotas[varContador].lifetime -  vecParedes[cuadricula[posicion_y][posicion_x]].costo

        if turn:
            vecPelotas[varContador].direccion = (vecPelotas[varContador].direccion + 4 -1) % 4
        else:
            vecPelotas[varContador].x = posicion_x
            vecPelotas[varContador].y = posicion_y
            vecPelotas[varContador].lifetime -1
        if vecPelotas[varContador].lifetime <= 0:
            puntaje_total = puntaje
            print(puntaje)

print(puntaje_total)   
            
        

