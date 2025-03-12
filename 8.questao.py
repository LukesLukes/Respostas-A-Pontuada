import os
os.system("clear || cls")

# Em uma loja de CD´s existem apenas quatro tipos de preços que estão associados a cores. 
# Assim os CD´s que ficam na loja não são marcados por preços e sim por cores.
# Desenvolva o algoritmo que a partir da entrada da cor o software mostre o preço. 
# A loja está atualmente com a seguinte tabela de preços.  

cd = (input("""
Verde
Azul
Amarelo
Vermelho

Digite a cor de um CD da sua escolha, e será mostrado valor do CD escolhido:    """))

match cd:
    case "Verde" | "VERDE":
        print("Valor: R$ 10.00")
    case "Azul" | "AZUL":
        print("Valor: R$ 20.00")
    case "Amarelo" | "AMARELO":
        print("Valor: R$ 30.00")
    case "Vermelho" | "VERMELHO":
        print("Valor: R$ 40.00")
    case _:
        print("Opção Inválida.")

