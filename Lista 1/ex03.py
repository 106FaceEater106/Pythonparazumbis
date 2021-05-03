#screva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule 
#o total em segundos.
d = int(input("Dia: "))
h = int(input("Hora: "))
m = int(input("Minutos: "))
s = int(input("Segundos: "))
dd = 86400 * d
hh = 3600 * h
mm = 60 * m
soma = dd + hh + mm + s
print(soma)