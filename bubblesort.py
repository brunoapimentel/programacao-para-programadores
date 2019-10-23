numeros = [2, 90, 43, 21, 5, 10]

for i in range (len(numeros)-1):
    for j in range(len(numeros)-1):
        if numeros[j] > numeros[j+1]:
            numeros[j], numeros[j+1] = numeros[j], numeros[j+1]
        print(numeros)






# numeros = [2, 90, 43, 21, 5, 10]

# let menor
# let maior

# for(i=0;i<numeros.length; i++){
#   for(j=0;j<numeros.length; j++){
#     if(numeros[j] > numeros[j+1]){
#       menor = numeros[j+1]
#       maior = numeros[j]
#       numeros[j] = menor
#       numeros[j+1] = maior
#     }
#   }
#   console.log(numeros)
# }

