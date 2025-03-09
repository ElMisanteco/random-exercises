# Definimos la altura del árbol (número de filas del triángulo)
altura = 9  # Puedes cambiar este número para hacer el árbol más grande o pequeño

# Hacemos el triángulo
for i in range(altura):
    # Los espacios antes de los asteriscos
    espacios = " " * (altura - i - 1)
    # Los asteriscos
    asteriscos = "*" * (2 * i + 1)
    # Juntamos espacios y asteriscos y los mostramos
    print(espacios + asteriscos)

# Hacemos el tronco
for i in range(3):  # 3 filas de tronco
    # Centramos el tronco usando espacios
    print(" " * (altura - 2) + "| |")