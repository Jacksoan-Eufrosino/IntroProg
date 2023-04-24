h_inicio, h_fim = input().split()
h_inicio, h_fim = int(h_inicio), int(h_fim)

if h_inicio < h_fim:
    print('O JOGO DUROU {} HORA(S)'.format(h_fim - h_inicio))
elif h_inicio >= h_fim:
    print('O JOGO DUROU {} HORA(S)'.format(24 - h_inicio + h_fim))
