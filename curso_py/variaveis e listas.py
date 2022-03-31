equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"
while resposta == "S":
    equipamentos.append(input('Equipamento :'))
    valores.append(float(input('valor: ')))
    seriais.append(int(input('numero serial: ')))
    departamentos.append(input('departamento:'))
    resposta = input('Digite \'S\' para continuar: ').upper()
busca = input('\nDigite qual equipe você esta procurando:')
for indice in range(0, len (equipamentos)):
    if busca == equipamentos[indice]:
        print('\nEquipamento.. : ', (indice + 1))
        print("Nome............. : ", equipamentos[indice])
        print('valor............. : ', valores[indice])
        print('serial............. : ', seriais[indice])
        print('departamento............. : ', departamentos[indice])
    
        
    