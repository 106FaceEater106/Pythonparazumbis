# Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média 
#esperada para a viagem.

d = int(input("Distancia KM: "))
v = int(input("Velocidade: "))
soma =  d / v
print("Sua viagem vai durar em média {}horas".format(soma))