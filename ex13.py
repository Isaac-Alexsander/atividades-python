pedido = int(input("Quantos livros deseja comprar? "))

livro = 24.95 

desc = livro - (livro * 0.35)

transporte = 3 

if pedido == 1:
 compra = desc + transporte 
 print( "O valor final é ","%.2f"%compra)
elif pedido > 1:
 pedido2 = pedido * 0.75
 compra = desc + transporte + pedido2 + pedido
 print("o valor final é ", "%.2f"%compra)

else:
 print("Voce nao comprou nenhum livro ")
