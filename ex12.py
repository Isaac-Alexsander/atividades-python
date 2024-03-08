vf = float(input("Qual o valor final desejado ? "))
nm = int(input("Quantos meses deseja aplicar? "))
i = float(input("Qual a rentabilidade em % ? "))
conversao = i * 0.01

pv = vf / ( 1 + conversao)** nm

print("O valor do investimento deve ser ""%.2f"%pv)