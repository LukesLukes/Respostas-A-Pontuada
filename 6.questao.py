import os
os.system("clear")

# Escreva um programa que leia do teclado as duas notas de um aluno, calcule e exiba a média aritmética das notas.
# O programa deve, adicionalmente, exibir uma mensagem de parabéns caso o aluno esteja aprovado (média superior ou igual a 6,0),
# média até 4,0, o aluno está em recuperação, caso a média seja inferior a 4,0 o aluno será reprovado.

nome_do_aluno = input("Digite o nome do aluno: ")
primeira_nota = float(input("Digite a primeira nota do aluno: "))
segunda_nota = float(input("Digite a segunda nota do aluno: "))

media = (primeira_nota + segunda_nota) / 2

if media >= 6:
   print("\nExibindo resultados...") 
   print(f"Média: {media}") 
   print("Parabens! Você foi aprovado.")
elif media >= 4:    
   print("\nExibindo resultados...") 
   print(f"Média: {media}")
   print("Você está na recuperação.")
else:
   print("\nExibindo resultados...") 
   print(f"Média: {media}") 
   print("Você foi reprovado.") 