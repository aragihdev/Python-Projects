print("Verificação de número 3")

numeros = []
num_tres = []
int_check = []
total_de_algarismos = 0
for i in range (5,0,-1):
    user_add = input(f"Digite o {i}° número da verificação: ")
    numeros.append(user_add)
for num_leitor in numeros:
    if "3" in num_leitor:
        int_check.append(num_leitor)
for i in int_check:
    num_tres.append(int(i))
for i in int_check:
    total_de_algarismos += i.count("3")
print(f"Os números digitados foram {numeros}.")
print(f"Entre esses os que possuem o algarismo 3 são {num_tres}, totalizando {total_de_algarismos}.")