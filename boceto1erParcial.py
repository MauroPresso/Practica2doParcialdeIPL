import os
os.system("cls")

# programa principal

# Inicializo en CERO los contadores por localidad
contadorCipolletti = 0
contadorNQN = 0
contadorRoca = 0
contadorPlottier = 0

# Inicializo en CERO los contadores por modalidad
contadorModalidadMixta = 0
contadorModalidadVirtual = 0
contadorModalidadPresencial = 0

# Inicializo en CERO los contadores por área de formación
contadorAreaAdministrativa = 0
contadorAreaNaturales = 0
contadorAreaTecnologicas = 0

# Inicializo en CERO los contadores por seminario
contadorSeminarioIAenNaturales = 0
contadorSeminarioLiderazgo = 0
contadorSeminarioRRHH = 0
contadorSeminarioNuevasTECSoftware = 0
contadorSeminarioInfoEnLaNube = 0

# Inicializo en CERO los contadores por modo de pago
contadorEfectivo = 0
contadorTarjeta = 0

# Inicializo en CERO los acumuladores
acumuladorDeImportesTotales = 0
acumuladorDeImportesApagarEfectivo = 0
acumuladorDeImportesApagarTarjeta = 0

# Inicializando las listas donde se guardaran los datos de cada docente.
ListaIDs = []
ListaDeNombres = []
ListaDeApellidos = []
ListaDeEdades = []
ListaDeAreas = []
ListaDeLocalidades = []
ListaDeSeminarios = []
ListaDeModalidades = []
ListaDeLugaresDeCursado = []
ListaDeImportePorEncuentro = []
ListaDeCantidadDeEncuentros = []
ListaDeImporteTotal = []
ListaDeModoDePago = []
ListaDeImporteAPagar = []

cantidadDeDocentes = int(input("Ingrese la cantidad de docentes: "))
while cantidadDeDocentes <= 0:
    print("Dato erroneo. Ingrese nuevamente.")
    cantidadDeDocentes = int(input("Ingrese la cantidad de docentes: "))
# Inicio ciclo for.
for i in range(cantidadDeDocentes):
    id = i + 1
    print(f"\nIngrese los datos del docente {i+1}:\n")
    nombre = input("Ingrese el nombre de la persona: ").capitalize()
    apellido = input("\nIngrese el apellido de la persona: ").upper()

    # Ingreso de la edad de la persona y su respectiva validación.
    edad = int(input("\nIngrese la edad de la persona (La edad debe estar entre 30 y 60 años): "))
    while edad < 30 or edad > 60:
        print("Dato erroneo, intente nuevamente")
        edad = int(input("\nIngrese la edad de la persona (La edad debe estar entre 30 y 60 años): "))
    
    # Ingreso del codigo de area de formacion y su respectiva validación.
    codigodeAreaDeFormacion = input("\nIngrese el area de formacion de la persona (ADM – NAT – TEC ): ").upper()
    while codigodeAreaDeFormacion != "ADM" and codigodeAreaDeFormacion != "NAT" and  codigodeAreaDeFormacion != "TEC":
        print("Dato erroneo, intente nuevamente")
        codigodeAreaDeFormacion = input("\nIngrese el area de formacion de la persona (ADM – NAT – TEC ): ").upper()
    # Area de formacion ya validada, ahora se asigna el area de formacion correspondiente.
    if codigodeAreaDeFormacion == "ADM":
        areaDeFormacion = "ADMINISTRATIVAS"
        contadorAreaAdministrativa += 1
    elif codigodeAreaDeFormacion == "NAT":
        areaDeFormacion = "NATURALES Y RENOVABLES"
        contadorAreaNaturales += 1
    else: # codigodeAreaDeFormacion == "TEC":
        areaDeFormacion = "TECNOLOGICAS"
        contadorAreaTecnologicas += 1

    # Ingreso del codigo de localidad y su respectiva validación.
    codigoDeLocalidad = input("\nIngrese el codigo de localidad de la persona\nC: Cipolletti\nN: Neuquén Capital\nR: General Roca\nP: Plottier\nIngrese aquí: ").upper()
    while codigoDeLocalidad != "C" and codigoDeLocalidad != "N" and codigoDeLocalidad != "R" and codigoDeLocalidad != "P":
        print("Dato erroneo, intente nuevamente")
        codigoDeLocalidad = input("\nIngrese el codigo de localidad de la persona\nC: Cipolletti\nN: Neuquén Capital\nR: General Roca\nP: Plottier\nIngrese aquí: ").upper()
    # Codigo de localidad ya validado, ahora se asigna el localidad correspondiente.
    if codigoDeLocalidad == "C":
        localidad = "Cipolletti"
        contadorCipolletti += 1
    elif codigoDeLocalidad == "N":
        localidad = "Neuquen Capital"
        contadorNQN += 1
    elif codigoDeLocalidad == "R":
        localidad = "General Roca"
        contadorRoca += 1
    else: # codigoDeLocalidad == "P":
        localidad = "Plottier"
        contadorPlottier += 1

    # Ingreso del codigo de seminario y su respectiva validación.
    codigoDeSeminario = input("\nIngrese el codigo de seminario de la persona\nA: IA EN LAS ÁREAS NATURALES\nB: LIDERAZGO SIGLO XXI\nC: ADMINISTRACIÓN DE RRHH\nD: NUEVAS TECNOLOGÍAS DE SOFTWARE\nE: INFORMÁTICA EN LA NUBE\nIngrese aquí: ").upper()
    while codigoDeSeminario != "A" and codigoDeSeminario != "B" and codigoDeSeminario != "C" and codigoDeSeminario != "D" and codigoDeSeminario != "E":
        print("Dato erroneo, intente nuevamente")
        codigoDeSeminario = input("\nIngrese el codigo de seminario de la persona\nA: IA EN LAS ÁREAS NATURALES\nB: LIDERAZGO SIGLO XXI\nC: ADMINISTRACIÓN DE RRHH\nD: NUEVAS TECNOLOGÍAS DE SOFTWARE\nE: INFORMÁTICA EN LA NUBE\nIngrese aquí: ").upper()
    # Codigo de seminario ya validado, ahora se asigna el seminario correspondiente.
    if codigoDeSeminario == "A":
        seminario = "IA EN LAS AREAS NATURALES"
        importePorEncuentro = 12500
        contadorSeminarioIAenNaturales += 1
    elif codigoDeSeminario == "B":
        seminario = "LIDERAZGO SIGLO XXI"
        importePorEncuentro = 8900
        contadorSeminarioLiderazgo += 1
    elif codigoDeSeminario == "C":
        seminario = "ADMINISTRACION DE RRHH"
        importePorEncuentro = 10500
        contadorSeminarioRRHH += 1
    elif codigoDeSeminario == "D":
        seminario = "NUEVAS TECNOLOGIAS DE SOFTWARE"
        importePorEncuentro = 11000
        contadorSeminarioNuevasTECSoftware += 1
    else: # codigoDeSeminario == "E"
        seminario = "INFORMATICA EN LA NUBE"
        importePorEncuentro = 14900
        contadorSeminarioInfoEnLaNube += 1

    # Ingreso del tipo de modalidad y su respectiva validación.
    tipoDeModalidad = input("\nIngrese el tipo de modalidad de la persona\nM: Mixta\nV: Virtual\nP: Presencial\nIngrese aquí: ").upper()
    while tipoDeModalidad != "M" and tipoDeModalidad != "V" and tipoDeModalidad != "P":
        print("Dato erroneo, intente nuevamente") 
        tipoDeModalidad = input("\nIngrese el tipo de modalidad de la persona\nM: Mixta\nV: Virtual\nP: Presencial\nIngrese aquí: ").upper()
    # Tipo de modalidad ya validado, ahora se asigna la modalidad correspondiente.
    if tipoDeModalidad == "M":
        modalidad = "MIXTA"
        lugarDeCursado = "Aula Magna y Zoom"
        contadorModalidadMixta += 1
    elif tipoDeModalidad == "V":
        modalidad = "VIRTUAL"
        lugarDeCursado = "Zoom"
        contadorModalidadVirtual += 1
    else: # tipoDeModalidad == "P":
        modalidad = "PRESENCIAL"
        lugarDeCursado = "Aula Magna"
        contadorModalidadPresencial += 1

    # Ingreso de la cantidad de encuentros y su respectiva validación.
    cantidadDeEncuentros = int(input("\nIngrese la cantidad de encuentros de la persona (de 1 a 5): "))
    while cantidadDeEncuentros < 1 or cantidadDeEncuentros > 5:
        print("Dato erroneo, intente nuevamente")
        cantidadDeEncuentros = int(input("\nIngrese la cantidad de encuentros de la persona (de 1 a 5): "))
    
    # Calculo el importe total de la persona.
    importeTotal = cantidadDeEncuentros * importePorEncuentro
    acumuladorDeImportesTotales = acumuladorDeImportesTotales + importeTotal
    
    # Ingreso del tipo de pago y su respectiva validación.
    tipoDePago = input("\nIngrese el tipo de pago de la persona\nE: Efectivo\nT: Tarjeta\nIngrese aquí: ").upper()
    while tipoDePago != "E" and tipoDePago != "T":
        print("Dato erroneo, intente nuevamente")
        tipoDePago = input("\nIngrese el tipo de pago de la persona\nE: Efectivo\nT: Tarjeta\nIngrese aquí: ").upper()
    # Tipo de pago ya validado, ahora se asigna el pago correspondiente.
    if tipoDePago == "E":
        modalidadDePago = "Efectivo"
        importeApagar = importeTotal*(1 - 0.05) # 5% de descuento
        acumuladorDeImportesApagarEfectivo = acumuladorDeImportesApagarEfectivo + importeApagar
        contadorEfectivo += 1
    else: # tipoDePago == "T":
        modalidadDePago = "Tarjeta"
        importeApagar = importeTotal*(1 + 0.10) # 10% de recargo
        acumuladorDeImportesApagarTarjeta = acumuladorDeImportesApagarTarjeta + importeApagar
        contadorTarjeta += 1

    # Guardo los datos de la persona en listas.
    ListaIDs.append(id)
    ListaDeNombres.append(nombre)
    ListaDeApellidos.append(apellido)
    ListaDeEdades.append(edad)
    ListaDeAreas.append(areaDeFormacion)
    ListaDeLocalidades.append(localidad)
    ListaDeSeminarios.append(seminario)
    ListaDeModalidades.append(modalidad)
    ListaDeLugaresDeCursado.append(lugarDeCursado)
    ListaDeImportePorEncuentro.append(importePorEncuentro)
    ListaDeCantidadDeEncuentros.append(cantidadDeEncuentros)
    ListaDeImporteTotal.append(importeTotal)
    ListaDeModoDePago.append(modalidadDePago)
    ListaDeImporteAPagar.append(importeApagar)
# Fin del ciclo for.

# Como terminó el ciclo for, los resultados están listos para ser guardados en un archivo.
pathArchivoDeDatos = "D:/Facultad/IFES/Materias/1erCuatri1erAnio/IntroAlPensamientoLogico/Practica2doParcial/DatosDelProgramaBoceto1erParcial.txt"
archivoDeDatos = open(pathArchivoDeDatos, "w") # El archivo de RESULTADOS se abrió en modo (sobre)escritura.
archivoDeDatos.write("DATOS DE LOS DOCENTES:\n")
archivoDeDatos.write("-"*20)
archivoDeDatos.close() # El archivo de DATOS se cerró de la apertura del mismo modo (sobre)escritura.
for i in range(cantidadDeDocentes):
    archivoDeDatos = open(pathArchivoDeDatos, "a") # El archivo de DATOS se abrió para agregar al final.
    archivoDeDatos.write("\nDOCENTE\t" + str(i+1) + ":\n")
    archivoDeDatos.write("*\tID:\t" + str(ListaIDs[i]) + "\n")
    archivoDeDatos.write( "*\tNombre completo:\t" + ListaDeNombres[i] + "\t" + ListaDeApellidos[i] + "\n")
    archivoDeDatos.write("*\tEdad:\t" + str(ListaDeEdades[i]) + "\n")
    archivoDeDatos.write("*\tArea de formacion:\t" + ListaDeAreas[i] + "\n")
    archivoDeDatos.write("*\tLocalidad:\t" + ListaDeLocalidades[i] + "\n")
    archivoDeDatos.write("*\tSeminario:\t" + ListaDeSeminarios[i] + "\n") 
    archivoDeDatos.write("*\tModalidad:\t" + ListaDeModalidades[i] + "\n")
    archivoDeDatos.write("*\tLugar de cursado:\t" + ListaDeLugaresDeCursado[i] + "\n")
    archivoDeDatos.write("*\tImporte por encuentro:\t" + str(ListaDeImportePorEncuentro[i]) + "\tpesos\n")
    archivoDeDatos.write("*\tCantidad de encuentros:\t" + str(ListaDeCantidadDeEncuentros[i]) + "\n")
    archivoDeDatos.write("*\tImporte total:\t" + str(ListaDeImporteTotal[i]) + "\n")
    archivoDeDatos.write("*\tModo de pago:\t" + ListaDeModoDePago[i] + "\n")
    archivoDeDatos.write("*\tImporte a pagar:\t" + str(ListaDeImporteAPagar[i]) + "\n")
    archivoDeDatos.close() # El archivo de DATOS se cerró de la apertura del mismo modo.

archivoDeDatos = open(pathArchivoDeDatos, "r") # El archivo de RESULTADOS se abrió en modo lectura.
datos = archivoDeDatos.read()
archivoDeDatos.close() # El archivo de RESULTADOS se cerró de la apertura del mismo modo lectura.
print(datos)
input("\nPresione ENTER para continuar...")
os.system("cls")

# Como terminó el ciclo for, los resultados están listos para ser guardados en un archivo.
pathArchivoDeResultados = "D:/Facultad/IFES/Materias/1erCuatri1erAnio/IntroAlPensamientoLogico/Practica2doParcial/ResultadosDelProgramaBoceto1erParcial.txt"
archivoDeResultados = open(pathArchivoDeResultados, "w") # El archivo de RESULTADOS se abrió en modo (sobre)escritura.
archivoDeResultados.write("REPORTE FINAL:\n")
archivoDeResultados.write("-"*20)
archivoDeResultados.write("\nParticipantes por area de formación:" + "\n\n")
archivoDeResultados.write("*\tCantidad de personas que cursaron de administrativa:\t" + str(contadorAreaAdministrativa) + "\n")
archivoDeResultados.write("*\tCantidad de personas que cursaron de Naturales:\t" + str(contadorAreaNaturales) + "\n")
archivoDeResultados.write("*\tCantidad de personas que cursaron de Tecnologicas:\t" + str(contadorAreaTecnologicas) + "\n")
archivoDeResultados.write("-"*20)
archivoDeResultados.write("\nParticipantes por modalidad:" + "\n\n")
archivoDeResultados.write("*\tCantidad de personas que cursaron de Mixta:\t" + str(contadorModalidadMixta) + "\n")
archivoDeResultados.write("*\tCantidad de personas que cursaron de Virtual:\t" + str(contadorModalidadVirtual) + "\n")
archivoDeResultados.write("*\tCantidad de personas que cursaron de Presencial:\t" + str(contadorModalidadPresencial) + "\n")
archivoDeResultados.write("-"*20)
archivoDeResultados.write("\nParticipantes por seminario:" + "\n\n")
archivoDeResultados.write("*\tCantidad de personas que cursaron de IA en Naturales:\t" + str(contadorSeminarioIAenNaturales) + "\n")
archivoDeResultados.write("*\tCantidad de personas que cursaron de RRHH:\t" + str(contadorSeminarioRRHH) + "\n")
archivoDeResultados.write("*\tCantidad de personas que cursaron de Liderazgo:\t" + str(contadorSeminarioLiderazgo) + "\n")
archivoDeResultados.write("*\tCantidad de personas que cursaron de Nuevas TEC Software:\t" + str(contadorSeminarioNuevasTECSoftware) + "\n")
archivoDeResultados.write("*\tCantidad de personas que cursaron de Info en la Nube:\t" + str(contadorSeminarioInfoEnLaNube) + "\n")
archivoDeResultados.write("-"*20)
archivoDeResultados.write("\nParticipantes por localidad:" + "\n\n")
archivoDeResultados.write("*\tCantidad de personas que cursaron de Plottier:\t" + str(contadorPlottier) + "\n")
archivoDeResultados.write("*\tCantidad de personas que cursaron de NQN:\t" + str(contadorNQN) + "\n")
archivoDeResultados.write("*\tCantidad de personas que cursaron de Cipolletti:\t" + str(contadorCipolletti) + "\n")
archivoDeResultados.write("*\tCantidad de personas que cursaron de Roca:\t" + str(contadorRoca) + "\n")
archivoDeResultados.write("-"*20)
archivoDeResultados.write("\nRecaudación:" + "\n")
archivoDeResultados.write("*\tImportes totales:\t" + str(acumuladorDeImportesTotales) + "\tpesos\n")
archivoDeResultados.write("\n*\tCantidad de personas que pagaron con efectivo:\t" + str(contadorEfectivo) + "\n")
archivoDeResultados.write("*\tImportes pagados por efectivo:\t" + str(acumuladorDeImportesApagarEfectivo) + "\tpesos\n")
archivoDeResultados.write("\n*\tCantidad de personas que pagaron con tarjeta:\t" + str(contadorTarjeta) + "\n")
archivoDeResultados.write("*\tImportes pagados por tarjeta:\t" + str(acumuladorDeImportesApagarTarjeta) + "\tpesos\n")
archivoDeResultados.write("-"*20)
archivoDeResultados.close() # Archivo de RESULTADOS cerrado en modo escritura.

archivoDeResultados = open(pathArchivoDeResultados, "r") # El archivo de RESULTADOS se abrió en modo lectura.
resultados = archivoDeResultados.read()
archivoDeResultados.close() # El archivo de RESULTADOS se cerró de la apertura del mismo modo lectura.
print(resultados)
input("\nIngrese ENTER para continuar...")
os.system("cls")
print("\nFin del programa =D")