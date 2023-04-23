entrada = input()

a, b, c = entrada.split()

a = round(float(a), 2)
b = round(float(b), 2)
c = round(float(c), 2)

pi = 3.14159
area_triangulo = a * c / 2
area_circulo = pi * (c**2)
area_trapezio = (a+b) * c / 2
area_quadrado = b**2
area_retangulo = a * b


print("TRIANGULO: {:.3f}".format(area_triangulo))
print("CIRCULO: {:.3f}".format(area_circulo))
print("TRAPEZIO: {:.3f}".format(area_trapezio))
print("QUADRADO: {:.3f}".format(area_quadrado))
print("RETANGULO: {:.3f}".format(area_retangulo))
