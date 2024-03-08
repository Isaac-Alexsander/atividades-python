preco = float(input("digite o valor do produto :"))
desc = float(input("digite o valor do desconto :"))

conver = desc * 0.01

resultado = preco * conver 

precodisc = preco - resultado

print ("O preço do produto original é ",preco,"valor do desconto : ",resultado,"e o valor final é ",precodisc,"R$")