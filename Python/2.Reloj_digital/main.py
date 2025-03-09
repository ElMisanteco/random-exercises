import tkinter as tk
from time import strftime

# Crear la ventana principal
root = tk.Tk()
root.title("Reloj Digital")

# Definición de la etiqueta que mostrará el reloj
etiqueta_reloj = tk.Label(root, font=("Helvetica", 50), bg="black", fg="white")
etiqueta_reloj.pack(anchor="center", fill="both", expand=True)

# Función para actualizar la hora
def actualizar_hora():
    hora_actual = strftime("%H:%M:%S")
    etiqueta_reloj.config(text=hora_actual)
    etiqueta_reloj.after(1000, actualizar_hora)

# Iniciar la actualización del reloj
actualizar_hora()
# Iniciar el bucle principal de la ventana
root.mainloop()

