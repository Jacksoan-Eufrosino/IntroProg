x1y1 = input()
x2y2 = input()

x1, y1 = x1y1.split()
x2, y2 = x2y2.split()

x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

distancia = ((x2-x1)**2 + (y2-y1)**2)**(1/2)

print('{:.4f}'.format(distancia))
