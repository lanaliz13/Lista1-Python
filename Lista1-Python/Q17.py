Lista = []
soma_impares = 0

T = int(input("Digite o tamanho da lista: "))


for cont in range(T):
    número = int(input(f"Digite um número {cont+1}: "))
    Lista.append(número)
    

print("Números ímpares da lista:")
for número in Lista:
    if número % 2 != 0:
        print(número)
        soma_impares += número


print(f"A soma dos números ímpares da lista é {soma_impares}")
 