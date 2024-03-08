capacidadedocilindro = float(input("Qual a capacidade do cilindro em litros ? "))
tempogasto = float(input("Quantas horas esta vazando ? "))

vazaoporhora = (3.600 * capacidadedocilindro) / tempogasto

print ("A vazão do tubo é de ","%.2f"%vazaoporhora," litros por hora")