Lista = []


T = int(input("Digite o tamanho da lista: "))

for cont in range(T):
    números = int(input(f"Digite um número{cont+1}: "))
    Lista.append(números)
    
print("Números da lista menores que 5:")
for números in Lista:
    if números < 5:
        print(números)
    