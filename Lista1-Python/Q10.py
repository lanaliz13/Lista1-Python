Lista = []
soma = 0


t = int(input("Digite o tamanho da lista: "))

for cont in range(t):
    números = int(input(f"Digite um número{cont+1}: "))
    Lista.append(números)

for numeros in Lista:
    soma += números
    media = soma/t


print(f"A média dos números digitados é: {media}")