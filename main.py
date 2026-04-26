from clases import ArchivoSIATA, ArchivoEEG

def menu():
    while True:
        print("Seleccione una opción:")
        print("1. Trabajar con archivo CSV (SIATA)")
        print("2. Trabajar con archivo EEG (.MAT)")
        print("3. Salir")

        opcion = input("Ingrese el número de la opción: ")

        if opcion == "1":
            ruta = input("Ingrese la ruta del archivo CSV: ")
            siata = ArchivoSIATA(ruta)
            while True:
                print("\nOpciones para CSV:")
                print("1. Información básica")
                print("2. Gráficos")
                print("3. Operaciones")
                print("4. Remuestreo")
                print("5. Volver al menú principal")

                op2 = input("Ingrese el número de la opción: ")

                if op2 == "1":
                    siata.info_basica()
                elif op2 == "2":
                    print("Columnas disponibles:")
                    print(siata.data.columns)
                    col = input("Ingrese la columna: ")
                    if siata.validar_columna(col):
                        siata.graficos(col)
                elif op2 == "3":
                    print(siata.data.columns)
                    c1 = input("Ingrese el nombre de la columna 1: ")
                    c2 = input("Ingrese el nombre de la columna 2: ")
                    if siata.validar_columna(c1) and siata.validar_columna(c2):
                        siata.operaciones(c1, c2)
                elif op2 == "4":
                    fecha = input("Ingrese la columna de fecha: ")
                    valor = input("Ingrese la columna de valor: ")
                    siata.remuestreo(fecha, valor)
                elif op2 == "5":
                    break
            
        elif opcion == "2":
            ruta = input("Ingrese la ruta del archivo EEG (.MAT): ")
            eeg = ArchivoEEG(ruta)

            eeg.ver_llaves()

            while True: 
                print("\nOpciones para EEG:")
                print("1. Sumar canales")
                print("2. Estadísticas")
                print("3. Volver al menú principal")

                op3 = input("Ingrese el número de la opción: ")

                if op3 == "1":
                    key = input("Nombre variable: ")
                    c1 = int(input("Canal 1: "))
                    c2 = int(input("Canal 2: "))
                    c3 = int(input("Canal 3: "))
                    inicio = int(input("Inicio: "))
                    fin = int(input("Fin: "))
                    eeg.sumar_canales(key, c1, c2, c3, inicio, fin)
                elif op3 == "2":
                    key = input("Nombre variable: ")
                    eeg.estadisticas(key)
                elif op3 == "3":
                    break
      
        elif opcion == "3":
            print("Saliendo del programa.")
            break

menu ()