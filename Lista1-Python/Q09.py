Lista = []


T = int(input("Digite o tamanho da lista: "))

for cont in range(T):
    números = int(input(f"Digite um número{cont+1}: "))
    Lista.append(números)


MN = Lista[0] 


for números in Lista:
    if números < MN:
        MN = números

print(f"O menor número na lista é: {MN}")