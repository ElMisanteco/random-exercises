import random

cara_moneda_usuario = input("¿Cara o cruz?\n").upper()

cara_moneda = random.choice(["CARA", "CRUZ"])

if cara_moneda_usuario == cara_moneda:
    print (f"Cayó {cara_moneda}, felicidades ganaste. :D")
else:
    print(f"Cayó {cara_moneda}, lo siento perdiste. :(")
