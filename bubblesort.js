numeros = [2, 90, 43, 21, 5, 10]

let menor
let maior

for(i=0;i<numeros.length-1; i++){
  for(j=0;j<numeros.length-1; j++){
    if(numeros[j] > numeros[j+1]){
      menor = numeros[j+1]
      maior = numeros[j]
      numeros[j] = menor
      numeros[j+1] = maior
    }
    console.log(numeros)
  }
}

