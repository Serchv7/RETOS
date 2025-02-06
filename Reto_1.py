import re

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

    Dic_exp = {material : [resultado1, resultado2, resultado3, resultado4, fecha]} 
    return Dic_exp

def add_To_listMat(Dict_Material: dict):
    
    List_Materiales.append(Dict_Material)

    return List_Materiales

def Show_listMat(List_Materiales: list):

    print("{:<5} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("#","Material", "250 Hz", "500Hz", "1KHz", "2KHz", "Fecha"))
    print("{:<5} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("---","---------", "------", "-----", "-----", "-----", "----------"))
    x = 0

    for pos in List_Materiales:
        x += 1
        for key,value in pos.items():
            print("{:<5} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(x, key, value[0], value[1], value[2], value[3], value[4]))

def Edit_name(List_Materiales: list, indice_mat, New_name):

    indice_mat -= 1 # Actualiza el indice para buscar la posicion correcta en la lista
    Names=list(List_Materiales[indice_mat].keys()) # Obtiene lista de nombres

    List_Materiales[indice_mat][New_name] = List_Materiales[indice_mat].pop(Names[0]) #Reemplaza el nombre

    return List_Materiales

def Edit_result(List_Materiales: list, indice_mat, new_r1, new_r2, new_r3, new_r4):

    indice_mat -= 1 # Actualiza el indice para buscar la posicion correcta en la lista

    for key,value in List_Materiales[indice_mat].items(): #Itera y accede al diccionario 
        value[0] = new_r1 # Se reemplaza el valor actual por el valor nuevo
        value[1] = new_r2
        value[2] = new_r3
        value[3] = new_r4
    
    return List_Materiales

def Edit_date(List_Materiales: list, indice_mat, New_date):
    
    indice_mat -= 1 # Actualiza el indice para buscar la posicion correcta en la lista

    for key,value in List_Materiales[indice_mat].items(): #Itera y accede al diccionario 
        value[4] = New_date # Se reemplaza el valor actual por el valor nuevo
    
    return List_Materiales


def Del_listMat(List_Materiales: list, indice_mat):

    indice_mat -= 1 # Actualiza el valor del indice para acceder a la posicion real de la lista
    List_Materiales.pop(indice_mat) # Elimina el material en la posicion escogida
    print("\nMaterial eliminado correctamente")  

    return List_Materiales #Actualiza la lista de materiales

#VARIABLES----------------------------------------------------------------------    
List_Materiales = []

#PROGRAMA ----------------------------------------------------------------------
while True:
    #MENU DE OPCIONES
    print("\nBienvenido al Programa de Cálculo de Calidad Acústica ")
    print("1. Agregar material")
    print("2. Ver lista de materiales")
    print("3. Modificar material")
    print("4. Eliminar material")
    print("5. Cálcular NRC y RT Mid")
    print("6. Comparacion de materiales")
    print("7. Salir")
    
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

        resultado1 = float(input("\nIngrese la abs en la banda de 250 Hz: "))
        resultado2 = float(input("\nIngrese la abs en la banda de 500 Hz: "))
        resultado3 = float(input("\nIngrese la abs en la banda de 1KHz: "))
        resultado4 = float(input("\nIngrese la abs en la banda de 2KHz: "))
        #Val_resultado(resultado)

        Dict_Material = add_exp(fecha, material, resultado1, resultado2, resultado3, resultado4) #Creamos un diccionario del material agregado
        add_To_listMat(Dict_Material)
        print("\nMaterial agregado correctamente")


    elif menu == 2: # VER MATERIALES AGREGADOS
    
        if len(List_Materiales) != 0: # Evalua si se han agregado experimentos

            Show_listMat(List_Materiales) # Muestra los experimentos agregados

        else:
            print("\nAun no se han agregado materiales al programa - Intente de nuevo")
        
    elif menu == 3: # EDITAR MATERIAL
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

                new_name=input("Ingrese el nuevo nombre del material: ")
                Edit_name(List_Materiales, indice_mat, new_name)

            elif menu == 2:

                new_r1 = float(input("\nIngrese la abs en la banda de 250 Hz: "))
                new_r2 = float(input("\nIngrese la abs en la banda de 500 Hz: "))
                new_r3 = float(input("\nIngrese la abs en la banda de 1KHz: "))
                new_r4 = float(input("\nIngrese la abs en la banda de 2KHz: "))
                Edit_result(List_Materiales, indice_mat, new_r1, new_r2, new_r3, new_r4)
            
            elif menu == 3:
                
                new_date = input("Ingrese la nueva fecha del experimento: ")
                Edit_date(List_Materiales, indice_mat, new_date)

            elif menu == 4:
                break



    elif menu == 4: # ELIMINAR MATERIAL

        Show_listMat(List_Materiales) # Muestra nuevamente la lista de materiales

        indice_mat = int(input("\nCon base en la lista, ingrese el indice del material que desea eliminar: ")) # Solicita el material que se quiere eliminar
        Del_listMat(List_Materiales, indice_mat)       

    else:

        print(menu)

    if menu == 7:
        print("\nFin del programa")
        break

print("Hola")