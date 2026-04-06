print("Verificação de inteiros e soma")

numeros = []
num_int = []
for i in range (10,0,-1):
    user_add = float(input(f"Digite o {i}° número da verificação: "))
    numeros.append(user_add)
for i in numeros:
    if i % 1 == 0:
        num_int.append(int(i))

print(f"os Números digitados foram {numeros}.")
print(f"Entre esses os inteiros digitados foram {num_int}.")
print(f"A soma dos inteiros é {sum(num_int)}.")