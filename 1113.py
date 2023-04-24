while True:
    entrada = input()
    x, y = entrada.split()
    x , y = int(x), int(y)
    if x == y:
        break
    elif x < y:
        print('Crescente')
    elif x > y:
        print('Decrescente')
