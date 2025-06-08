import os
os.system("cls")
from io import open

# Programa principal

#Creando listas
ListaDeNombres = []
ListaDeApellidos = []
ListaIDs = []
ListaDeModalidad = []
ListaDeMaterias = []
ListaDeProfesores = []
ListaDeAulas = []
ListaDeHorarios = []
ListaDePromedios = []
ListaDeCondiciones = []
ListaDeDefensa = []
ListaDeExamen = []
ListaDeFechas = []

#Cantidad de promocionados, regulares, libres y ausentes
contPromo,contRegu,contLibres,contAus = 0,0,0,0

#Cantidad de estudiantes por materia
contIPL,contSist,contMath,contEngl = 0,0,0,0

#Cantidad de promocionados por materia
contPromoIPL,contPromoSist,contPromoMath,contPromoEngl = 0,0,0,0

#Cantidad de regulares por materia
contReguIPL,contReguSist,contReguMath,contReguEngl = 0,0,0,0

#Cantidad de alumnos libres por materia
contLibresIPL,contLibresSist,contLibresMath,contLibresEngl = 0,0,0,0

#Cantidad de ausentes por materia
contAusIPL,contAusSist,contAusMath,contAusEngl = 0,0,0,0

#Cantidad de estudiantes según modalidad y materia
contIPLPresencial,contIPLVirtual,contIPLMixta = 0,0,0
contSistPresencial,contSistVirtual,contSistMixta = 0,0,0
contMathPresencial,contMathVirtual,contMathMixta = 0,0,0
contEnglPresencial,contEnglVirtual,contEnglMixta = 0,0,0
#...
cantidadDeAlumnos = int(input("Cantidad de alumnos: "))
while cantidadDeAlumnos <= 0:
    print("Cantidad de alumnos no valida")
    cantidadDeAlumnos = int(input("Cantidad de alumnos: "))



print("\nIngrese los datos de los alumnos:\n")
for i in range(cantidadDeAlumnos):
    print(f"\n\nAlumno {i+1}:\n")
    id = i + 1

    nombre = input("Nombre del alumno: ").capitalize()
    apellido = input("Apellido del alumno: ").upper()
    
    codigoDeMateria = int(input("\nIngrese el código de la materia\n100: Introduccion al pensamiento logico\n200: Sistemas de computacion\n300: Matematica\n400: Ingles\nIngrese aquí: "))
    while codigoDeMateria not in [100, 200, 300, 400]:
        print("Dato erroneo. Intente nuevamente")
        codigoDeMateria = int(input("\nIngrese el código de la materia\n100: Introduccion al pensamiento logico\n200: Sistemas de computacion\n300: Matematica\n400: Ingles\nIngrese aquí: "))

    print("\nIngrese las notas del alumno (1 a 10): ")
    sumaNotas = 0
    for i in range(3): # Son 3 notas.
        nota = int(input(f"Nota {i+1}: "))
        while nota < 1 or nota > 10:
            print("Nota no valida")
            nota = int(input(f"Nota {i+1}: "))
        sumaNotas += nota
    promedio = sumaNotas / 3

    tipoDeModalidad = input("\nTipo de modalidad (V/P/M): ").upper()
    while tipoDeModalidad not in ["V", "P", "M"]:
        print("Tipo de modalidad no valida")
        tipoDeModalidad = input("Tipo de modalidad (V/P/M): ").upper()

    # GENERANDO DATOS.

    # Definiendo la materia.
    if codigoDeMateria == 100:
        materia = "Introduccion al pensamiento logico"
        profesor = "Juan Perez"
    elif codigoDeMateria == 200:
        materia = "Sistemas de computacion"
        profesor = "Andrea Garrido"
    elif codigoDeMateria == 300:
        materia = "Matematica"
        profesor = "Sebastian Prost"
    else: # codigoDeMateria == 400
        materia = "Ingles"
        profesor = "Andrea Gomez"

    # Definiendo la condicion del alumno.
    if promedio>=7:
        condicion = "Promocion"
        defensa = "NO"
        examen = "NO"
        fecha = "Directo"
    elif promedio>=4:
        condicion = "Regular"
        defensa = "SI"
        examen = "SI"
        fecha = "10/07/2025"
    elif promedio>=3:
        condicion = "Libre"
        defensa = "NO"
        examen = "SI"
        fecha = "14/07/2025"
    else:
        condicion = "Ausente"
        defensa = "NO"
        examen = "NO"
        fecha = "Recursa"
    
    # Definiendo el tipo de modalidad.
    if tipoDeModalidad == "V":
        modalidad = "Virtual"
    elif tipoDeModalidad == "P":
        modalidad = "Presencial"
    else:
        modalidad = "Mixta"

    # Definiendo aula y horario.
    if modalidad == "Presencial":
        if materia == "Introduccion al pensamiento logico":
            aula = "1"
            horario = "Lunes 19:00 a 21:00"
        elif materia == "Sistemas de computacion":
            aula = "8"
            horario = "Jueves 20:30 a 22:00"
        elif materia == "Matematica":
            aula = "12"
            horario = "Viernes 19:00 a 21:00"
        else: # materia == "Ingles"
            aula = "15"
            horario = "Martes 19:00 a 20:30"
    elif modalidad == "Virtual":
        if materia == "Introduccion al pensamiento logico":
            aula = "Zoom"
            horario = "Lunes 19:00 a 21:00"
        elif materia == "Sistemas de computacion":
            aula = "Meet"
            horario = "Jueves 20:30 a 22:00"
        elif materia == "Matematica":
            aula = "Meet"
            horario = "Viernes 19:00 a 21:00"
        else: # materia == "Ingles"
            aula = "Zoom"
            horario = "Martes 19:00 a 20:30"
    else: # modalidad == "Mixta"
        if materia == "Introduccion al pensamiento logico":
            aula = "Zoom"
            horario = "Miercoles 19:00 a 20:40"
        elif materia == "Sistemas de computacion":
            aula = "8"
            horario = "Lunes 19:00 a 21:00"
        elif materia == "Matematica":
            aula = "12"
            horario = "Miercoles 21:00 a 22:40"
        else: # materia == "Ingles"
            aula = "Zoom"
            horario = "Jueves 19:00 a 20:30"
        
    # Contadores
    
    # Contando alumnos por materia y modalidad. Inciso g).
    if materia == "Introduccion al pensamiento logico":
        contIPL += 1
        if modalidad == "Presencial":
            contIPLPresencial += 1
        elif modalidad == "Virtual":
            contIPLVirtual += 1
        else: # modalidad == "Mixta"
            contIPLMixta += 1
    elif materia == "Sistemas de computacion":
        contSist += 1
        if modalidad == "Presencial":
            contSistPresencial += 1
        elif modalidad == "Virtual":
            contSistVirtual += 1
        else: # modalidad == "Mixta"
            contSistMixta += 1
    elif materia == "Matematica":
        contMath += 1
        if modalidad == "Presencial":
            contMathPresencial += 1
        elif modalidad == "Virtual":
            contMathVirtual += 1
        else: # modalidad == "Mixta"
            contMathMixta += 1
    else: # materia == "Ingles"
        contEngl += 1
        if modalidad == "Presencial":
            contEnglPresencial += 1
        elif modalidad == "Virtual":
            contEnglVirtual += 1
        else: # modalidad == "Mixta"
            contEnglMixta += 1
    
    # Contado por condicion y por materia.
    if condicion == "Promocion":
        contPromo += 1
        if materia == "Introduccion al pensamiento logico":
            contPromoIPL += 1
        elif materia == "Sistemas de computacion":
            contPromoSist += 1
        elif materia == "Matematica":
            contPromoMath += 1
        else: # materia == "Ingles"
            contPromoEngl += 1
    elif condicion == "Regular":
        contRegu += 1
        if materia == "Introduccion al pensamiento logico":
            contReguIPL += 1
        elif materia == "Sistemas de computacion":
            contReguSist += 1
        elif materia == "Matematica":
            contReguMath += 1
        else: # materia == "Ingles"
            contReguEngl += 1
    elif condicion == "Libre":
        contLibres += 1
        if materia == "Introduccion al pensamiento logico":
            contLibresIPL += 1
        elif materia == "Sistemas de computacion":
            contLibresSist += 1
        elif materia == "Matematica":
            contLibresMath += 1
        else: # materia== "Ingles"
            contLibresEngl += 1
    else: # condicion == "Ausente"
        contAus += 1
        if materia == "Introduccion al pensamiento logico":
            contAusIPL += 1
        elif materia == "Sistemas de computacion":
            contAusSist += 1
        elif materia == "Matematica":
            contAusMath += 1
        else: # materia == "Ingles"
            contAusEngl += 1
    
    # GUARDANDO LOS DATOS DEL ALUMNO EN LISTAS:
    ListaDeNombres.append(nombre)
    ListaDeApellidos.append(apellido)
    ListaIDs.append(id)
    ListaDeModalidad.append(modalidad)
    ListaDeMaterias.append(materia)
    ListaDeProfesores.append(profesor)
    ListaDeAulas.append(aula)
    ListaDeHorarios.append(horario)
    ListaDePromedios.append(promedio)
    ListaDeCondiciones.append(condicion)
    ListaDeDefensa.append(defensa)
    ListaDeExamen.append(examen)
    ListaDeFechas.append(fecha)

# Como terminó el ciclo for, las listas ya están llenas y listas para ser guardadas en un archivo.
pathArchivoDeDatos = "D:/Facultad/IFES/Materias/1erCuatri1erAnio/IntroAlPensamientoLogico/Practica2doParcial/datosDelPrograma.txt"
archivoDeDatos = open(pathArchivoDeDatos, "w") # El archivo de DATOS se abrió en modo (sobre)escritura.
archivoDeDatos.write("DATOS DE LOS ALUMNOS:\n")
archivoDeDatos.write("-"*20)
archivoDeDatos.close() # El archivo de DATOS se cerró de la apertura del mismo modo (sobre)escritura.
for i in range(cantidadDeAlumnos):
    archivoDeDatos = open(pathArchivoDeDatos, "a") # El archivo de DATOS se abrió para agregar al final.
    archivoDeDatos.write("\nALUMNO\t" + str(i+1) + ":\n")
    archivoDeDatos.write( "*\tNombre completo:\t" + ListaDeNombres[i] + "\t" + ListaDeApellidos[i] + "\n")
    archivoDeDatos.write("*\tID:\t" + str(ListaIDs[i]) + "\n")
    archivoDeDatos.write("*\tModalidad:\t" + ListaDeModalidad[i] + "\n")
    archivoDeDatos.write("*\tMateria:\t" + ListaDeMaterias[i] + "\n")
    archivoDeDatos.write("*\tProfesor:\t" + ListaDeProfesores[i] + "\n")
    archivoDeDatos.write("*\tAula:\t" + ListaDeAulas[i] + "\n")
    archivoDeDatos.write("*\tHorario:\t" + ListaDeHorarios[i] + "\n")
    archivoDeDatos.write("*\tPromedio:\t" + str(ListaDePromedios[i]) + "\n")
    archivoDeDatos.write("*\tCondicion:\t" + ListaDeCondiciones[i] + "\n")
    archivoDeDatos.write("*\tDefensa:\t" + ListaDeDefensa[i] + "\n")
    archivoDeDatos.write("*\tExamen:\t" + ListaDeExamen[i] + "\n")
    archivoDeDatos.write("*\tFecha:\t" + ListaDeFechas[i] + "\n")
    archivoDeDatos.write("-"*20)
    archivoDeDatos.close() # El archivo de DATOS se cerró de la apertura del mismo modo.
os.system("cls")
archivoDeDatos = open(pathArchivoDeDatos, "r") # El archivo de DATOS se abrió en modo lectura.
datos = archivoDeDatos.read()
archivoDeDatos.close() # El archivo de DATOS se cerró de la apertura del mismo modo lectura.
print(datos)
input("\nIngrese ENTER para continuar...")
os.system("cls")

# Como terminó el ciclo for, los resultados están listos para ser guardados en un archivo.
pathArchivoDeResultados = "D:/Facultad/IFES/Materias/1erCuatri1erAnio/IntroAlPensamientoLogico/Practica2doParcial/ResultadosDelPrograma.txt"
archivoDeResultados = open(pathArchivoDeResultados, "w") # El archivo de RESULTADOS se abrió en modo (sobre)escritura.
archivoDeResultados.write("REPORTE FINAL:\n")
archivoDeResultados.write("-"*20)
# Inciso b)
archivoDeResultados.write("\nTotal de alumnos por materia:\n\n")
archivoDeResultados.write("*\tIntroduccion al pensamiento logico:\t" + str(contIPL) + "\n")
archivoDeResultados.write("*\tSistemas de computacion:\t" + str(contSist) + "\n")
archivoDeResultados.write("*\tMatematica:\t" + str(contMath) + "\n")
archivoDeResultados.write("*\tIngles:\t" + str(contEngl) + "\n")
archivoDeResultados.write("-"*20)
# Inciso g)
archivoDeResultados.write("\nTotal de alumnos por modalidad y materia:\n\n")
archivoDeResultados.write("Introduccion al pensamiento logico:\n")
archivoDeResultados.write("*\tPresencial:\t" + str(contIPLPresencial) + "\n")
archivoDeResultados.write("*\tVirtual:\t" + str(contIPLVirtual) + "\n")
archivoDeResultados.write("*\tMixta:\t" + str(contIPLMixta) + "\n")
archivoDeResultados.write("\nSistemas de computacion:\n")
archivoDeResultados.write("*\tPresencial:\t" + str(contSistPresencial) + "\n")
archivoDeResultados.write("*\tVirtual:\t" + str(contSistVirtual) + "\n")
archivoDeResultados.write("*\tMixta:\t" + str(contSistMixta) + "\n")
archivoDeResultados.write("\nMatematica:\n")
archivoDeResultados.write("*\tPresencial:\t" + str(contMathPresencial) + "\n")
archivoDeResultados.write("*\tVirtual:\t" + str(contMathVirtual) + "\n")
archivoDeResultados.write("*\tMixta:\t" + str(contMathMixta) + "\n")
archivoDeResultados.write("\nIngles:\n")
archivoDeResultados.write("*\tPresencial:\t" + str(contEnglPresencial) + "\n")
archivoDeResultados.write("*\tVirtual:\t"+ str(contEnglVirtual) + "\n")
archivoDeResultados.write("*\tMixta:\t" + str(contEnglMixta) + "\n")
archivoDeResultados.write("-"*20)
# Inciso a)
archivoDeResultados.write("\nTotal de alumnos por condicion:\n\n")
archivoDeResultados.write("*\tTotal de alumnos promocionados:\t" + str(contPromo) + "\n")
archivoDeResultados.write("*\tTotal de alumnos regulares:\t" + str(contRegu) + "\n")
archivoDeResultados.write("*\tTotal de alumnos libres:\t" + str(contLibres) + "\n")
archivoDeResultados.write("*\tTotal de alumnos ausentes:\t" + str(contAus) + "\n")
archivoDeResultados.write("-"*20)
# Inciso c)
archivoDeResultados.write("\nTotal de alumnos promocionados por materia:\n\n")
archivoDeResultados.write("*\tIntroduccion al pensamiento logico:\t" + str(contPromoIPL) + "\n")
archivoDeResultados.write("*\tSistemas de computacion:\t" + str(contPromoSist) + "\n")
archivoDeResultados.write("*\tMatematica:\t" + str(contPromoMath) + "\n")
archivoDeResultados.write("*\tIngles:\t" + str(contPromoEngl) + "\n")
archivoDeResultados.write("-"*20)
# Inciso d)
archivoDeResultados.write("\nTotal de alumnos regulares por materia:\n\n")
archivoDeResultados.write("*\tIntroduccion al pensamiento logico:\t" + str(contReguIPL) + "\n")
archivoDeResultados.write("*\tSistemas de computacion:\t" + str(contReguSist) + "\n")
archivoDeResultados.write("*\tMatematica:\t" + str(contReguMath) + "\n")
archivoDeResultados.write("*\tIngles:\t" + str(contReguEngl) + "\n")
archivoDeResultados.write("-"*20)
# Inciso e)
archivoDeResultados.write("\nTotal de alumnos libres por materia:\n\n")
archivoDeResultados.write("*\tIntroduccion al pensamiento logico:\t" + str(contLibresIPL) + "\n")
archivoDeResultados.write("*\tSistemas de computacion:\t" + str(contLibresSist) + "\n")
archivoDeResultados.write("*\tMatematica:\t" + str(contLibresMath) + "\n")
archivoDeResultados.write("*\tIngles:\t" + str(contLibresEngl) + "\n")
archivoDeResultados.write("-"*20)
# Inciso f)
archivoDeResultados.write("\nTotal de alumnos ausentes por materia:\n\n")
archivoDeResultados.write("*\tIntroduccion al pensamiento logico:\t" + str(contAusIPL) + "\n")
archivoDeResultados.write("*\tSistemas de computacion:\t" + str(contAusSist) + "\n")
archivoDeResultados.write("*\tMatematica:\t" + str(contAusMath) + "\n")
archivoDeResultados.write("*\tIngles:\t" + str(contAusEngl) + "\n")
archivoDeResultados.write("-"*20)
archivoDeResultados.close() # El archivo de RESULTADOS se cerró de la apertura del mismo modo (sobre)escritura.

archivoDeResultados = open(pathArchivoDeResultados, "r") # El archivo de RESULTADOS se abrió en modo lectura.
resultados = archivoDeResultados.read()
archivoDeResultados.close() # El archivo de RESULTADOS se cerró de la apertura del mismo modo lectura.
print(resultados)
input("\nIngrese ENTER para continuar...")
os.system("cls")
print("\nFin del programa =D")