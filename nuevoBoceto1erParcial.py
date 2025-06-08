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


for i in range(3):
    
    id = i+1
    
    nombre = input("Ingrese el nombre de la persona: ").capitalize()
    apellido = input("Ingrese el apellido de la persona: ").upper()

    sexo = input("Ingrese el sexo de la persona:\nM para masculino\nF para femenino\nIngrese aquí: ").upper()
    while sexo != "M" and sexo != "F":
        print("ERROR: Ingrese un sexo válido")
        sexo = input("Ingrese el sexo de la persona:\nM para masculino\nF para femenino\nIngrese aquí: ").upper()
    
    codigoDeSector = input("Ingrese el código de sector de la persona (A/B/C): ").upper()
    while codigoDeSector!="A" and codigoDeSector!="B" and codigoDeSector!="C":
        print("ERROR: Ingrese un código de sector válido")
        codigoDeSector = input("Ingrese el código de sector de la persona (A/B/C): ").upper()
    
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

    aniosDeAntiguedad = int(input("Ingrese la antiguedad de la persona (entre 0 a 20 años): "))
    while aniosDeAntiguedad < 0 or  aniosDeAntiguedad > 20:
        print("ERROR: Ingrese una antiguedad válida")
        aniosDeAntiguedad = int(input("Ingrese la antiguedad de la persona (entre 0 a 20 años): "))

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

    edad = int(input("Ingrese la edad de la persona (entre 21 y 70 años): "))
    while edad < 21 or edad > 70:
        print("ERROR: Ingrese una edad válida")
        edad = int(input("Ingrese la edad de la persona (entre 21 y 70 años): "))
    
    # Acumular edades
    acumuladorEdades = acumuladorEdades + edad
    # Contar cantidad de edades
    cantidadDeEdades += 1

    zona = input("Ingrese la zona de la persona:\nN para Norte\nS para Sur\nO para Oeste\nE para Este\nIngrese aquí: ").upper()
    while zona != "N" and zona != "S" and zona != "O" and zona != "E":
        print("ERROR: Ingrese una zona válida")
        zona = input("Ingrese la zona de la persona:\nN para Norte\nS para Sur\nO para Oeste\nE para Este\nIngrese aquí: ").upper()

    if zona=="N" or zona=="E":
        modalidad = "VIRTUAL"
    elif zona=="S":
        modalidad = "PRESENCIAL"
    else: # zona=="O"
        modalidad = "BIMODAL"
        contadorBImodal += 1

    # Muestro los datos de la persona.
    print("\n-----------------DATOS DE LA PERSONA-----------------")
    print("ID:", id)
    print("Nombre:", nombre)
    print("Apellido:", apellido)
    print("Sexo:", sexo)
    print("Zona:", zona)
    print("Sector:", sector)
    print(f"Edad: {edad} años")
    print(f"Antiguedad: {aniosDeAntiguedad} años")
    print(f"Sueldo: {sueldo} pesos")
    print("Capacitación:", capacitacion)
    print("Modalidad:", modalidad)
    print("-------------------------------------------------------\n")
    input("\nPresione ENTER para continuar...")
    os.system("cls") # Limpiar pantalla   
# Fin del ciclo for.

print("\n\n\n----------------RESULTADOS---------------------")
print("\nCantidad de personas por capacitación:")
print("OFFICE:", contadorOFFICE)
print("COMUNICACION:", contadorCOMUNICACION)
print("CLIMA ORGANIZACIONAL:", contadorCLIMAorganizacional)
print("VENTAS ONLINE:", contadorVENTASonline)
print("\nCantidad de personas de la modalidad mixta:", contadorBImodal)
print("\n")
print(f"Acumulador de sueldos: {acumuladorSueldos} pesos")
print(f"Acumulador de sueldos por años de antigüedad: {acumuladorSueldosPorAnios} pesos")
print("\n")
print(f"Promedio de edades: {acumuladorEdades/cantidadDeEdades} años")
print(f"Promedio de sueldos: {acumuladorSueldos/cantidadDeEdades} pesos")
print("-----------------------------------------------------")
input("\nPresione ENTER para continuar...") 
print("\nFin del programa.")
    
