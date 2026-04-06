print("Lista ao quadrado")
numeros = []
numquadrado = []
for i in range (5,0,-1):
    num = input(f"Digite o {i}° número da lista:")
    numeros.append(num)
    numeros.sort()
print(f"Originais: {numeros}.")
for i in numeros:
    numquadrado.append(float(i) * float(i))
print(f"Ao quadrado: {numquadrado}.")