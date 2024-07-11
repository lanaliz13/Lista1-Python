Lista = []

T = int(input("Digite o tamanho da lista: "))

for cont in range(T):
    número = int(input(f"Digite um número {cont+1}: "))
    Lista.append(número)

Lista_decrescente = sorted(Lista, reverse=True)

print("Lista de números em ordem decrescente:")
for número in Lista_decrescente:
    print(número)