from webcolors import name_to_hex

def nombre_color_a_codigo(nombre_color):
    try:
        codigo_color = name_to_hex(nombre_color.lower())  # Convierte a minúsculas
        return f"El código hexadecimal de '{nombre_color}' es: {codigo_color}"
    except ValueError:
        return "Ese color no existe en la lista de webcolors."

nombre_color = input("Ingrese el nombre del color: ")
resultado_de_codigo = nombre_color_a_codigo(nombre_color)
print(resultado_de_codigo)
