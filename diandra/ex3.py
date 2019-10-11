#venda de sabão em pó em multinivel, a cada venda a pessoa superior ganha 5% em cima 
# do valor total da pessoa subordinada. 


boss = {
    "nome": "Bruno",
    "salario": ""}

equipe1= {
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
}
        
equipe2 = {
        "nome": "Di",
        "vendas": 450,
        "subordinados":
            {
                "nome": "Maga",
                "vendas": 200,            
            }
    }

equipe3 = {
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

ganho = 0.05

soma1 = equipe1.get('vendas') * ganho
print(soma1)



  

for i in equipe1:
    print(i, ":", equipe1[i])
    

for i in equipe2:
    print(i, ":", equipe2[i])


for i in equipe3:
    print(i, ":", equipe3[i])


