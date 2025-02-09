from webcolors import name_to_hex

def nombre_color_a_codigo(nombre_color):
    try:
        codigo_color = name_to_hex(nombre_color)
        return codigo_color
    except ValueError:
        return "No Existe"

nombre_color = input("Ingrese el nombre del color: ")
resultado_de_codigo = nombre_color_a_codigo(nombre_color)
print(resultado_de_codigo)
