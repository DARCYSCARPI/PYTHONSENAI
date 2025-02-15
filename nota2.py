nota = float(input('Digite uma nota: '))

if nota > 10:
    print('Você digitou um numero invalido')
else:
    print ("voce não digitou um numero maior que 10")    

if nota > 5:
    print('aprovada')
else:
    print ("voce não digitou um numero maior/igual 5")   

if nota >=3 :
    print('recuperação')  

if nota < 0:
    print('Você digitou um numero invalido')
else:
    print('voce não digitou um numero menor que 0 - e está reprovada')
