Lista = []


T = int(input("Digite o tamanho da lista: "))


for cont in range(T):
    número = int(input(f"Digite um número {cont+1}: "))
    Lista.append(número)

Lista.sort()


print("Lista ordenada em ordem crescente:")
for número in Lista:
    print(número, end=" ")


    
