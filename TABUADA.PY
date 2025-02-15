#DEFINIR A VARIAVEL DA TABUADA.
#DEFINIR UMA VARIAVEL DE CONTADOR - VARIAVEL DE 1 A 10
#CRIAR UM LOOP.
#MULTIPLICAR AS VARIAVEIS E GUARDAR O RESULTADO.
#MOSTRAR O RESULTADO.
#SOMAR 1 AO VALOR DO CONTADOR.

tabuada = 1
contador = 0
resultado  = 0
while resultado <20:
    resultado = tabuada * contador
    print (tabuada, "x", contador, "=", resultado)
    contador  += 1
  
tabuada = 1
contador = 0
resultado  = 0
while tabuada <=10:
    resultado = tabuada * contador
    print (tabuada, "x", contador, "=", resultado)
    contador  += 1
    if contador == 11:
        tabuada += 1
        contador = 1
