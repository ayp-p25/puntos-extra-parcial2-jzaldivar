# Entradas
numero = int(input("Número: "))

# Proceso
divisores = 0
for digito in str(numero):
    digito = int(digito)
    if digito != 0 and numero % digito == 0:
        divisores += 1

# Salidas
print("Divisores:", divisores)
