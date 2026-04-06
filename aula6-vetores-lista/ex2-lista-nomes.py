print("Listador de nomes")
import time
nomes = []
for i in range (0,5):
    user_add = input(f"Digite o {i}° nome da lista:")
    nomes.append(user_add)
for i in nomes:
    print(f"{i}")
    time.sleep(.4)