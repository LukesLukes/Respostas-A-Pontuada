import os
os.system("clear")

# Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa.
# Caso sexo seja “F” e estado civil seja “CASADA”, solicitar o tempo de casada (anos). Por fim, mostre os dados do usuário.

nome = str(input("Digite o seu nome: "))
sexo = str(input("Digite o seu sexo: "))
estado_civil = str(input("Digite o seu estado civil: "))

match estado_civil:
    case "Solteiro" | "Solteira":
        print("\nExibindo dados...")
        print(f"Nome: {nome}")
        print(f"Sexo: {sexo}")
        print(f"Estado Civil: {estado_civil}")
    
    case "Casado" | "Casada":
        tempo_de_casado = input("Digite o seu tempo de casado em anos: ")   

        print("\nExibindo dados...")
        print(f"Nome: {nome}")
        print(f"Sexo: {sexo}")
        print(f"Estado Civil: {estado_civil}")
        print(f"Tempo de Casado: {tempo_de_casado}")
    case _:
        print("Inválido.")    
        
   

   
   
    















