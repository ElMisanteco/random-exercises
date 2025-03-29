import schemdraw
import schemdraw.elements as elm

d = schemdraw.Drawing()

# Alimentación con batería de 3.3V
d.add(elm.Battery().label('3.3V'))

# Resistencia de 220Ω para limitar la corriente y proteger el LED
d.add(elm.Resistor().right().label('220Ω'))

# LED con su símbolo característico
d.add(elm.LED().right().label('LED'))

# Línea bajando hacia la conexión a tierra
d.add(elm.Line().down())

# Línea de retorno hacia la batería
d.add(elm.Line().left().tox(0))

# Conexión a tierra
d.add(elm.Ground())

d.draw()
