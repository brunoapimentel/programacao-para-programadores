#venda de sabão em pó em multinivel, a cada venda a pessoa superior ganha 5% em cima
# do valor total da pessoa subordinada.
ganho = 1.05
salarioBruno = []


equipes = [
    {
        "nome": "Ana",
        "vendas": 300,
        "subordinados": [
            {
                "nome": "Bia",
                "vendas": 100,
            },
            {
                "nome": "Camila",
                "vendas": 350,
            }
        ]
    },
    {
       "nome": "Di",
       "vendas": 450,
       "subordinados": [
           {
               "nome": "Maga",
               "vendas": 200,
           },
            {
               "nome": "Fabio",
               "vendas": 210,
           }
       ]
   },
    {
       "nome": "Nico",
       "vendas": 500,
       "subordinados": [
           {
               "nome": "Lucas",
               "vendas": 150,
               },
           {
               "nome": "Vini",
               "vendas": 100,
           }
       ]
   }
]

total_vendas = 0

def sales(subordinados, vendas):
    for vendedor in equipes:
        vendas_subordinados = 0
        for subordinado in vendedor['subordinados']:
            vendas_subordinados += subordinado['vendas']
    
    comissao_vendas = vendas_subordinados * 0.05
    total_vendas += comissao_vendas + vendedor['vendas']
    print(f'O vendedor {vendedor["nome"]} vendeu {vendedor["vendas"]} e recebeu de comissão {comissao_vendas}')

print(f'o Bruno não trabalhou e recebeu o valor de {total_vendas * 0.05}')