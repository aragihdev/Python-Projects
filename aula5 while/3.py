print("Acumulador de valores personalizado")

pos = 0
neg = 0
zero = 0
while True:
    num = float(input("Digite um número qualquer:"))
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    elif num == 0:
        zero += 1
    else:
        break
    print(f"{pos} foram positivos, {neg} foram negativos e {zero} foram iguais a 0.")
print("Você deve digitar um número, sem letras ou caracteres especiais.")