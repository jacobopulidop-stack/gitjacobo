import tkinter as tk
from tkinter import ttk, messagebox

ventana = tk.Tk()  # Instanciar ventana principal
ventana.title("Saludo interactivo")
ventana.geometry("360x180")


def saludar():  # Función invocada cuando se hace clic
    nombre = entrada.get().strip()  # Leer y quitar espacios extremos

    if not nombre:  # Comprobar que exista un nombre
        messagebox.showwarning("Dato requerido", "Ingrese su nombre")
        return  # Detener el procesamiento si está vacío

    messagebox.showinfo("Saludo", f"¡Hola, {nombre}!")  # Mostrar mensaje de saludo


ttk.Label(ventana, text="Nombre:").pack(pady=(10, 4))

entrada = ttk.Entry(ventana)  # Crear campo de entrada
entrada.pack(pady=4, fill="x", padx=20)

ttk.Button(
    ventana,
    text="Saludar",
    command=saludar
).pack(pady=12)

ventana.mainloop()  # Ejecutar interfaz