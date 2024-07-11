Lista = []
soma = 0

T = int(input("Digite o tamanho da lista: "))


for cont in range(T):
    número = int(input(f"Digite um número {cont+1}: "))
    Lista.append(número)
    


for número in Lista:
        soma += número


print(f"A soma dos números pares da lista é {soma}")