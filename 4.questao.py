import os
os.system("clear")

# Uma fruteira está vendendo frutas com a seguinte tabela de preços: 
# Se o cliente comprar a partir de 10 Kg em frutas ou o valor total da compra ultrapassar R$ 15,00,
# receberá ainda um desconto de 10% sobre este total.
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos
# e a quantidade (em Kg) de maçãs adquiridas e escreva o valor a ser pago pelo cliente.

valor_kg = input("""
Tabela de Frutas
| Frutas \t Até 5kg \t\t Acima de 5kg
Morango \t R$ 2,50 POR Kg\t\t R$ 2,20 por Kg                  
Maçã \t\t R$ 1,80 POR Kg \t R$ 1,50 por Kg
Aperte ENTER para continuar:                  
                 """)





morangos = int(input("Digite quantos morangos, em kg, foram comprados: "))
macas = int(input("Digite quantas maçãs, em kg, foram compradas: "))

if morangos <= 5:
    valor_morango = morangos * 2.5
else:
    valor_morango = morangos * 2.2
    
if macas <= 5:
    valor_macas = macas * 1.8
else:
    valor_macas = macas * 1.5
    
valor = valor_macas + valor_morango

if (morangos + macas) >= 10 or valor > 15:
    desconto = valor * 0.1
    valor_a_ser_pago = valor - desconto
    print("\nExibindo dados...")
    print("Você recebeu um desconto!")
    print(f"Valor do Morango: {valor_morango:.2f}")
    print(f"Valor das Maçãs: {valor_macas:.2f}")
    print(f"Valor a ser pago: R$ {valor_a_ser_pago:.2f}")
else:    
    print("\nExibindo dados...")
    print(f"Valor do Morango: {valor_morango:.2f}")
    print(f"Valor das Maçãs: {valor_macas:.2f}")
    print(f"Valor a ser pago: R$ {valor_a_ser_pago:.2f}")
    
        