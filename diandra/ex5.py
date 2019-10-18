# trabalhar com busca binária, e encontrar o número selecionado dentro do vetor abaixo:
# resolvido

numeros = [2, 7, 9, 10, 31, 50, 140, 328, 1024]

numero_busca = 328
encontrei_numero = False

while not encontrei_numero:
    metade_vetor = (len(numeros) // 2) - 1

    print(f'metade_vetor: {metade_vetor}')

    numero_metade_vetor = numeros[metade_vetor]

    print(f'numero_metade_vetor: {numero_metade_vetor}')

    if numero_metade_vetor == numero_busca:
        print("numero encontrado")
        encontrei_numero = True
    elif numero_busca > numero_metade_vetor:
        print('numero_busca é maior que numero_metade_vetor')
        numeros = numeros[metade_vetor + 1:]    
    else:
        print('numero_busca é menor que numero_metade_vetor')
        numeros = numeros[:metade_vetor]

    if not encontrei_numero:
        print('Terminei uma passada. O novo vetor é: ')
        print(numeros)
        