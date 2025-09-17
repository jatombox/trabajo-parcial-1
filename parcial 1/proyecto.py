import tkinter as tk
from tkinter import messagebox, Toplevel

# ---configuracion del icono---

icono = "conversion.ico"


# ---funciones de la calculadora---


def celsius_a_fahrenheit():
    try:
        c = float(entry_valor.get())
        f = (c * 9/5) + 32
        etiqueta_resultado.config(text=f"{c} °C = {f:.1f} °F")
    except:
        etiqueta_resultado.config(text="Ingresa un número válido.")


def km_a_millas():
    try:
        km = float(entry_valor.get())
        mi = km * 0.6214
        etiqueta_resultado.config(text=f"{km} km = {mi:.2f} mi")
    except:
        etiqueta_resultado.config(text="Ingresa un número válido.")


def kg_a_libras():
    try:
        kg = float(entry_valor.get())
        lb = kg * 2.2046
        etiqueta_resultado.config(text=f"{kg} kg = {lb:.2f} lb")
    except:
        etiqueta_resultado.config(text="Ingresa un número válido.")


def salir():
    """
    cierra la aplicacion
    """
    ventana.quit()


def mostrar_info():
    """
    mostrar ayuda
    """
    messagebox.showinfo(
        "Ayuda",
        "esta es una calculadora simple que permite realizar diferentes tipos de conversiones\n\n"
    )


def mostrar_ayuda():
    """abrir ventana con markdown"""
    nueva = Toplevel(ventana)
    nueva.title("acerca de la calculadora de conversion")
    nueva.geometry("500x300")

   # c
    etiqueta_instruccion = tk.Label(
        nueva, text="Crado por: Jacobo Morales\nVersion 1.0\n2025")
    etiqueta_instruccion.pack(pady=10)


def mostrar_tutorial():
    messagebox.showinfo(
        "Tutorial", "Ingresa un número y haz clic en un botón para convertir.")

# --- Configuracion de la interfaz grafica ---


# crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora conversion")
ventana.geometry("500x300")

# configurar el icono de la ventana
try:
    ventana.iconbitmap(icono)
except tk.TclError:
    print(
        f"Advertencia No se pudo cargar el icono desde: {icono}")


# --Menu desplegable--
barra_menu = tk.Menu(ventana)

# Menu archivo

menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="tutorial", command=mostrar_tutorial)
menu_archivo.add_command(label="salir", command=salir)
barra_menu.add_cascade(label="inicio", menu=menu_archivo)

# Menu calculadora

menu_calculadora = tk.Menu(barra_menu, tearoff=0)
menu_calculadora.add_command(label="°C a °F", command=celsius_a_fahrenheit)
menu_calculadora.add_command(label="Km a Mi", command=km_a_millas)
menu_calculadora.add_command(label="Kg a Li", command=kg_a_libras)
barra_menu.add_cascade(label="calcular", menu=menu_calculadora)

# Menu ayuda

menu_ayuda = tk.Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Mostrar ayuda", command=mostrar_info)
menu_ayuda.add_command(label="Acerca de", command=mostrar_ayuda)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

# asignar la barra de menu a la ventana

ventana.config(menu=barra_menu)

# crear y colocar los widgets

etiqueta_instruccion = tk.Label(
    ventana, text="ingrese el valor que desee transformar :")
etiqueta_instruccion.pack(pady=10)

etiqueta_valor = tk.Label(ventana, text="valor:")
etiqueta_valor.pack()
entry_valor = tk.Entry(ventana)
entry_valor.pack()


# crear un marco para grupar lo botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

# crear y colocar los botones
button_celsius_a_fahrenheit = tk.Button(
    frame_botones, text="celsius a fahrenheit", command=celsius_a_fahrenheit)
button_celsius_a_fahrenheit.pack(side=tk.LEFT, padx=5)

button_Km_a_millas = tk.Button(
    frame_botones, text="km a millas", command=km_a_millas)
button_Km_a_millas.pack(side=tk.LEFT, padx=5)

button_kg_a_libras = tk.Button(
    frame_botones, text="kg a libras", command=kg_a_libras)
button_kg_a_libras.pack(side=tk.LEFT, padx=5)
# crear y colocar la etiqueta de resultado

etiqueta_resultado = tk.Label(ventana, text="Resultado:")
etiqueta_resultado.pack()

# iniciar bucle principal de la ventana
ventana.mainloop()
