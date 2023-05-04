tempo_gasto = int(input())
velocidade = int(input())

dist_percorrida = tempo_gasto * velocidade

gas_necessario = dist_percorrida / 12

print('{:.3f}'.format(gas_necessario))
