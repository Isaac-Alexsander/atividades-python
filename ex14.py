R = float(input("Qual o tamanho em CM da circuferencia maior ? "))
r = float(input("Qual o tamanho da menor circuferencia em CM ? "))

pi = 3.14

Acoroa = pi * R ** 2 - pi * r ** 2 

print ("A area da coroa é","%.2f"%Acoroa,"cm")