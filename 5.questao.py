import os
os.system("clear")

# Faça um programa que leia um código de operação (+,-,* ou /), e também dois valores inteiros A e B. 
# O programa deve calcular o resultado da operação escolhida aplicado a A e B.
# Por exemplo, se a operação escolhida foi * e A = 1 e B = 3,
# o programa deve fornecer como resultado o valor de 1*3, que é 3.

a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
operacao = (input("""
+ - Adição                       
- - Subtração
* - Multiplicação
/ - Divisão                      
                       
Digite uma operação de sua escolha: """))

match operacao:
    case "+" | "Adição":
        resultado = a + b
        print(f"O resultado da soma entre (A) e (B)) é: {resultado}")
    case "-" | "Subtração":
        resultado = a - b
        print(f"O resultado da subtração entre (A) e (B)) é: {resultado}")
    case "*" | "Multiplicação":
        resultado = a * b
        print(f"O resultado da multiplicação entre (A) e (B)) é: {resultado}")   
    case "/" | "Divisão":
        resultado = a / b
        print(f"O resultado da divisão entre (A) e (B)) é: {resultado}")
    case _:
        print("Opção Inválida.")














