#frase = input("Digite uma frase ou palavra: ")
#letra = input("Digite uma frase ou palavra: ")

#contagem = frase.count(letra)
#print(f"A letra {letra} aparece {contagem} vezes na palavra {frase}")


frase = input("Digite uma frase ou palavra: ")
letra = input("Digite uma letra: ")

contador = 0
for i in frase:
    if i is letra:
        contador = contador + 1

print(f"A letra {letra} aparece {contador} vezes na palavra {frase}")
        
