#Crie um algoritmo de bubble sort no vetor desordenado abaixo:
#numeros = [2, 90, 43, 21, 5, 10]


#versão python pra facilitar a vida
numeros = [2, 90, 43, 21, 5, 10]
print(sorted(numeros))

#versão sem a facilidade
numeros = [2, 90, 43, 21, 5, 10]


# for i in range(len(numeros)-1):
#     for j in range((len(numeros)-1) - i):
#         if numeros[j] > numeros[j+1]:
#             numeros[j], numeros[j+1] = numeros[j+1], numeros[j]
# print(numeros)


esta_ordenado = False
while not esta_ordenado:
    esta_ordenado = True
    for i in range(len(numeros)-1):
        if numeros[i] > numeros[i+1]:
            numeros[i], numeros[i+1] = numeros[i+1], numeros[i]
            esta_ordenado = False
print(numeros)



            
            
            
            
            