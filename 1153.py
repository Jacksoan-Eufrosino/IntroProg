n = int(input())
resultado = 0
while (n > 1):
    n = n*(n-1)
    resultado += n
    n -= 1
print(resultado)
