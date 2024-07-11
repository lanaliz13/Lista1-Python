Lista_palavras = []

t = int(input("Quantidade de elementos da lista: "))

for cont in range(t):
    Palavra = input(f"Digite uma palavra {cont+1}: ")
    Lista_palavras.append(Palavra)
    
print("Palavras da lista que iniciam com a letra 'A':")
for Palavra in Lista_palavras:
    if Palavra[0] == "a" or Palavra[0] == "A":
        print(Palavra)