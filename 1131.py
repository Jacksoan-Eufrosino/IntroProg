gremio_vit = 0
inter_vit = 0
empates = 0
qtd_jogos = 0

while True:
    entrada = input()
    inter, gremio = entrada.split()
    inter, gremio = int(inter), int(gremio)
    if gremio > inter:
        gremio_vit += 1
    elif inter > gremio:
        inter_vit += 1
    elif gremio == inter:
        empates += 1
    qtd_jogos += 1
    escolha = int(input('Novo grenal (1-sim 2-nao)'))
    if escolha == 1:
        continue
    elif escolha == 2:
        break

print('{} grenais'.format(qtd_jogos))
print('Inter: {}'.format(inter_vit))
print('Gremio: {}'.format(gremio_vit))
print('Empates: {}'.format(empates))

if gremio_vit > inter_vit:
    print('Gremio venceu mais')
elif gremio_vit < inter_vit:
    print('Inter venceu mais')
else:
    print('Nao houve vencedor')
