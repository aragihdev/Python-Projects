print("Verificador de paridade")

numeros = []
numpares = []
for i in range (10,0,-1):
    user_add = float(input(f"Digite o {i}° número da verificação: "))
    numeros.append(user_add)
for i in numeros:
    if i % 2 == 0:
        numpares.append(int(i))

print(f"Números digitados {numeros}.")
print(f"Números pares {numpares}.")