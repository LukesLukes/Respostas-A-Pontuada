import os
os.system("clear")

# Uma fruteira está vendendo frutas com a seguinte tabela de preços: 
# Se o cliente comprar a partir de 10 Kg em frutas ou o valor total da compra ultrapassar R$ 15,00,
# receberá ainda um desconto de 10% sobre este total.
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos
# e a quantidade (em Kg) de maçãs adquiridas e escreva o valor a ser pago pelo cliente.

quantitade_morango = int(input("Digite a quantidade de morangos, em kg, que deseja comprar: "))
quantitade_maca = int(input("Digite a quantidade de maçãs, em kg, que deseja comprar: "))
valor_total = float
valor_a_ser_pago = float

quantidade_frutas = quantitade_morango + quantitade_maca

if quantidade_frutas > 10 or valor_total > 15.00:
    desconto = valor_total * 0.10
    valor_a_ser_pago = valor_total - desconto
    
    print("\nExibindo os resultados...")
    print(f"Quantidade de morangos adquiridos, em kg: {quantitade_morango}")
    print(f"Quantidade de maçãs adquiridas, em kg: {quantitade_maca}")
    print(f"Valor total: R$ {valor_total}")
    print(f"Valor desconto: R$ {desconto}")
    print(f"Valor a pagar: R$ {valor_a_ser_pago}")
else:
    print("\nExibindo os resultados...")
    print(f"Quantidade de morangos adquiridos, em kg: {quantitade_morango}")
    print(f"Quantidade de maçãs adquiridas, em kg: {quantitade_maca}")
    print(f"Valor a pagar: R$ {valor_a_ser_pago}")





































