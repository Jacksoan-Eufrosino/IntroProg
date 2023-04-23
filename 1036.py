entrada = input()
numeros = entrada.split()
A= float(numeros[0])
B =float(numeros[1])
C =float(numeros[2])


delta = (B**2) - (4*A*C)

if delta < 0:
    print("Impossivel calcular")
elif delta == 0:
    x = (-B) / 2*A
    print(x)
else:
    x1 = (-B + delta**(1/2)) / (2*A)
    x2 = (-B - delta**(1/2)) / (2*A)
    print("R1 = {:.4f}".format(x1))
    print("R2 = {:.4f}".format(x2))
