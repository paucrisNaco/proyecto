
import datetime
import random

#Datos de la quiniela
nombrequiniela="Quiniela Los Amigos =)"
direccion="Bv Roca esq. M. de Lorenzi"

#Fecha y hora
fecha_hora_actual = datetime.datetime.now()
fecha = fecha_hora_actual.strftime("%d-%m-%Y")
hora = fecha_hora_actual.strftime("%H:%M:%S")

#Contadores
numero_comprobante=0
n_arqueo=0

#Listas:
numeros_apuesta={}

#Función 1: escribir las apuestas del juego Quiniela
def escribir_apuesta_quiniela(archivo_nombre, dni, numero_apuesta, importe_quiniela, opcion_elegida, numero_comprobante):
    with open(archivo_nombre, "a") as archivo:
        archivo.write(f"Fecha: {fecha}\n")
        archivo.write(
            f"Dni: {dni} - Numero apuesta: {numero_apuesta} - Importe apuesta: ${importe_quiniela} - Tipo de juego: {opcion_elegida} Quiniela - N° de comprobante: {numero_comprobante}\n"
        )

#Función 2: escribir las apuestas del juego Quini 6
def escribir_apuesta_quini(archivo_nombre, dni, numeros_apuesta, importe_quiniela, opcion_elegida, numero_comprobante):
    with open(archivo_nombre, "a") as archivo:
        archivo.write(f"Fecha: {fecha}\n")
        archivo.write(
            f"Dni: {dni} - Numeros apuesta: {numeros_apuesta} - Importe apuesta: ${importe_quiniela} - Tipo de juego: {opcion_elegida} Quiniela - N° de comprobante: {numero_comprobante}\n"
        )

#Función 3: generar números al azar
def generar_numeros_azar():
    numeros_generados = []
    while len(numeros_generados) < 6:
        numero_aleatorio = random.randint(0, 45)
        if 0 <= numero_aleatorio < 10:
            numero_aleatorio_str = "0" + str(numero_aleatorio)
        else:
            numero_aleatorio_str = str(numero_aleatorio)

        if numero_aleatorio_str not in numeros_generados:
            numeros_generados.append(numero_aleatorio_str)
    print("Los números generados al azar son:", numeros_generados)

#Función 4: leer las apuestas del juego Quiniela
def leer_apuesta_quiniela(archivo_nombre, dni, numero_apuesta):
    with open(archivo_nombre, "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            if f"Dni: {dni} - Numero apuesta: {numero_apuesta}" in linea:
                return True
    return False

#Función 5: leer las apuestas del juego Quini 6
def leer_apuesta_quini6(archivo_nombre, dni, numero_apuesta):
    with open(archivo_nombre, "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            if f"Dni: {dni} - Numeros apuesta: {numeros_apuesta}" in linea:
                return True
    return False

#Función 6: bienvenida
def bienvenida():
    print("Bienvenid@ a nuestro sistema Pybel®")
    print("Fecha:",fecha,"Hora:",hora,)
    print(nombrequiniela)
    print(direccion)
    print("Menú principal:")

#Función 7: arqueo de caja
def arqueo_caja(importe_quiniela, importe_quini):
    total_quiniela=sum(importe_quiniela)
    total_quini=sum(importe_quini)
    total_recaudacion=total_quiniela+total_quini
    retencion=round(total_recaudacion*0.47,2)
    ganancia=total_recaudacion-retencion
    return total_quiniela, total_quini, total_recaudacion, retencion, ganancia

#Función 8: leer archivo para el arqueo
def leer_importes(nombre_archivo):
    importe_quiniela=[]
    importe_quini=[]

    with open(nombre_archivo, "r") as lineas:
        for linea in lineas:
            if "Tipo de juego: 1 Quiniela" in linea:
                importe = float(linea.split("- Importe apuesta: $")[1].split(" ")[0])
                importe_quiniela.append(importe)
            elif "Tipo de juego: 2 Quiniela" in linea:
                importe = float(linea.split("- Importe apuesta: $")[1].split(" ")[0])
                importe_quini.append(importe)    
    return importe_quiniela, importe_quini

#Menú de opciones:
menu = {
    "1": "Quiniela",
    "2": "Quini 6",
    "3": "Comprobar apuesta",
    "4": "Arqueo de caja",
    "5": "Salir"}


#Programa principal
bienvenida()
while True:
    for opcion, descripcion in menu.items():
        print(f"*{opcion} - {descripcion}")

    opcion_elegida = input("Escoja una opción: ")

    if opcion_elegida == "1":
        print("Juego:", menu[opcion_elegida], fecha, hora)

        while True:
            jugar = None
            numero_apuesta = None
            importe_quiniela = None
            dni = None
            imprimir_comprobante = None

            while jugar not in [1, 2]:
                try:
                    jugar = int(input("Para comenzar ingrese 1, para cancelar ingrese 2: "))
                    if jugar == 2:
                        print("Volviendo al menú principal")
                        break
                except ValueError:
                    print("Debe ingresar 1 o 2 para continuar")
                    continue

            if jugar == 2:
                break

            while True:
                try:
                    numero_apuesta = int(input("Ingrese un número de 2, 3 o 4 cifras: "))
                    if numero_apuesta<0 or len(str(numero_apuesta))<2 or len(str(numero_apuesta))>4:
                        raise ValueError
                    break
                except ValueError:
                    print("La opción ingresada no es válida. Intente nuevamente.")

            while True:
                try:
                    importe_quiniela = float(input("Ingrese el importe de la apuesta: $"))
                    break
                except ValueError:
                    print("La opción ingresada no es válida. Intente nuevamente.")

            while True:
                try:
                    dni = int(input("Ingrese el número de DNI sin puntos: "))
                    if len(str(dni)) == 8:
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("La opción ingresada no es válida. Intente nuevamente.")

            escribir_apuesta_quiniela("apuestasAgosto.txt", dni, numero_apuesta, importe_quiniela, opcion_elegida, numero_comprobante)
            numero_comprobante += 1
            print("Apuesta guardada exitosamente", end="\n")
            while imprimir_comprobante not in ("Y", "N",):
                try:
                    imprimir_comprobante = input("Para imprimir el comprobante ingrese Y (si) o N (no): ").upper()
                    if imprimir_comprobante == "Y":
                        print("Imprimiendo comprobante", end="\n")
                        print(" -------------------------------------- ")
                        print("|**************************************|")
                        print("|* Apuestas de", nombrequiniela, "*|")
                        print("|Dirección:",direccion,"|")
                        print("|**************************************|")
                        print("|--------------------------------------|")
                        print("| Juego: Quiniela - N° comprobante:",numero_comprobante," |")
                        print("|--------------------------------------|")
                        print("| Número apostado: ",numero_apuesta, "              |")
                        print("| DNI del cliente:",dni, "           |")
                        print("| Importe de la apuesta: $",importe_quiniela, "     |")
                        print("| ------------------------------------ |")
                        print("| Fecha:",fecha, "    Hora:",hora, "|")
                        print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ")
                        
                    elif imprimir_comprobante == "N":
                        print("No se imprimirá el comprobante.")
                    else:
                        raise ValueError
                except ValueError:
                    print("La opción ingresada no es válida. Intente nuevamente.")

    elif opcion_elegida == "2":
        print("Juego:", menu[opcion_elegida], fecha, hora)
        while True:
            numeros_apuesta = None
            importe_quini = None
            dni = None
            imprimir_comprobante = None
            numeros_apostados = []  # Creamos una lista vacía para almacenar los números apostados
            contador = 0  # Variable para llevar el conteo de números ingresados

            while contador < 6:
                opcion = input("Desea ingresar los números manualmente (1). Desea generarlos al azar(2). Desea volver al menú principal (3): ")

                if opcion == "1":
                    while contador < 6:
                        numeros_apuesta = input("Ingrese un número entre 00 y 45: ")

                        # Verificamos si el input tiene dos cifras y está dentro del rango
                        if len(numeros_apuesta) != 2 or not (numeros_apuesta.isdigit() and 0 <= int(numeros_apuesta) <= 45):
                            print("La opción ingresada no es válida. Intente nuevamente.")
                            continue

                        # Convertimos el input en un número entero
                        numeros_apuesta = int(numeros_apuesta)

                        # Verificamos si el número ya fue ingresado previamente
                        if numeros_apuesta in numeros_apostados:
                            print("El número ya ha sido ingresado previamente. Intente nuevamente.")
                            continue

                        # Agregamos el número a la lista y aumentamos el contador
                        numeros_apostados.append(numeros_apuesta)
                        contador += 1

                    print("Los números ingresados son:", numeros_apostados)

                    while True:
                        try:
                            importe_quini = float(input("Ingrese el importe de la apuesta: $"))
                            break
                        except ValueError:
                            print("La opción ingresada no es válida. Intente nuevamente.")

                    while True:
                        try:
                            dni = int(input("Ingrese el número de DNI sin puntos: "))
                            if len(str(dni)) == 8:
                                break
                            else:
                                raise ValueError
                        except ValueError:
                            print("La opción ingresada no es válida. Intente nuevamente.")
                    escribir_apuesta_quini("apuestasAgosto.txt", dni, numeros_apostados, importe_quini, opcion_elegida, numero_comprobante)
                    numero_comprobante += 1
                    print("Apuesta guardada exitosamente", end="\n")
                    while imprimir_comprobante not in ("Y", "N"):
                        try:
                            imprimir_comprobante = input("Para imprimir el comprobante ingrese Y (si) o N (no): ").upper()
                            if imprimir_comprobante == "Y":
                                print("Imprimiendo el comprobante...", end="\n")
                                print(" -------------------------------------- ")
                                print("|**************************************|")
                                print("|* Apuestas de", nombrequiniela, "*|")
                                print("|Dirección:",direccion,"|")
                                print("|**************************************|")
                                print("|--------------------------------------|")
                                print("| Juego: Quini 6 - N° comprobante:",numero_comprobante,"  |")
                                print("|--------------------------------------|")
                                print("| N° apostados: ",numeros_apostados, "  |")
                                print("| DNI del cliente:",dni, "           |")
                                print("| Importe de la apuesta: $",importe_quini, "     |")
                                print("| ------------------------------------ |")
                                print("| Fecha:",fecha, "    Hora:",hora, "|")
                                print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ")
                            
                            elif imprimir_comprobante == "N":
                                print("No se imprimirá el comprobante.")
                            else:
                                raise ValueError
                        except ValueError:
                            print("La opción ingresada no es válida. Intente nuevamente.")
                        break  # Salimos del bucle cuando se completan los 6 números

                elif opcion == "2":
                    generar_numeros_azar()

                    while True:
                        try:
                            importe_quini = float(input("Ingrese el importe de la apuesta: $"))
                            break
                        except ValueError:
                            print("La opción ingresada no es válida. Intente nuevamente.")

                    while True:
                        try:
                            dni = int(input("Ingrese el número de DNI sin puntos: "))
                            if len(str(dni)) == 8:
                                break
                            else:
                                raise ValueError
                        except ValueError:
                            print("La opción ingresada no es válida. Intente nuevamente.")

                    escribir_apuesta_quini("apuestasAgosto.txt", dni, numeros_apostados, importe_quini, opcion_elegida, numero_comprobante)
                    numero_comprobante += 1
                    print("Apuesta guardada exitosamente", end="\n")
                    while imprimir_comprobante not in ("Y", "N"):
                        try:
                            imprimir_comprobante = input("Para imprimir el comprobante ingrese Y (si) o N (no): ").upper()
                            if imprimir_comprobante == "Y":
                                print("Imprimiendo el comprobante...", end="\n")
                                print(" -------------------------------------- ")
                                print("|**************************************|")
                                print("|* Apuestas de", nombrequiniela, "*|")
                                print("| Dirección:",direccion,"|")
                                print("|**************************************|")
                                print("|--------------------------------------|")
                                print("| Juego: Quini 6 - N° comprobante:",numero_comprobante,"  |")
                                print("|--------------------------------------|")
                                print("| Números apostados: ",numeros_apostados, "|")
                                print("| DNI del cliente:",dni, "           |")
                                print("| Importe de la apuesta: $",importe_quini, "     |")
                                print("| ------------------------------------ |")
                                print("| Fecha:",fecha, "    Hora:",hora, "|")
                                print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ")

                            elif imprimir_comprobante == "N":
                                print("No se imprimirá el comprobante.")
                            else:
                                raise ValueError
                        except ValueError:
                            print("La opción ingresada no es válida. Intente nuevamente.")
                elif opcion == "3":
                    break
                else:
                    print("La opción ingresada no es válida. Intente nuevamente.")
            break

    elif opcion_elegida=="3":
        print("Juego:", menu[opcion_elegida], fecha, hora)
        
        while True:
            opcion = input("Desea comprobar número ganador en Quiniela (1). Desea comprobar números ganadores en Quini 6 (2). Desea volver al menú principal (3): ")
            if opcion=="1":
                while True:
                    try:
                        numero_ganador = int(input("Ingrese el número ganador: "))
                        if numero_ganador<0 or len(str(numero_ganador))<2 or len(str(numero_ganador))>4:
                            raise ValueError
                        break
                    except ValueError:
                        print("La opción ingresada no es válida. Intente nuevamente.")
                        continue
                    
                while True:
                    try:
                        dni = int(input("Ingrese el número de DNI sin puntos: "))
                        if len(str(dni)) == 8:
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("La opción ingresada no es válida. Intente nuevamente.")
                    
                if leer_apuesta_quiniela("apuestasAgosto.txt", dni, numeros_apuesta):
                    print("El N° de la apuesta es el ganador. ¡Felicidades! ")
                else:
                    print("No hubo acierto.")

            elif opcion=="2":
                contador=0
                while True:
                    try:
                        numeros_apostados=[]
                        while contador < 6:
                            numeros_apuesta = input("Ingrese un número entre 00 y 45: ")
                            if len(numeros_apuesta) != 2 or not (numeros_apuesta.isdigit() and 0 <= int(numeros_apuesta) <= 45):
                                print("La opción ingresada no es válida. Intente nuevamente.")
                                continue
                            numeros_apuesta = int(numeros_apuesta)

                            # Verificamos si el número ya fue ingresado previamente
                            if numeros_apuesta in numeros_apostados:
                                print("El número ya ha sido ingresado previamente. Intente nuevamente.")
                                continue

                            # Agregamos el número a la lista y aumentamos el contador
                            numeros_apostados.append(numeros_apuesta)
                            contador += 1
                        print("Los números ganadores son:", numeros_apostados)
                    except ValueError:
                        print("La opción ingresada no es válida. Intente nuevamente.")
                        continue
                        
                    while True:
                        try:
                            dni = int(input("Ingrese el número de DNI sin puntos: "))
                            if len(str(dni)) == 8:
                                break
                            else:
                                raise ValueError
                        except ValueError:
                            print("La opción ingresada no es válida. Intente nuevamente.")
                            
                    if leer_apuesta_quini6("apuestasAgosto.txt", dni, numeros_apuesta):
                        print("Los N° de la apuesta son ganadores. ¡Felicidades!")
                        break
                    else:
                        print("No hubo aciertos")
                        break

            elif opcion=="3":
                break
            else:
                print("La opción ingresada no es válida. Intente nuevamente.")
    
    elif opcion_elegida=="4":
        while True:
            try:
                opcion_arqueo=input("Si desea imprimir el arqueo de caja, presione 1. Para salir presione 2: ")
                #Leer importes desde el archivo
                importe_quiniela, importe_quini = leer_importes("apuestasAgosto.txt")

                if opcion_arqueo=="1":
                    # Calcular los resultados
                    total_quiniela, total_quini, total_recaudacion, retencion, ganancia = arqueo_caja(importe_quiniela, importe_quini)
                    print("Imprimiendo el arqueo de caja...", end="\n")
                    print(" ______________________________________ ")
                    print("|**************************************|")
                    print("|* Apuestas de", nombrequiniela, "*|")
                    print("|Dirección:",direccion,"|")
                    print("|**************************************|")
                    print("|--------------------------------------|")
                    print("|---         Arqueo de caja         ---|")
                    print("|--------------------------------------|")
                    print("| Fecha:",fecha, "    Hora:",hora, "|")
                    print("| N° de arqueo:                     ",n_arqueo, "|")
                    print("| Recaudación                          |")
                    print("| *Quiniela:                           |")
                    print("| N° comprobante", "-", "Importe       |")
                    for i, importe in enumerate(importe_quiniela):
                        print(f"| {i} - ${importe:.2f} |")
                    print("|--------------------------------------|")
                    print("| Total recaudado en la quiniela: ", total_quiniela, "|")
                    print("|--------------------------------------|")
                    print("| *Quini 6:                            |")
                    print("| N° comprobante", "-", "Importe       |")
                    for i, importe in enumerate(importe_quini):
                        print(f"| {i} - ${importe:.2f} |")
                    print("|--------------------------------------|")
                    print("| Total recaudado en el quini 6: ", total_quini,"|")
                    print("|--------------------------------------|")
                    print("| Total recaudación mensual: $", total_recaudacion,"|")
                    print("| Retenciones del Estado (47%): $", retencion,"|")
                    print("| ------------------------------------ |")
                    print("| Total ganancia neta: $", ganancia," |")
                    print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ")
                    n_arqueo+=1

                elif opcion_arqueo=="2":
                    print("Volviendo al menú principal...")
                    break
                else:
                    print("La opción ingresada no es válida. Intente nuevamente.")
                
            except ValueError:
                print("La opción ingresada no es válida. Intente nuevamente.")
                break

    elif opcion_elegida=="5":
        
        while True:
            try:
                volver=input("Para cancelar presione 1. Para salir del sistema presione 2: ")
                if volver=="1":
                    print("Volviendo al menú principal.")
                    break
                elif volver=="2":
                    print("Saliendo del sistema....")
                    print("Gracias por utilizar nuestro servicio Pybel®")
                    continue
                else:
                    print("La opción ingresada no es válida. Intente nuevamente")
            except ValueError:
                break
        
