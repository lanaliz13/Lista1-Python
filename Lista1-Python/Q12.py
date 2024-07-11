Lista = []


T = int(input("Digite o tamanho da lista: "))

for cont in range(T):
    números = int(input(f"Digite um número{cont+1}: "))
    Lista.append(números)
    
print("Números ímpares da lista:")
for números in Lista:
    if números % 2 != 0:
        print(números)
    