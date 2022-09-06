# Armazenar um número entre 0 e 255. Por exemplo, o número 120.
numero = 120

# subtraia o numero por 128, se o resultado da operação for 0 ou superior então o primeiro bit é 1
if (numero - 128) >= 0:
    bit1 = "1"
    numero = numero - 128
else:
    bit1 = "0"

# subtraia o numero por 64, se o resultado da operação for 0 ou superior então o segundo bit é 1
if (numero - 64) >= 0:
    bit2 = "1"
    numero = numero - 64
else:
    bit2 = "0"

# subtraia o numero por 32, se o resultado da operação for 0 ou superior então o terceiro bit é 1
if (numero - 32) >= 0:
    bit3 = "1"
    numero = numero - 32
else:
    bit3 = "0"


# subtraia o numero por 16, se o resultado da operação for 0 ou superior então o quarto bit é 1
if (numero - 16) >= 0:
    bit4 = "1"
    numero = numero - 16
else:
    bit4 = "0"


# subtraia o numero por 8, se o resultado da operação for 0 ou superior então o quinto bit é 1
if (numero - 8) >= 0:
    bit5 = "1"
    numero = numero - 8
else:
    bit5 = "0"


# subtraia o numero por 4, se o resultado da operação for 0 ou superior então o sexto bit é 1
if (numero - 4) >= 0:
    bit6 = "1"
    numero = numero - 4
else:
    bit6 = "0"


# subtraia o numero por 2, se o resultado da operação for 0 ou superior então o setimo bit é 1
if (numero - 2) >= 0:
    bit7 = "1"
    numero = numero - 2
else:
    bit7 = "0"


# subtraia o numero por 1, se o resultado da operação for 0 ou superior então o oitavo bit é 1
if (numero - 1) >= 0:
    bit8 = "1"
    numero = numero - 1
else:
    bit8 = "0"

print(numero)
print(bit1 + bit2 + bit3 + bit4 + bit5 + bit6 + bit7 + bit8)