import math
numero = 0
for random in range(0, 360, 6):
    nuevo = numero + random
    y = math.sin(math.radians(nuevo))
    print (y)