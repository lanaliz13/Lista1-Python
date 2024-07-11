palavras = input("Digite as palavras que desejar: ")


lp = palavras.split()


palavraMaior = ""

for palavra in lp:
    if len(palavra) > len(palavraMaior):
        palavraMaior = palavra


print(f"A palavra mais longa é: {palavraMaior}")