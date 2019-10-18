let piramide = {
    nome: "Bruno",
    vendedoresSecundarios: [
        {
            nome: "Ana",
            valor: 300,
            vendedoresTerciarios: [
                {
                    nome: "Bia",
                    valor: 100
                },
                {
                    nome: "Camila",
                    valor: 350  
                }
            ]
        },
        {
            nome: "Diandra",
            valor: 450,
            vendedoresTerciarios: [
                {
                    nome: "Maga",
                    valor: 200
                },
                {
                    nome: "Fábio",
                    valor: 210
                }
            ]
        },
        {
            nome: "Nico",
            valor: 500,
            vendedoresTerciarios: [
                {
                    nome: "Lucas",
                    valor: 150
                },
                {
                    nome: "Vini",
                    valor: 100
                }
            ]
        }
    ]
}

let ana = ((piramide.vendedoresSecundarios[0].vendedoresTerciarios[0].valor + piramide.vendedoresSecundarios[0].vendedoresTerciarios[1].valor) / 100)*5 

let totalAna = (((piramide.vendedoresSecundarios[0].vendedoresTerciarios[0].valor + piramide.vendedoresSecundarios[0].vendedoresTerciarios[1].valor) / 100)*5) + piramide.vendedoresSecundarios[0].valor

let diandra = ((piramide.vendedoresSecundarios[1].vendedoresTerciarios[0].valor + piramide.vendedoresSecundarios[1].vendedoresTerciarios[1].valor)/100)*5 

let totalDiandra = (((piramide.vendedoresSecundarios[1].vendedoresTerciarios[0].valor + piramide.vendedoresSecundarios[1].vendedoresTerciarios[1].valor)/100)*5) + piramide.vendedoresSecundarios[1].valor  

let nico = ((piramide.vendedoresSecundarios[2].vendedoresTerciarios[0].valor + piramide.vendedoresSecundarios[2].vendedoresTerciarios[1].valor)/100)*5

let totalNico = (((piramide.vendedoresSecundarios[2].vendedoresTerciarios[0].valor + piramide.vendedoresSecundarios[2].vendedoresTerciarios[1].valor)/100)*5) + piramide.vendedoresSecundarios[2].valor

let bruno = ((totalAna + totalDiandra + totalNico)/100)*5

console.log(`A Ana recebeu comissão de R$ ${ana.toFixed(2)} e faturou no total R$ ${totalAna.toFixed(2)}`)
console.log(`A Diandra recebeu comissão de R$ ${diandra.toFixed(2)} e faturou no total R$ ${totalDiandra.toFixed(2)}`)
console.log(`O Nico recebeu comissão de R$ ${nico.toFixed(2)} e faturou no total R$ ${totalNico.toFixed(2)}`)

console.log(`O Bruno não vendeu nada e recebeu R$ ${bruno.toFixed(2)}`)

