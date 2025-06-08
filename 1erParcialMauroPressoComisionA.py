import os
os.system("cls")

# Programa principal

# Inicializo los contadores por sector
contadorSectorA = 0
contadorSectorB = 0
contadorSectorC = 0

# Acumulo sueldos por sector
acumuladorSueldosSectorA = 0
acumuladorSueldosSectorB = 0
acumuladorSueldosSectorC = 0

# Acumulo plus por capacitación
acumuladorPlusCapacitacionTangoGestion = 0
acumuladorPlusCapacitacionJommla = 0
acumuladorPlusCapacitacionEstrategias = 0

# Inicializo los contadores de la capacitacion
contadorSIcapacitacion = 0
contadorNOcapacitacion = 0

# Inicializo las listas para guardar los datos de los empleados.
ListaDeNumeroDeInscripcion = []
ListaDeNumeroDeNombres = []
ListaDeNumeroDeApellidos = []
ListaDeSector = []
ListaDeCapacitacion = []
ListaDeAntiguedades = []
ListaDeLocalidades = []
ListaDeSueldos = []
ListaDePlus = []

cantidadDeEmpleados = int(input("Ingrese la cantidad de empleados: "))
while cantidadDeEmpleados <= 0:
    print("Dato erroneo. Ingrese nuevamente")
    cantidadDeEmpleados = int(input("Ingrese la cantidad de empleados: "))


for i in range(cantidadDeEmpleados):
    
    numeroDeInscripicion = i + 100 # i arranca en cero.

    apellido = input("\n\nIngrese su apellido: ").upper()
    nombre = input("Ingrese su nombre: ").capitalize()
    
    # Ingreso y valido antiguedad
    antiguedad = int(input("\nIngrese su antiguedad (entre 0 a 25 años): "))
    while antiguedad < 0 or antiguedad > 25:
        print("Antiguedad incorrecta. Intente de nuevo.")
        antiguedad = int(input("\nIngrese su antiguedad (entre 0 a 25 años): "))
    # Valide antiguedad

    # Ingreso y valido código de sector
    codigoDeSector = input("\nIngrese su código de sector (A/B/C): ").upper()
    while codigoDeSector != "A" and codigoDeSector != "B" and codigoDeSector != "C":
        print("Código de sector incorrecto. Intente de nuevo.")
        codigoDeSector = input("\nIngrese su código de sector (A/B/C): ").upper()
    # Valide código de sector

    # ¿Hace la capacitación?
    haceCapacitacion = input("\nIngrese si hace la capacitación (S/N): ").upper()
    while haceCapacitacion != "S" and haceCapacitacion != "N":
        print("Respuesta incorrecta. Intente de nuevo.")
        haceCapacitacion = input("\nIngrese si hace la capacitación (S/N): ").upper()
    # Valide capacitación

    # Ingreso y valido código de localidad
    codigoDeLocalidad = input("\nIngrese su código de localidad (C/N/P): ").upper()
    while codigoDeLocalidad != "C" and codigoDeLocalidad != "N" and codigoDeLocalidad != "P":
        print("Código de localidad incorrecto. Intente de nuevo.")
        codigoDeLocalidad = input("\nIngrese su código de localidad (C/N/P): ").upper()
    # Valide código de localidad

    if codigoDeSector == "A":
        sueldo = 1224500
        sector = "ADMINISTRACION"
        capacitacion = "TANGO GESTION"
        contadorSectorA = contadorSectorA + 1
    elif codigoDeSector == "B":
        sueldo = 1225200
        sector = "DESARROLLO"
        capacitacion = "JOMMLA"
        contadorSectorB = contadorSectorB + 1
    else: # codigoDeSector == "C"
        sueldo = 1228800
        sector = "LOGISTICA"
        capacitacion = "ESTRATEGIAS"
        contadorSectorC = contadorSectorC + 1

    # Calcular el Plus en el sueldo por hacer capacitación
    if haceCapacitacion == "S":
        plus = sueldo*(0.10)
        contadorSIcapacitacion = contadorSIcapacitacion + 1
        if capacitacion == "TANGO GESTION":
            acumuladorPlusCapacitacionTangoGestion = acumuladorPlusCapacitacionTangoGestion + plus
        elif capacitacion == "JOMMLA":
            acumuladorPlusCapacitacionJommla = acumuladorPlusCapacitacionJommla + plus
        else: # capacitacion == "ESTRATEGIAS"
            acumuladorPlusCapacitacionEstrategias = acumuladorPlusCapacitacionEstrategias + plus

    else: # haceCapacitacion == "N"
        plus = 0
        contadorNOcapacitacion = contadorNOcapacitacion + 1
  
    # Sumo los sueldos totales por sector
    if codigoDeSector == "A":
        acumuladorSueldosSectorA = acumuladorSueldosSectorA + sueldo
    elif codigoDeSector == "B":
        acumuladorSueldosSectorB = acumuladorSueldosSectorB + sueldo
    else: # codigoDeSector == "C"
        acumuladorSueldosSectorC = acumuladorSueldosSectorC + sueldo

    # Asigno localidad
    if codigoDeLocalidad == "C":
        localidad = "Cipolletti"
    elif codigoDeLocalidad == "N":
        localidad = "Neuquen"
    else: # codigoDeLocalidad == "P"
        localidad = "Plottier"

    # Guardo en listas los datos de la persona
    ListaDeNumeroDeInscripcion.append(numeroDeInscripicion)
    ListaDeNumeroDeNombres.append(nombre)
    ListaDeNumeroDeApellidos.append(apellido)
    ListaDeSector.append(sector)
    if haceCapacitacion == "S":
        ListaDeCapacitacion.append(capacitacion)
    else: # haceCapacitacion == "N"
        ListaDeCapacitacion.append("NO HIZO CAPACITACION")
    ListaDeAntiguedades.append(antiguedad)
    ListaDeLocalidades.append(localidad)
    ListaDeSueldos.append(sueldo)
    ListaDePlus.append(plus)
# Fin ciclo for

# Como terminó el ciclo for, los resultados están listos para ser guardados en un archivo.
pathArchivoDeDatos = "D:/Facultad/IFES/Materias/1erCuatri1erAnio/IntroAlPensamientoLogico/Practica2doParcial/DatosDelProgramaDel1erParcial.txt"
archivoDeDatos = open(pathArchivoDeDatos, "w") # El archivo de RESULTADOS se abrió en modo (sobre)escritura.
archivoDeDatos.write("DATOS DE LOS EMPLEADOS:\n")
archivoDeDatos.write("-"*20)
for i in range(cantidadDeEmpleados):
    archivoDeDatos = open(pathArchivoDeDatos, "a") # El archivo de DATOS se abrió para agregar al final.
    archivoDeDatos.write("\nEMPLEADO\t" + str(i+1) + ":\n")
    archivoDeDatos.write("*\tNumero de inscripcion:\t" + str(ListaDeNumeroDeInscripcion[i]) + "\n")
    archivoDeDatos.write("*\tNombre:\t" + ListaDeNumeroDeNombres[i] + "\n")
    archivoDeDatos.write("*\tApellido:\t" + ListaDeNumeroDeApellidos[i] + "\n")
    archivoDeDatos.write("*\tSector:\t" + ListaDeSector[i] + "\n")
    archivoDeDatos.write("*\tCapacitacion:\t" + ListaDeCapacitacion[i] + "\n")
    archivoDeDatos.write("*\tAntiguedad:\t" + str(ListaDeAntiguedades[i]) + "\tanos\n")
    archivoDeDatos.write("*\tLocalidad:\t" + ListaDeLocalidades[i] + "\n")
    archivoDeDatos.write("*\tSueldo:\t" + str(ListaDeSueldos[i]) + "\tpesos\n")
    archivoDeDatos.write("*\tPlus:\t" + str(ListaDePlus[i]) + "\tpesos\n") 
    archivoDeDatos.write("-"*20)
    archivoDeDatos.close() # El archivo de DATOS se cerró de la apertura del mismo modo.

archivoDeDatos = open(pathArchivoDeDatos, "r") # El archivo de RESULTADOS se abrió en modo lectura.
datos = archivoDeDatos.read()
archivoDeDatos.close() # El archivo de RESULTADOS se cerró de la apertura del mismo modo lectura.
print(datos)
input("\nPresione ENTER para continuar...")
os.system("cls")

# Como terminó el ciclo for, los resultados están listos para ser guardados en un archivo.
pathArchivoDeResultados = "D:/Facultad/IFES/Materias/1erCuatri1erAnio/IntroAlPensamientoLogico/Practica2doParcial/ResultadosDelProgramaDel1erParcial.txt"
archivoDeResultados = open(pathArchivoDeResultados, "w") # El archivo de RESULTADOS se abrió en modo (sobre)escritura.
archivoDeResultados.write("REPORTE FINAL:\n")
archivoDeResultados.write("-"*20)
# Ejercicio 4 Inciso l)
archivoDeResultados.write("\n*\tAcumulacion del Plus capacitacion TANGO GESTION:\t" + str(acumuladorPlusCapacitacionTangoGestion) + "\tpesos\n")
archivoDeResultados.write("*\tAcumulacion del Plus capacitacion JOMMLA:\t" + str(acumuladorPlusCapacitacionJommla) + "\tpesos\n")
archivoDeResultados.write("*\tAcumulacion del Plus capacitacion ESTRATEGIAS:\t" + str(acumuladorPlusCapacitacionEstrategias) + "\tpesos\n")
archivoDeResultados.write("-"*20)
archivoDeResultados.write("\n*\tCantidad de trabajadores que hicieron capacitacion:\t" + str(contadorSIcapacitacion) + "\n") # Ejercicio 4 inciso m.
archivoDeResultados.write("*\tCantidad de trabajadores que no hicieron capacitacion:\t" + str(contadorNOcapacitacion) + "\n") # Ejercicio 4 inciso n.
archivoDeResultados.write("-"*20)
# Ejercicio 4 inciso j.
archivoDeResultados.write("\n*\tCantidad de trabajadores en sector A:\t" + str(contadorSectorA) + "\n")
archivoDeResultados.write("*\tCantidad de trabajadores en sector B:\t" + str(contadorSectorB) + "\n")
archivoDeResultados.write("*\tCantidad de trabajadores en sector C:\t" + str(contadorSectorC) + "\n")
archivoDeResultados.write("-"*20)
# Ejercicio 4 inciso k.
archivoDeResultados.write("\nPromedio de sueldos por sector:\n")
if contadorSectorA > 0:
    archivoDeResultados.write("*\tPromedio de sueldo del sector A:\t" + str(acumuladorSueldosSectorA/contadorSectorA) + "\tpesos\n")
else:
    archivoDeResultados.write("*\tNo hay trabajadores en el sector A." + "\n")
if contadorSectorB > 0:
    archivoDeResultados.write("*\tPromedio de sueldo del sector B:\t" + str(acumuladorSueldosSectorB/contadorSectorB) + "\tpesos\n")
else:
    archivoDeResultados.write("*\tNo hay trabajadores en el sector B.")
if contadorSectorC > 0:
    archivoDeResultados.write("*\tPromedio de sueldo del sector C:\t" + str(acumuladorSueldosSectorC/contadorSectorC) + "\tpesos\n")
else:
    archivoDeResultados.write("*\tNo hay trabajadores en el sector C.")
archivoDeResultados.write("-"*20)
archivoDeResultados.close() # El archivo de RESULTADOS se cerró de la apertura del mismo modo (sobre)escritura.

archivoDeResultados = open(pathArchivoDeResultados, "r") # El archivo de RESULTADOS se abrió en modo lectura.
resultados = archivoDeResultados.read()
archivoDeResultados.close() # El archivo de RESULTADOS se cerró de la apertura del mismo modo lectura.
print(resultados)
input("\nPresione ENTER para continuar...")
os.system("cls")
print("\nFin del programa =D")

