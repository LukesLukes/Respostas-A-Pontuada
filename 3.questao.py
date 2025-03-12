import os
os.system("clear")

# Faça um algoritmo que leia dois valores inteiros A e B se os valores forem iguais deverá se somar os dois,
# caso contrário multiplique A por B.
# Ao final de qualquer um dos cálculos deve-se atribuir o resultado para uma variável C e mostrar seu conteúdo na tela.

a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float

if a == b:
    c = a + b
    print(f"(A) é igual a (B); e o resultado de (C), sendo adição, é: {c}")
else:
    c = a * b
    print(f"(A) não é igual a (B); e o resultado de (C), sendo multiplicação, é: {c}")    



























