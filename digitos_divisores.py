numero = int(input("Número: "))

divisores = 0
for digito in str(numero):
    digito = int(digito)
    if digito and numero % digito == 0:
        divisores += 1
print("Divisores:", divisores)
