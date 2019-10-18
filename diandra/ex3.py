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
           "vendas": 100,},
       {
           "nome": "Camila",
           "vendas": 350,
       }
   ]
},
{
       "nome": "Di",
       "vendas": 450,
       "subordinados":
           {
               "nome": "Maga",
               "vendas": 200,
           }
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

valor = (equipes[0]['subordinados'][0]['vendas'])
print(valor)

valor1 = (equipes[0]['vendas']) * 1.05
valor2 = (equipes[1]['vendas']) * 1.05
valor3 = (equipes[2]['vendas']) * 1.05

print(valor1, valor2, valor3)


for i in equipes:
    for v in i.values():
        print(v)