nota = float(input('Digite uma nota entre 0 e 10: '))

if nota > 5:
    print('Você foi aprovado! ')

elif nota > 3:
    print('Você está de Recuperação! ')

elif nota > 10 and nota < 0 :
    print('Digite um número válido! ')
    
else:
    print('Você Reprovou! ')