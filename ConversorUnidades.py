1
#Antes de iniciar instalar la libreria Numpy
#En CMD inicial el comando:
# pip install numpy

#Llamado a NumPy

import numpy as np
#Declaracion del vector "vecDatos"
vecDatos = np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7])

#Declaracion Constante
consSeparador = "============================="



#Funciones en comun(Modularidad y reduccion de lineas de codigo)


def Imprimir(prmVector,prmMensaje):
    print(prmMensaje)
    for varContador in [1,2,3,4,5,6]:
        print("{:.3f}".format(prmVector[varContador]))
        if varContador == 3:
            print("================================")

#Funciones conversoras (Modularidad y reduccion de lineas de codigo)

def conversora(prmValor):
    varAux1 = prmValor 
    varAux2 = prmValor 
    vecDatos[1]= prmValor
    for varContador in [2,3,4,5,6]:
        if varContador <=3:
            varAux1 = varAux1 * 10
            vecDatos[varContador] = varAux1
        else:
            varAux2 = varAux2/10
            vecDatos[varContador] = varAux2  


#Funciones independientes

def distancia(prmValor):
    print(consSeparador)
    conversora(prmValor)
    print( prmValor ,"Metros son:",prmValor *1.0936 , "Yardas")
    print( prmValor ,"Metros son:",prmValor *39.39, "Pulgadas")
    print( prmValor ,"Metros son:",prmValor *3.281 , "Pies")
    print( prmValor ,"Metros son:",prmValor *0.0006214 , "Millas")
    return  Imprimir(vecDatos,"Conversion en SI: los resultados se muestran con el siguiente orden [metro,decimetro,centimetro / decametros,hectometro,kilometros]")
        
 
def masa (prmValor):
    print(consSeparador)
    conversora(prmValor)
    print( prmValor ,"Gramos son:",prmValor *0.0022046 , "Onzas")
    print( prmValor ,"Gramos son:",prmValor *0.0000011023, "Libras")
    return  Imprimir(vecDatos,"Conversion en SI: los resultados se muestran con el siguiente orden [gramo,decigramo,centigramo / decagramo,hectogramo,kilogramo]")
        

def tiempo ():
    print(consSeparador)
    print("Seleccione la unidad de tiempo a ingresar (1. Seguntos, 2. Minutos , 3. Horas ,  4. dia , 5.Años)")
    argument = int(input("Selecione una opcion: "))
    varValor = int(input("Ingrese el valor de la unidad a convertir"))
    if(argument==1):
        tiempo_s(varValor)
    if(argument==2):
        tiempo_m(varValor)
    if(argument==3):
        tiempo_h(varValor)
    if(argument==4):
        tiempo_d(varValor)
    if(argument==5):
        tiempo_a(varValor)
#Sub Opciones tiempo    
def tiempo_s(prmValor):
    print(consSeparador)
    print(prmValor,"Segundos son: " ,prmValor / 60 ,"Minutos")
    print(prmValor,"Segundos son: " ,(prmValor / 60 )/60,"Horas")
    print(prmValor,"Segundos son: " ,((prmValor / 60 )/60)/24 ,"dias")
    print(prmValor,"Segundos son: " ,(((prmValor / 60 )/60)/24)/365 ,"años")

def tiempo_m(prmValor):
    print(consSeparador)
    print(prmValor,"Minutos son: " ,prmValor * 60 ,"Segundos")
    print(prmValor,"Minutos son: " ,prmValor / 60 ,"Horas")
    print(prmValor,"Minutos son: " ,((prmValor / 60 )/24) ,"dias")
    print(prmValor,"Minutos son: " ,((prmValor / 60 )/24)/365 ,"años")
def tiempo_h(prmValor):
    print(consSeparador)
    print(prmValor,"Horas son: " ,(prmValor * 60)*60 ,"Segundos")
    print(prmValor,"Horas son: " ,prmValor * 60 ,"Minutos")
    print(prmValor,"Horas son: " ,(prmValor / 24) ,"dias")
    print(prmValor,"Horas son: " ,(prmValor/24)/365 ,"años")
def tiempo_d(prmValor):
    print(consSeparador)
    print(prmValor,"Dias son: " ,((prmValor * 24)*60)*60 ,"Segundos")
    print(prmValor,"Dias son: " ,(prmValor * 24)*60 ,"Minutos")
    print(prmValor,"Dias son: " ,(prmValor * 24 ) ,"Horas")
    print(prmValor,"Dias son: " ,(prmValor/365) ,"años")
def tiempo_a(prmValor):
    print(consSeparador)
    print(prmValor,"Años son: " ,(((prmValor *365) * 24)*60)*60  ,"Segundos")
    print(prmValor,"Años son: " ,(((prmValor *365) * 24)*60)  ,"Minutos")
    print(prmValor,"Años son: " ,((prmValor *365) * 24)   ,"Horas")
    print(prmValor,"Años son: " ,(prmValor *365) ,"Dias")

def corrienteElectrica(prmValor):
    conversora(prmValor)
    return  Imprimir(vecDatos,"Conversion en SI: los resultados se muestran con el siguiente orden [Amper,deciamper,centiamper / decaamper,hectoamper,kiloamper]")
def temperatura():
    print(consSeparador)
    print("Seleccione la unidad de tiempo a ingresar (1. Celsius, 2. Fahrenheit , 3. Kelvin )")
    argument = int(input("Selecione una opcion: "))
    varValor = int(input("Ingrese el valor de la unidad a convertir"))
    if(argument==1):
        temp_c(varValor)
    if(argument==2):
        temp_f(varValor)
    if(argument==3):
        temp_k(varValor)

#Sub Opciones temperatura
def temp_c(prmValor):
    print(prmValor ,"Celcius son ",prmValor + 273.15 ,"Grados Kelvin") 
    print(prmValor ,"Celcius son ",((9*prmValor)/5)+32,"Grados Fahrenheit") 
def temp_f(prmValor):
    print(prmValor ,"Fahrenheit son ",(5(prmValor-32))/9,"Grados Celcius") 
    print(prmValor,"Fahrenheit son ",((5(prmValor-32))/9)+273.15,"Grados Kelvin") 
def temp_k(prmValor):
    print(prmValor ,"Kelvin son ",prmValor - 273.15,"Grados Celcius") 
    print(prmValor ,"Kelvin son ",((9*(prmValor-273))/5)+32,"Grados Fahrenheit") 




        

#Programa principal

print("================Bienvenido al conversor================")
print("1. Conversor de distancia")
print("2. Conversor de masa")
print("3. Conversor de tiempo")
print("4. Conversor de Corriente electrica")
print("5. Conversor de temperatura")
print("6. Salir")
argument = int(input("Selecione una opcion: "))

if argument == 1:
    distancia(int(input("Ingrese la distancia EN METROS a convertir: ")))
if argument == 2:
    masa(int(input("Ingrese la masa EN GRAMOS a convertir: ")))
if argument == 3:
    tiempo()
if argument == 4:
    corrienteElectrica(int(input("Ingrese la masa EN AMPERIOS a convertir: ")))
if argument == 5:
    temperatura()
if argument == 6:
    print('FIN')

