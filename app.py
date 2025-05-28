import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Logica import RegistrarFecha, MostrarFecha, BorrarFecha  # importa la función del otro archivo

#Funciones para las funciones del programa

def RegistrarFecha_GUI():
    dia = entrada_dia.get()
    mes = entrada_mes.get()
    año = entrada_año.get()
    nombre = entrada_nombre.get()

    FechaAgregada = RegistrarFecha(dia, mes, año, nombre)
    if "ErrorGetDia_Mes_Año" in FechaAgregada:
        messagebox.showerror("Error", "¡Digite bien el día, mes, año o nombre!")
    elif "ErrorMesDiferente" in FechaAgregada:
        messagebox.showerror("Error", "¡Error al Digitar el Mes!")
    elif "ErrorMasDiasDelMes31" in FechaAgregada:
        messagebox.showerror("Error", "¡El mes que seleccionaste tiene entre (1-31) días!")
    elif "ErrorMasDiasDelMes30" in FechaAgregada:
        messagebox.showerror("Error", "¡El mes que seleccionaste tiene entre (1-30) días!")
    elif "ErrorMasDiasDeFebreroAñoBisiesto" in FechaAgregada:
        messagebox.showerror("Error","¡El mes que seleccionaste tiene entre (1-29) días!, ¡¡Es año bisiesto!!")
    elif "ErrorMasDiasdeFebrero" in FechaAgregada:
        messagebox.showerror("Error", "¡El mes que seleccionaste tiene entre (1-28) días!")
    else:
        messagebox.showinfo(f"La cita \"{FechaAgregada['Nombre']}\" fue agregada con éxito", f"Cita registrada:\n{FechaAgregada}")
    
    entrada_dia.delete(0, tk.END)
    entrada_mes.delete(0, tk.END)
    entrada_año.delete(0, tk.END)
    entrada_nombre.delete(0, tk.END)

#Tabla para mostrar
tabla = None
def MostrarFechas_GUI():
    global tabla
    tabla = ttk.Treeview(ventana, columns=("ID", "Citas",), show="headings")
    tabla.heading("ID", text='ID')
    tabla.heading("Citas", text="Citas Registradas")
    tabla.column("Citas", width=450)
    tabla.column("ID", width=80)
    tabla.grid(row=6, column=0, columnspan=4)

    # Insertar las citas
    for contador,cita in enumerate(MostrarFecha(), start=1):
        tabla.insert("", "end", values=(contador, cita))
    return tabla

def NoMostrarFechas_GUI():
    for item in tabla.get_children():
        tabla.delete(item)

def BorrarFecha_GUI():
    seleccion = tabla.selection()
    if not seleccion:
        messagebox.showwarning("Advertencia", "Seleccione una cita para eliminar.")
        return

    fechaseleccionada= tabla.item(seleccion)
    id_cita = fechaseleccionada["values"][0]

    confirmacion = messagebox.askyesno("Confirmar eliminación", f"¿Estás seguro de que deseas eliminar la cita número {id_cita}?")
    if confirmacion:
        BorrarFecha(id_cita)
        tabla.delete(seleccion)
        messagebox.showinfo("Cita eliminada", f"La cita número {id_cita} ha sido eliminada con éxito.")


# Creación del GUI(Interfaz)
ventana = tk.Tk()
ventana.title("Scheduler")
ventana.geometry("750x550")

TituloLabel = tk.Label(ventana, text="Registro de Citas")
TituloLabel.config(font=('Arial', 12, 'bold'))
TituloLabel.grid(row=0,column=1, padx=10, pady=10)

DiaLabel = tk.Label(ventana, text="Día:")
DiaLabel.config(font=('Arial', 12, 'bold'))
DiaLabel.grid(row=1 , column=0, padx=10, pady=10)
entrada_dia = tk.Entry(ventana)
entrada_dia.config(width=50, font=('Arial', 12),)
entrada_dia.grid(row=1 , column=1, padx=10, pady=10, columnspan=2)

MesLabel = tk.Label(ventana, text="Mes:")
MesLabel.config(font=('Arial', 12, 'bold'))
MesLabel.grid(row=2 , column=0, padx=10, pady=10)
entrada_mes = tk.Entry(ventana)
entrada_mes.config(width=50, font=('Arial', 12),)
entrada_mes.grid(row=2 , column=1, padx=10, pady=10, columnspan=2)

AñoLabel = tk.Label(ventana, text="Año:")
AñoLabel.config(font=('Arial', 12, 'bold'))
AñoLabel.grid(row=3 , column=0, padx=10, pady=10)
entrada_año = tk.Entry(ventana)
entrada_año.config(width=50, font=('Arial', 12),)
entrada_año.grid(row=3 , column=1, padx=10, pady=10, columnspan=2)

NombreLabel = tk.Label(ventana, text="Nombre:")
NombreLabel.config(font=('Arial', 12, 'bold'))
NombreLabel.grid(row=4 , column=0, padx=10, pady=10)
entrada_nombre = tk.Entry(ventana)
entrada_nombre.config(width=50, font=('Arial', 12),)
entrada_nombre.grid(row=4 , column=1, padx=10, pady=10, columnspan=2)

"""Creación de botones"""

#Botón registrar
RegistrarBoton = tk.Button(ventana, text="Registrar", command=RegistrarFecha_GUI)
RegistrarBoton.config(width=20, font=('Arial', 12, 'bold'), fg='white', background='#28a61b', cursor='hand2', activebackground="#1bd820")
RegistrarBoton.grid(row=5, column=0, padx=10, pady=10)

# Contenedor para los botones
boton_frame = tk.Frame(ventana)
boton_frame.grid(row=5, column=1, columnspan=1, pady=10)

# Botón Mostrar
MostrarBoton = tk.Button(boton_frame, text="Mostrar", command=MostrarFechas_GUI)
MostrarBoton.config(width=10, font=('Arial', 12, 'bold'), fg='white', background='#0015c4', cursor='hand2', activebackground='#2266f6')
MostrarBoton.pack(side=tk.LEFT)

# Botón Quitar
NoMostrarBoton = tk.Button(boton_frame, text='Quitar', command=NoMostrarFechas_GUI)
NoMostrarBoton.config(width=10, font=('Arial', 12, 'bold'), fg='white', background='#0015c4', cursor='hand2', activebackground='#2266f6')
NoMostrarBoton.pack(side=tk.LEFT)

#Botón Borrar
BorrarBoton = tk.Button(ventana, text="Borrar", command=BorrarFecha_GUI)
BorrarBoton.config(width=20, font=('Arial', 12, 'bold'), fg='white', background='#e10000', cursor='hand2', activebackground='#fd1f1f')
BorrarBoton.grid(row=5, column=2, padx=10, pady=10)

ventana.mainloop()