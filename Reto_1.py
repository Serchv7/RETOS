import re
#VARIABLES----------------------------------------------------------------------    
List_Materiales = []
List_MatSort = []
Minimo = {}
Maximo = {}

#FUNCIONES----------------------------------------------------------------------
def Val_fecha(fecha):
    dia, mes, anio = fecha.split("/") # Separa la fecha en variables segun el separador "/"" - 3 Variables
    if len(dia) == 2 and len(mes) == 2 and len(anio) == 4: # Valida la cantidad de digitos segun corresponda
        if dia.isdigit() and mes.isdigit() and anio.isdigit(): # Valida que efectivamente sean digitos
            if 1<= int(dia) <= 31 and 1 <= int(mes) <= 12 and 1900 <= int(anio) <= 2025: #Valida que la fecha este dentro de los rangos comunes
                print("Fecha valida")
                Val = True
            else:
                print("Fecha erronea: El dia, mes o año es erróneo - Intente de nuevo")
                Val = False
        else:
            print("Fecha erronea: Los valores de la fecha no son numericos - Intente de nuevo")
            Val = False
    else:
        print("Fecha erronea: Los valores de la fecha estan fuera del rango o no existen - Intente de nuevo")
        Val = False
    return Val

def Val_nombre(material):
    if re.fullmatch(r'[a-zA-Z0-9 ]+', material): # Valida que los caracteres esten entre a-z, A-Z, 0-9 y espacios
        print("Texto valido")
        Val = True
    else:
        print("Texto invalido: Solo se permiten letras, numeros y espacios - Intente de nuevo")
        Val = False
    return Val

def Val_resultado (resultado):
    if resultado.isdigit():
        print("Resultado valido")
        resultado = float(resultado)
    else:
        print("Resultado incorrecto: El valor no es numerico")

   # if isinstance(resultado,int) or isinstance(resultado,float):
        # print("Resultado valido")
    # else:
        # print("Resultado incorrecto: El valor no es numerico")

def add_exp(fecha, material, resultado1, resultado2, resultado3, resultado4 ): # Creal el diccionario del material

    Dic_exp = {"Fecha": fecha, 
               "Material": material, 
               "Resultados" : [resultado1, resultado2, resultado3, resultado4]} 
    return Dic_exp

def add_To_listMat(Dict_Material: dict):
    
    List_Materiales.append(Dict_Material)

def Show_listMat(List_Materiales: list):

    print("{:<5} {:<12} {:<10} {:<10} {:<10} {:<10} {:<10}".format("#","Fecha","Material", "250 Hz", "500 Hz", "1 KHz", "2 KHz"))
    print("{:<5} {:<12} {:<10} {:<10} {:<10} {:<10} {:<10}".format("---","----------","---------","------","------","------","------"))
    x = 0

    for dict in List_Materiales:
        x += 1
        print("{:<5} {:<12} {:<10} {:<10} {:<10} {:<10} {:<10}".format(x, dict["Fecha"], dict["Material"], dict["Resultados"][0], dict["Resultados"][1], dict["Resultados"][2], dict["Resultados"][3]))

def Edit_name(List_Materiales: list, indice_mat, New_name):

    indice_mat -= 1 # Actualiza el indice para buscar la posicion correcta en la lista
    List_Materiales[indice_mat]["Material"] = New_name

def Edit_result(List_Materiales: list, indice_mat, new_r1, new_r2, new_r3, new_r4):

    indice_mat -= 1 # Actualiza el indice para buscar la posicion correcta en la lista
    
    List_Materiales[indice_mat]["Resultados"][0]= new_r1
    List_Materiales[indice_mat]["Resultados"][1]= new_r2
    List_Materiales[indice_mat]["Resultados"][2]= new_r3
    List_Materiales[indice_mat]["Resultados"][3]= new_r4
    
def Edit_date(List_Materiales: list, indice_mat, New_date):
    
    indice_mat -= 1 # Actualiza el indice para buscar la posicion correcta en la lista
    
    List_Materiales[indice_mat]["Fecha"] = New_date
 
def Del_listMat(List_Materiales: list, indice_mat):

    indice_mat -= 1 # Actualiza el valor del indice para acceder a la posicion real de la lista
    List_Materiales.pop(indice_mat) # Elimina el material en la posicion escogida
    print("\nMaterial eliminado correctamente")  

def Calc_NRC(List_Materiales: list):
    
    for dict in List_Materiales:
        Promedio1 = lambda a,b,c,d : round((a+b+c+d)/4,2) #Funcion que realiza el promedio de los datos
        dict["NRC"]= Promedio1(dict["Resultados"][0],dict["Resultados"][1],dict["Resultados"][2],dict["Resultados"][3]) # Se agrega el promedio a la lista de materiales

def Show_listRst(List_Materiales: list):

    print("{:<5} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("#","Material", "250 Hz", "500 Hz", "1 KHz", "2 KHz", "NRC")) # Imprime titulos 
    print("{:<5} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("---","---------","------","------","------","------","------")) # Imprime separadores 
    x = 0

    for dict in List_Materiales:
        x += 1
        print("{:<5} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(x, dict["Material"], dict["Resultados"][0], dict["Resultados"][1], dict["Resultados"][2], dict["Resultados"][3], dict["NRC"])) # Imprime los resultados

def Export_file(List_Materiales: list, List_MatSort: list, Minimo: dict, Maximo: dict):
    with open("Informe de Resultados - Absorción Acústica.txt","w") as file:
        file.write("Materiales - Absorción Acústica")

        file.write("\n{:<5} {:<12} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("#","Fecha","Material","250 Hz","500 Hz","1 KHz","2 KHz","NRC"))
        file.write("\n{:<5} {:<12} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("---","----------","---------","------","------","------","------","-----"))
        x = 0

        for dict in List_Materiales:
            x += 1
            file.write("\n{:<5} {:<12} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(x, dict["Fecha"], dict["Material"], dict["Resultados"][0], dict["Resultados"][1], dict["Resultados"][2], dict["Resultados"][3], dict["NRC"]))

        file.write("\nMateriales - Absorción Acústica (Ordenados)")

        file.write("\n{:<5} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("#","Material", "250 Hz", "500 Hz", "1 KHz", "2 KHz", "NRC")) # Imprime titulos 
        file.write("\n{:<5} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("---","---------","------","------","------","------","------")) # Imprime separadores 
        x = 0

        for dict in List_MatSort:
            x += 1
            file.write("\n{:<5} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(x, dict["Material"], dict["Resultados"][0], dict["Resultados"][1], dict["Resultados"][2], dict["Resultados"][3], dict["NRC"])) # Imprime los resultados

        file.write(f"\nEl mayor valor de NRC es de: {Maximo["NRC"]} y corresponde al material: {Maximo["Material"]}")
        file.write(f"\nEl menor valor de NRC es de: {Minimo["NRC"]} y corresponde al material: {Minimo["Material"]}")

        file.close()


#PROGRAMA ----------------------------------------------------------------------
while True:
    #MENU DE OPCIONES
    print("\nBienvenido al Programa de Cálculo de Calidad Acústica ")
    print("1. Agregar material")
    print("2. Ver lista de materiales")
    print("3. Modificar material")
    print("4. Eliminar material")
    print("5. Cálcular NRC del material")
    print("6. Comparacion de materiales")
    print("7. Exportar informacion")
    print("8. Salir")
    
    menu = int(input("\nSeleccione una opción del menu: "))

    if menu == 1: # AGREGAR MATERIAL
        #Se ingresa los datos del experimento (fecha, nombre y resultado)
        while True: # Pregunta la fecha hasta que sea valida
            fecha = input("\nIngrese la fecha de las mediciones (DD/MM/AAAA): ")

            if Val_fecha(fecha): # Verifica (True/False) si la fecha es aceptada o no para pasar al siguiente item
                break

        while True:
            material = input("\nIngrese el nombre del material: ")

            if Val_nombre(material): # Verifica (True/False) si el nombre es aceptada o no para pasar al siguiente item
                break

        resultado1 = round(float(input("\nIngrese la abs en la banda de 250 Hz: ")),2)
        resultado2 = round(float(input("\nIngrese la abs en la banda de 500 Hz: ")),2)
        resultado3 = round(float(input("\nIngrese la abs en la banda de 1KHz: ")),2)
        resultado4 = round(float(input("\nIngrese la abs en la banda de 2KHz: ")),2)
        #Val_resultado(resultado)

        Dict_Material = add_exp(fecha, material, resultado1, resultado2, resultado3, resultado4) #Creamos un diccionario del material agregado

        add_To_listMat(Dict_Material)
        print("\nMaterial agregado correctamente")

        Calc_NRC(List_Materiales) #Calcula el promedio de resultados de una vez


    elif menu == 2: # VER MATERIALES AGREGADOS
    
        if len(List_Materiales) != 0: # Evalua si se han agregado experimentos

            Show_listMat(List_Materiales) # Muestra los experimentos agregados

        else:
            print("\nAun no se han agregado materiales al programa - Intente de nuevo")
        
    elif menu == 3: # EDITAR MATERIAL

        if len(List_Materiales) != 0:

            Show_listMat(List_Materiales) # Muestra los experimentos agregados
            indice_mat = int(input("\n¿Que material desea modificar?:"))
            
            while True: # Menu de acciones

                print("\n¿Que item desea modificar ?: ")
                print("1. Nombre del material")
                print("2. Resultados")
                print("3. Fecha")
                print("4. Regresar al menú principal")
                menu = int(input("\nSeleccione una opción: "))

                if menu == 1:

                    while True:

                        new_name=input("Ingrese el nuevo nombre del material: ")# Solicita el nuevo nombre

                        if Val_nombre(new_name): #Valida que el nombre sea correcto
                            break

                    Edit_name(List_Materiales, indice_mat, new_name) #Edita únicamente el nombre del material según el indice dado

                elif menu == 2:

                    new_r1 = float(input("\nIngrese la abs en la banda de 250 Hz: "))
                    new_r2 = float(input("\nIngrese la abs en la banda de 500 Hz: "))
                    new_r3 = float(input("\nIngrese la abs en la banda de 1KHz: "))
                    new_r4 = float(input("\nIngrese la abs en la banda de 2KHz: "))
                    Edit_result(List_Materiales, indice_mat, new_r1, new_r2, new_r3, new_r4)
                
                elif menu == 3:
                    
                    while True:

                        new_date = input("Ingrese la nueva fecha del experimento: ") # Solicita la nueva fecha
                        
                        if Val_fecha(new_date): #Valida que la fecha sea correcta 
                            break

                    Edit_date(List_Materiales, indice_mat, new_date) #Edita únicamente la fecha del experimento según el indice dado

                elif menu == 4:
                    break

        else:

            print("\nAun no se han agregado materiales al programa - Intente de nuevo")



    elif menu == 4: # ELIMINAR MATERIAL

        if len(List_Materiales) != 0:

            Show_listMat(List_Materiales) # Muestra nuevamente la lista de materiales

            indice_mat = int(input("\nCon base en la lista, ingrese el indice del material que desea eliminar: ")) # Solicita el material que se quiere eliminar
            Del_listMat(List_Materiales, indice_mat)

        else:

            print("\nAun no se han agregado materiales al programa - Intente de nuevo")          

    elif menu == 5: # CALCULO NRC

        if len(List_Materiales) != 0:

            Show_listRst(List_Materiales) # Muestra la lista de materiales con el promedio de resultados

        else:

            print("\nAun no se han agregado materiales al programa - Intente de nuevo")

    elif menu == 6:

        if len(List_Materiales) != 0:

            Minimo = min(List_Materiales, key=lambda k: k["NRC"]) # Evalua cual valor de NRC de todos los diccionarios es el menor
            Maximo = max(List_Materiales, key=lambda k: k["NRC"]) # Evalua cual valor de NRC de todos los diccionarios es el mayor
            List_MatSort = sorted(List_Materiales, key=lambda k: k["NRC"]) # Busca el valor de la llave en cada diccionario de la lista y ordena de mneor a mayor
            
            print("\nA continuación se presentan los materiales ordenados de menor a mayor absorción acústica: ")
            Show_listRst(List_MatSort)# Se orden la lista de menor a mayor valor de NRC

            print("\nEl mayor valor de NRC es de: ", Maximo["NRC"], "y corresponde al material: ", Maximo["Material"])
            print("El menor valor de NRC es de: ", Minimo["NRC"], "y corresponde al material: ", Minimo["Material"])

        else:
             
             print("\nAun no se han agregado materiales al programa - Intente de nuevo")


    elif menu == 7:
        
        if len(List_Materiales) != 0 and len(List_MatSort) != 0:

            Export_file(List_Materiales, List_MatSort, Minimo, Maximo) # Exporta el informe de resultados en un archivo .txt

        else:
            print("\nAun no se encuentra la informacion completa para generar el informe - Intente de nuevo")

    if menu == 8:
        print("\nFin del programa")
        break