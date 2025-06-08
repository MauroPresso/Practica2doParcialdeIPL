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

# Inicio ciclo for.
for i in range(3):
    id = i + 1
    
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
        areaDeFormacion = "TECNOLÓGICAS"
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
        localidad = "Neuquén Capital"
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
        seminario = "IA EN LAS ÁREAS NATURALES"
        importePorEncuentro = 12500
        contadorSeminarioIAenNaturales += 1
    elif codigoDeSeminario == "B":
        seminario = "LIDERAZGO SIGLO XXI"
        importePorEncuentro = 8900
        contadorSeminarioLiderazgo += 1
    elif codigoDeSeminario == "C":
        seminario = "ADMINISTRACIÓN DE RRHH"
        importePorEncuentro = 10500
        contadorSeminarioRRHH += 1
    elif codigoDeSeminario == "D":
        seminario = "NUEVAS TECNOLOGÍAS DE SOFTWARE"
        importePorEncuentro = 11000
        contadorSeminarioNuevasTECSoftware += 1
    else: # codigoDeSeminario == "E"
        seminario = "INFORMÁTICA EN LA NUBE"
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

    # Muestro los datos de la persona.
    print("\n-----------------DATOS DE LA PERSONA-----------------")
    print("ID:", id)
    print("Nombre:", nombre)
    print("Apellido:", apellido)
    print("Edad:", edad)
    print("Area de formacion:", areaDeFormacion)
    print("Localidad:", localidad)
    print("Seminario:", seminario)
    print("Modalidad:", modalidad)
    print("Lugar de cursado:", lugarDeCursado)
    print(f"Importe por encuentro: {importePorEncuentro} pesos")
    print("Cantidad de encuentros:", cantidadDeEncuentros)
    print(f"Importe total: {importeTotal} pesos")
    print("Modalidad de pago:", modalidadDePago)
    if modalidadDePago == "Efectivo":
        print("Importe a pagar: ", importeApagar, "pesos")
    else: # modalidadDePago == "Tarjeta":
        print("Importe a pagar: ", importeApagar, "pesos")
    print("--------------------------------------------------------")
    input("\nIngrese cualquier tecla para continuar:\t")
    os.system("cls")
# Fin del ciclo for.

print("\n\n\n----------------RESULTADOS---------------------")
print("\nParticipantes por área de formación:")
print("Cantidad de personas que cursaron de administrativa:", contadorAreaAdministrativa)
print("Cantidad de personas que cursaron de Naturales:", contadorAreaNaturales)
print("Cantidad de personas que cursaron de Tecnologicas:", contadorAreaTecnologicas)
print("\n\nParticipantes por modalidad:")
print("Cantidad de personas que cursaron de Mixta:", contadorModalidadMixta)
print("Cantidad de personas que cursaron de Virtual:", contadorModalidadVirtual)
print("Cantidad de personas que cursaron de Presencial:", contadorModalidadPresencial)
print("\n\nParticipantes por seminario:")
print("Cantidad de personas que cursaron de IA en Naturales:", contadorSeminarioIAenNaturales)
print("Cantidad de personas que cursaron de RRHH:", contadorSeminarioRRHH)
print("Cantidad de personas que cursaron de Liderazgo:", contadorSeminarioLiderazgo)
print("Cantidad de personas que cursaron de Nuevas TEC Software:", contadorSeminarioNuevasTECSoftware)
print("Cantidad de personas que cursaron de Info en la Nube:", contadorSeminarioInfoEnLaNube)
print("\n\nParticipantes por localidad:")
print("Cantidad de personas que cursaron de Plottier:", contadorPlottier)
print("Cantidad de personas que cursaron de NQN:", contadorNQN)
print("Cantidad de personas que cursaron de Cipolletti:", contadorCipolletti)
print("Cantidad de personas que cursaron de Roca:", contadorRoca)
print("\n\nRecaudación:")
print("\nImportes totales: ", acumuladorDeImportesTotales, "pesos")
print("\nCantidad de personas que pagaron con efectivo: ", contadorEfectivo)
print("Importes pagados por efectivo: ", acumuladorDeImportesApagarEfectivo, "pesos")
print("\nCantidad de personas que pagaron con tarjeta: ", contadorTarjeta)
print("Importes pagados por tarjeta: ", acumuladorDeImportesApagarTarjeta, "pesos")
print("--------------------------------------------------------")
input("\nPresione ENTER para continuar...") 
print("\nFin del programa.")