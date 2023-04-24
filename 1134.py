alcool = 0
gasolina = 0
diesel = 0
flag = 4

entrada = int(input())

while entrada != flag:
    if entrada == 1:
        alcool += 1
    elif entrada == 2:
        gasolina += 1
    elif entrada == 3:
        diesel += 1

    entrada = int(input())

print('MUITO OBRIGADO')
print('Alcool: {}'.format(alcool))
print('Gasolina: {}'.format(gasolina))
print('Diesel: {}'.format(diesel))
