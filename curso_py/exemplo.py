nomes = []
idade = []
resposta = "S"
while resposta == "S":
    nomes.append(input('Digite seu nome:'))
    idade.append(int(input('você tem quantos anos:')))
    resposta = input('Digite \"S\" para continuar:').upper()
    
for indice in range(0, len (nomes)):
    print('\nNome..: ', (indice + 1))
    print('nome......... :', nomes[indice])
    print('idade......... :', [indice])


    
    
    
