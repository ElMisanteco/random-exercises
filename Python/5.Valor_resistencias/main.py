colores = ["negro", "marron", "rojo", "naranja", "amarillo", "verde", "azul", "violeta", "gris", "blanco"]

try:
    n = colores.index(input("Ingrese el primer color: ").strip().lower())
    m = colores.index(input("Ingrese el segundo color: ").strip().lower())
    p = colores.index(input("Ingrese el tercer color: ").strip().lower())

    resistencia = ((n * 10) + m) * (10 ** p)
    kiloohms = resistencia / 1000

    print("\nEl valor de la resistencia es:")
    print(f"{resistencia} Ohms ({kiloohms} kΩ)")

except ValueError:
    print("\nError: Uno de los colores ingresados no es válido.")
