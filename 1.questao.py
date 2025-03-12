import os
os.system("clear")

# Faça um algoritmo que leia os valores A, B, C 
# e imprima na tela se a soma de A + B é menor que C, caso contrário, imprima que a A + B é maior que C.

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

if a + b < c:
    print("A + B é menor que C")
else:
    print("A + B é maior que C")