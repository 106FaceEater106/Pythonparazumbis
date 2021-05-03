#Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a 
#quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante 
#perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o 
#total de dias.

c = int(input("Cigarros: "))
a = int(input("Anos: "))
total =  a * 365 * c
d = total / 144
print(f"Voce perdeu {d:.1f}dias")



