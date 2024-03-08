pv = float(input("Qual o valor inicial do investimento? "))
n = int(input("Quantos meses o dinheiro sera aplicado? "))
i = float(input("Qual a rentabilidade mensal? "))

conversao = i * 0.01 

fv = pv * (conversao + 1) ** n




print("O valor do montante final é ","%.2F"%fv)