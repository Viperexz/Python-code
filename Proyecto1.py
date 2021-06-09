class Paciente:
    def __init__(self,Cedula=0,Nombre="",Enfermedad="",Edad=0,Sexo=""):
        self.Cedula=Cedula
        self.Nombre=Nombre
        self.Enfermedad=Enfermedad
        self.Edad=Edad
        self.Sexo=Sexo

matrizHospital = (
[Paciente(0,0,0,0,0),Paciente(0,0,0,0,0),Paciente(0,0,0,0,0),Paciente(0,0,0,0,0)],
[Paciente(0,0,0,0,0),Paciente(0,0,0,0,0),Paciente(0,0,0,0,0),Paciente(0,0,0,0,0)],
[Paciente(0,0,0,0,0),Paciente(0,0,0,0,0),Paciente(0,0,0,0,0),Paciente(0,0,0,0,0)],
[Paciente(0,0,0,0,0),Paciente(0,0,0,0,0),Paciente(0,0,0,0,0),Paciente(0,0,0,0,0)],
[Paciente(0,0,0,0,0),Paciente(0,0,0,0,0),Paciente(0,0,0,0,0),Paciente(0,0,0,0,0)])



varPiso1=0
varPiso2=0
varPiso3=0
varPiso4=0
varPiso5=0

def Mostrar(prmVector):
    for varColumna in range(5):
        for varContador in range(4):
            if(prmVector[varColumna][varContador].Cedula == 0):
                print("\t","['0']",end="")
            else:
                print("\t","[",prmVector[varColumna][varContador].Cedula ,prmVector[varColumna][varContador].Nombre, prmVector[varColumna][varContador].Enfermedad, prmVector[varColumna][varContador].Edad ,prmVector[varColumna][varContador].Sexo,"]",end="")
        print()


def OcupacionHabitacion(varPiso):
    varContador = 0
    varAux = 0
    if(varPiso == 1):
        for varContador in range(4):
            if(matrizHospital[1][varContador].Cedula == 0):
                varAux = varAux +1
        print("Habitaciones disponibles: " , varAux)
        return varAux       
    if(varPiso == 2):
        for varContador in range(4):
            if(matrizHospital[2][varContador].Cedula == 0):
                varAux = varAux +1
        print("Habitaciones disponibles: " , varAux)
        return varAux          
    if(varPiso == 3):
        for varContador in range(4):
            if(matrizHospital[3][varContador].Cedula == 0):
                varAux = varAux +1
        print("Habitaciones disponibles: " , varAux)
        return varAux          
    if(varPiso == 4):
        for varContador in range(4):
            if(matrizHospital[4][varContador].Cedula == 0):
                varAux = varAux +1
        print("Habitaciones disponibles: " , varAux)
        return varAux          
    if(varPiso == 5):
        for varContador in range(4):
            if(matrizHospital[5][varContador].Cedula == 0):
                varAux = varAux +1
        print("Habitaciones disponibles: " , varAux)
        return varAux           


def RetirarPaciente(prmVector,prmCedula):
    for varColumna in range(5):
        for varContador in range(4):
            if(prmVector[varColumna][varContador].Cedula == prmCedula):
                matrizHospital[varColumna][varContador] = Paciente(0,0,0,0,0)




def RegistrarPaciente(varPiso):
    if(varPiso == 1):
            if(varPiso1 !=5):
                print("***** Cuidados intensivos *****")
                matrizHospital[0][varPiso1] = Paciente(int(input("Cedula: ")),input("Nombre:"),input("Enfermedad: "),int(input("Edad: ")),input("Sexo: "))
                varPiso1+1
            else:
                print("Piso lleno.")
    if(varPiso == 2):
            if(varPiso2 !=5):
                print("***** Cuidados intermedios *****")
                matrizHospital[1][varPiso2] = Paciente(int(input("Cedula: ")),input("Nombre:"),input("Enfermedad: "),int(input("Edad: ")),input("Sexo: "))
                varPiso2+1
            else:
                print("Piso lleno.")
    if(varPiso == 3):
            if(varPiso3 !=5):
                print("***** Urgencias *****")
                matrizHospital[2][varPiso3] = Paciente(int(input("Cedula: ")),input("Nombre:"),input("Enfermedad: "),int(input("Edad: ")),input("Sexo: "))
                varPiso3+1
            else:
                print("Piso lleno.")
    if(varPiso == 4):
            if(varPiso4 !=5):
                print("***** Recuperacion *****")
                matrizHospital[3][varPiso4] = Paciente(int(input("Cedula: ")),input("Nombre:"),input("Enfermedad: "),int(input("Edad: ")),input("Sexo: "))
                varPiso4+1
            else:
                print("Piso lleno.")
    if(varPiso == 5):
            if(varPiso5 !=5):
                print("***** Recuperacion *****")
                matrizHospital[4][varPiso5] = Paciente(int(input("Cedula: ")),input("Nombre:"),input("Enfermedad: "),int(input("Edad: ")),input("Sexo: "))
                varPiso5+1
            else:
                print("Piso lleno.")



def BuscarPaciente(prmVector,prmCedula):
    for varColumna in range(5):
        for varContador in range(4):
            if(prmVector[varColumna][varContador].Cedula == prmCedula):
                print("El paciente esta en el piso:", varColumna+1 ,"Con habitacion: ", varContador+1 )
    print("El paciente no existe.")


def MoverPaciente(prmVector,prmCedula,prmPiso):
    varAux = Paciente
    for varColumna in range(5):
        for varContador in range(4):
            if(prmVector[varColumna][varContador].Cedula == prmCedula):
                varAux = prmVector[varColumna][varContador]
    print("El paciente no existe.")
    
    if OcupacionHabitacion(prmPiso) != 0 :
        for varContador in range(4):
            if(prmVector[prmPiso][varContador].Cedula == 0):
                prmVector[prmPiso][varContador] = varAux




#Programa principal
varBandera = True
while varBandera:
    print("================SOFTWARE DE LA CLINICA BIENVENIDOS================")
    print("1. Conocer el cupo de un piso")
    print("2. Registrar un paciente")
    print("3. Retirar un paciente")
    print("4. Buscar un paciente")
    print("5. Mover un paciente de piso")
    print("6. Mostrar ocupacion de la clinica")
    print("0. SALIR")
    argument = int(input("Selecione una opcion: "))

    if argument == 1:
        print("================Cupo de un piso================")
        OcupacionHabitacion(int(input("Ingrese el piso: ")))
        
    if argument == 2:
        print("================Registrar un paciente================")
        RegistrarPaciente(varPiso = int(input("Ingrese el piso: ")))

    if argument == 3:
        print("================Retirar un paciente================")
        RetirarPaciente(matrizHospital,int(input("Ingrese la cedula del paciente")))
    if argument == 4:
        print("================Buscar un paciente================")
        BuscarPaciente(matrizHospital,int(input("Ingrese la cedula del paciente")))
    if argument == 5:
        print("================Mover un paciente================")
        print('FIN')
    if argument == 6:
        print("================ Ocipacion de la clinica ================")
        Mostrar(matrizHospital)
    if argument == 0:
        print('FIN')
        varBandera = False