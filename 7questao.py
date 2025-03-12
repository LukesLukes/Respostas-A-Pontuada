import os
os.system("clear")

# Faça um algoritmo para ler: a descrição do produto (nome), a quantidade adquirida e o preço unitário.
# Calcular e escrever o total (total = quantidade adquirida * preço unitário), 
# o desconto e o total a pagar (total a pagar = total - desconto), sabendo-se que: 
# - Se quantidade <= 5 o desconto será de 2% 
# - Se quantidade > 5 e quantidade <= 10 o desconto será de 3% 
# - Se quantidade > 10 o desconto será de 5%.

nome_do_produto = input("Digite o nome do produto: ")
quantidade_adquirida = float(input("Digite a quantidade adquirida: "))
preco_unitario = float(input("Digite o preço unitário do produto: "))

total = quantidade_adquirida * preco_unitario


if quantidade_adquirida <= 5:
   desconto = total * 0.02
   total_a_pagar = total - desconto
   print(f"Total a pagar: {total_a_pagar}")
elif quantidade_adquirida <= 10:
    desconto = total * 0.03
    total_a_pagar = total - desconto
    print(f"Total a pagar: {total_a_pagar}")
else:
    desconto = total * 0.05
    total_a_pagar = total - desconto
    print(f"Total a pagar: {total_a_pagar}")    
    