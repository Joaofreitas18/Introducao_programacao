#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

inicio = 0
fim = 50

while inicio <= fim:
    inicio += 1
    if inicio % 2 != 0:
        print(inicio)
