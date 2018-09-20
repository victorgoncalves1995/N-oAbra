import math

x1 = int(input("valor de Px1: "))
y1 = int(input("valor de Py1: "))
x2 = int(input("valor de Qx2: "))
y2 = int(input("valor de Qy2: "))

d = math.sqrt( (x1-x2)**2 + (y1-y2)**2 )

print("Distância ente P e Q é: ", d)

