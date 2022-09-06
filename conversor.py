# Armazenar um número entre 0 e 255. Por exemplo, o número 120.
numero = 120

# subtraia o numero por 128, se o resultado da operação for 0 ou superior então o primeiro bit é 1
if (numero - 128) >= 0:
    bit1 = 1
    numero = numero - 128
else:
    bit1 = 0

    
    print(numero)
    print(bit1)
