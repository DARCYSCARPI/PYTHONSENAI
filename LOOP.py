limite = 101
contador = 0
sair = False # True ou False

while sair == False: 
    print("contando.: ", contador)
    contador = contador + 1
    resposta = input ("deseja parar o contador? S/N: ")

    if resposta == "N":
        sair = False
    else:
        sair = True    
        while contador <= limite:
            print("contando.: ", contador)
    contador = contador + 1
    
while contador >= limite:
    print("contando.: ", contador)
    contador += 115

while contador <= limite:
    print("contando.: ", contador)
    contador = contador + 1

print("FINAL DA CONTAGEM")    
    