import os
os.system("cls") # Limpiar pantalla

# PROGRAMA PRINCIPAL:

# 3a) Acumular sueldos
acumuladorSueldos = 0

# 3b) Promediar edades
acumuladorEdades = 0
cantidadDeEdades = 0

# 3c) Contar cantidad de personas por capacitacion.
contadorOFFICE = 0
contadorCOMUNICACION = 0
contadorCLIMAorganizacional = 0
contadorVENTASonline = 0

# 3d) Contar cantidad de personas de la modalidad mixta.
contadorBImodal = 0

# 3e) Inventar dos situaciones en donde se apliquen contadores - acumuladores
# i) Promediar los sueldos de las personas.
# ii) Acumular el sueldo por anios de antiguedad.
acumuladorSueldosPorAnios = 0

# Inicializando las listas donde se guardaran los datos de cada docente.
ListaIDs = []
ListaDeNombres = []
ListaDeApellidos = []
ListaDeEdades = []
ListaDeAntiguedades = []
ListaDeZonas = []
ListaDeSexos = []
ListaDeSectores = []
ListaDeCapacitacion = []
ListaDeModalidad = []
ListaDeSueldos = []

cantidadDeEmpleados = int(input("Ingrese la cantidad de empleados: "))
while cantidadDeEmpleados <= 0:
    print("Dato erroneo. Ingrese nuevamente.")
    cantidadDeEmpleados = int(input("\nIngrese la cantidad de empleados: "))
print("\nIngrese los datos de los empleados:")
for i in range(cantidadDeEmpleados):
    
    id = i+1
    print(f"\n{i+1}:\n")
    nombre = input("Ingrese el nombre del empleado: ").capitalize()
    apellido = input("Ingrese el apellido del empleado: ").upper()

    sexo = input("Ingrese el sexo del empleado:\nM para masculino\nF para femenino\nIngrese aquí: ").upper()
    while sexo != "M" and sexo != "F":
        print("ERROR: Ingrese un sexo válido")
        sexo = input("Ingrese el sexo del empleado:\nM para masculino\nF para femenino\nIngrese aquí: ").upper()
    
    codigoDeSector = input("Ingrese el código de sector del empleado (A/B/C): ").upper()
    while codigoDeSector!="A" and codigoDeSector!="B" and codigoDeSector!="C":
        print("ERROR: Ingrese un código de sector válido")
        codigoDeSector = input("Ingrese el código de sector del empleado (A/B/C): ").upper()
    
    if codigoDeSector=="A":
        sector = "FINANZAS"
        sueldo = 1780632
    elif codigoDeSector=="B":
        sector = "MARKETING"
        sueldo = 1890562
    else: # codigoDeSector=="C":
        sector = "IT"
        sueldo = 1952630

    # Acumular sueldos
    acumuladorSueldos = acumuladorSueldos + sueldo

    aniosDeAntiguedad = int(input("Ingrese la antiguedad del empleado (entre 0 a 20 años): "))
    while aniosDeAntiguedad < 0 or aniosDeAntiguedad > 20:
        print("ERROR: Ingrese una antiguedad válida")
        aniosDeAntiguedad = int(input("Ingrese la antiguedad del empleado (entre 0 a 20 años): "))

    # Acumular sueldo por años de antiguedad
    acumuladorSueldosPorAnios = acumuladorSueldosPorAnios + sueldo * aniosDeAntiguedad

    if codigoDeSector=="A" and aniosDeAntiguedad<10: 
        capacitacion = "OFFICE"
        contadorOFFICE += 1
    elif codigoDeSector=="B" and aniosDeAntiguedad>10:
        capacitacion = "COMUNICACION"
        contadorCOMUNICACION += 1
    elif codigoDeSector=="C" and aniosDeAntiguedad>10:
        capacitacion = "VENTAS ONLINE"
        contadorVENTASonline += 1
    else:
        capacitacion = "CLIMA ORGANIZACIONAL"
        contadorCLIMAorganizacional += 1

    edad = int(input("Ingrese la edad del empleado (entre 21 y 70 años): "))
    while edad < 21 or edad > 70:
        print("ERROR: Ingrese una edad válida")
        edad = int(input("Ingrese la edad del empleado (entre 21 y 70 años): "))
    
    # Acumular edades
    acumuladorEdades = acumuladorEdades + edad
    # Contar cantidad de edades
    cantidadDeEdades += 1

    zona = input("Ingrese la zona del empleado:\nN para Norte\nS para Sur\nO para Oeste\nE para Este\nIngrese aquí: ").upper()
    while zona != "N" and zona != "S" and zona != "O" and zona != "E":
        print("ERROR: Ingrese una zona válida")
        zona = input("Ingrese la zona del empleado:\nN para Norte\nS para Sur\nO para Oeste\nE para Este\nIngrese aquí: ").upper()

    if zona=="N" or zona=="E":
        modalidad = "VIRTUAL"
    elif zona=="S":
        modalidad = "PRESENCIAL"
    else: # zona=="O"
        modalidad = "BIMODAL"
        contadorBImodal += 1

    # Guardo los datos del empleado en listas.
    ListaIDs.append(id)
    ListaDeNombres.append(nombre)
    ListaDeApellidos.append(apellido)
    ListaDeSexos.append(sexo)
    ListaDeZonas.append(zona)
    ListaDeSectores.append(sector)
    ListaDeEdades.append(edad)
    ListaDeAntiguedades.append(aniosDeAntiguedad)
    ListaDeSueldos.append(sueldo)
    ListaDeCapacitacion.append(capacitacion)
    ListaDeModalidad.append(modalidad)
# Fin del ciclo for.
os.system("cls") # Limpiar pantalla
# Como terminó el ciclo for, los resultados están listos para ser guardados en un archivo.
pathArchivoDeDatos = "D:/Facultad/IFES/Materias/1erCuatri1erAnio/IntroAlPensamientoLogico/Practica2doParcial/DatosDelProgramaNuevoBoceto1erParcial.txt"
archivoDeDatos = open(pathArchivoDeDatos, "w") # El archivo de DATOS se abrió en modo (sobre)escritura.
archivoDeDatos.write("DATOS DE LOS EMPLEADOS:\n")
archivoDeDatos.write("-"*20)
archivoDeDatos.close()
for i in range(cantidadDeEmpleados):
    archivoDeDatos = open(pathArchivoDeDatos, "a")
    archivoDeDatos.write("\nEMPLEADO\t" + str(i+1) + ":\n\n")
    archivoDeDatos.write("*\tID:\t" + str(ListaIDs[i]) + "\n")
    archivoDeDatos.write("*\tNombre completo:\t" + ListaDeNombres[i] + "\t" + ListaDeApellidos[i] + "\n")
    archivoDeDatos.write("*\tSexo:\t" + ListaDeSexos[i] + "\n")
    archivoDeDatos.write("*\tZona:\t" + ListaDeZonas[i] + "\n")
    archivoDeDatos.write("*\tSector:\t" + ListaDeSectores[i] + "\n")
    archivoDeDatos.write("*\tEdad:\t" + str(ListaDeEdades[i]) + "\tanos\n")
    archivoDeDatos.write("*\tAntiguedad:\t" + str(ListaDeAntiguedades[i]) + "\tanos\n")
    archivoDeDatos.write("*\tSueldo:\t" + str(ListaDeSueldos[i]) + "\tpesos\n")
    archivoDeDatos.write("*\tCapacitacion:\t" + ListaDeCapacitacion[i] + "\n")
    archivoDeDatos.write("*\tModalidad:\t" + ListaDeModalidad[i] + "\n")
    archivoDeDatos.write("-"*20)
    archivoDeDatos.close()

archivoDeDatos = open(pathArchivoDeDatos, "r") # El archivo de DATOS se abrió en modo lectura.
datos = archivoDeDatos.read()
archivoDeDatos.close() # El archivo de DATOS se cerró de la apertura del mismo modo lectura.
print(datos)
input("\nPresione ENTER para continuar...")
os.system("cls")


# Como terminó el ciclo for, los resultados están listos para ser guardados en un archivo.
pathArchivoDeResultados = "D:/Facultad/IFES/Materias/1erCuatri1erAnio/IntroAlPensamientoLogico/Practica2doParcial/ResultadosDelProgramaNuevoBoceto1erParcial.txt"
archivoDeResultados = open(pathArchivoDeResultados, "w") # El archivo de RESULTADOS se abrió en modo (sobre)escritura.
archivoDeResultados.write("REPORTE FINAL:\n")
archivoDeResultados.write("-"*20)
archivoDeResultados.write("\nCantidad de personas por capacitacion:\n\n")
archivoDeResultados.write("*\tOFFICE:\t" + str(contadorOFFICE) + "\n")
archivoDeResultados.write("*\tCOMUNICACION:\t" + str(contadorCOMUNICACION) + "\n")
archivoDeResultados.write("*\tCLIMA ORGANIZACIONAL:\t" + str(contadorCLIMAorganizacional) + "\n")
archivoDeResultados.write("*\tVENTAS ONLINE:\t" + str(contadorVENTASonline) + "\n")
archivoDeResultados.write("-"*20)
archivoDeResultados.write("\n*\tCantidad de personas de la modalidad mixta:\t" + str(contadorBImodal) + "\n")
archivoDeResultados.write("-"*20)
archivoDeResultados.write("\n*\tAcumulador de sueldos:\t" + str(acumuladorSueldos) + "\tpesos\n")
archivoDeResultados.write("\n*\tAcumulador de sueldos por anos de antiguedad:\t" + str(acumuladorSueldosPorAnios) + "\tpesos\n")
archivoDeResultados.write("-"*20)
archivoDeResultados.write("\n*\tPromedio de edades:\t" + str(acumuladorEdades/cantidadDeEdades) + "\tanos\n")
archivoDeResultados.write("\n*\tPromedio de sueldos:\t" + str(acumuladorSueldos/cantidadDeEdades) + "\tpesos\n")
archivoDeResultados.write("-"*20)
archivoDeResultados.close()

archivoDeResultados = open(pathArchivoDeResultados, "r") # El archivo de RESULTADOS se abrió en modo lectura.
resultados = archivoDeResultados.read()
archivoDeResultados.close() # El archivo de RESULTADOS se cerró de la apertura del mismo modo lectura.
print(resultados)
input("\nIngrese ENTER para continuar...")
os.system("cls")
print("\nFin del programa =D")
