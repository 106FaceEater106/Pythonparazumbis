#solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o 
#preço a pagar.
p = float(input("Produto: "))
d = int(input("Desconto: "))
s = (p * d / 100)
total = p - s
print("O produto R${} com desconto de {} = {} saira por {}".format(p,d,s,total))