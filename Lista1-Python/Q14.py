Lista = []


T = int(input("Digite o tamanho da lista: "))

for cont in range(T):
    números = int(input(f"Digite um número{cont+1}: "))
    Lista.append(números)
    
print("Números da lista maiores que 10:")
for números in Lista:
    if números > 10:
        print(números)
    