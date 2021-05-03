#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a 
#porcentagem do aumento. Exiba o valor do aumento e do novo salário.
n = float(input("Salario: "))
p = int(input("Porcentagem de aumento: "))
soma = n + ( n * p / 100)
print("Seu salario antigo {} seu salario com novo ajuste de {}% R${} ".format(n,p,soma))