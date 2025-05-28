def RegistrarFecha(dia, mes, año, nombre):    
    try:
        dia = int(dia)
        mes = str(mes).capitalize()
        año = int(año)
        nombre = str(nombre)
    except ValueError:
        print("\n¡Digite una opción valida!")
        return "ErrorGetDia_Mes_Año"

    if mes != "Enero" and mes != "Febrero" and mes != "Marzo" and mes != "Abril" and mes != "Mayo" and mes != "Junio" and mes != "Julio" and mes != "Agosto" and mes != "Septiembre" and mes != "Octubre" and mes != "Noviembre" and mes != "Diciembre":
        print("\n¡Error al Digitar el Mes!")
        return "ErrorMesDiferente"

    if mes == "Enero" or mes == "Marzo" or mes == "Mayo" or mes == "Julio" or mes == "Agosto" or mes == "Octubre" or mes == "Diciembre":
        if dia < 1 or dia > 31:
            print("\n¡Error, el mes que seleccionaste tiene entre (1-31) días!")
            return "ErrorMasDiasDelMes31"
        else:
            pass
    elif mes == "Abril" or mes == "Junio" or mes == "Septiembre" or mes == "Noviembre":
        if dia < 1 or dia > 30:
            print("\n¡Error, el mes que seleccionaste tiene entre (1-30) días!")
            return "ErrorMasDiasDelMes30"
    else:
        if año%4 == 0:
            if dia < 1 or dia > 29:
                print("\n¡Error, el mes que seleccionaste tiene entre (1-29) días!, ¡¡Es año bisiesto!!")
                return "ErrorMasDiasDeFebreroAñoBisiesto"
        else:
            if dia < 1 or dia > 28:
                print("\n¡Error, el mes que seleccionaste tiene entre (1-28) días!")
                return "ErrorMasDiasdeFebrero"
            else:
                pass

    fecha = {"Día": dia,
            "Mes": mes,
            "Año": año,
            "Nombre": nombre}
#Acá se crea o accede al documento 'fechas.txt' y se guardan las fechas allí.
    with open("fechas.txt", "a") as archivo: 
        archivo.write(f"Nombre: {fecha['Nombre']}, Día: {fecha['Día']}, Mes: {fecha['Mes']}, Año: {fecha['Año']}\n")
    return fecha


def MostrarFecha():
    with open("fechas.txt", "r") as archivo:
        obtener = archivo.readlines()  #El metodo .readlines() convierte todas las líneas del archivo en listas.
        if not obtener:
            print("\nAún no ha registrado una cita")
            return False
        else:
            i = len(obtener)
            print(f"\n---Tienes registradas {i} cita/s---\n")
            for contador, f in enumerate(obtener, start=1):
                print(f"{contador}. {f.strip()}") #El metodo .strip() hace que se eliminen espacios al inicio y al final de la lista.
            return [f.strip() for f in obtener]


def BorrarFecha(num_Fecha):
    num_Fecha_qsevaausar = num_Fecha -1

    with open("fechas.txt", "r") as archivo:
        obtener = archivo.readlines()
        if num_Fecha_qsevaausar < 0 or num_Fecha_qsevaausar > len(obtener):
            print("No hay alguna cita registrada con ese número")
            return

        del obtener[num_Fecha_qsevaausar]
        with open("fechas.txt", "w") as archivo:
            archivo.writelines(obtener)
    print(f"\nLa cita {num_Fecha} se ha eliminado con éxito")