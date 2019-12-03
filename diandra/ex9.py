#Descobrir se o aluno passou ou não na faculdade

alunos = [
    {
        'nome': 'Ana Beatriz',
        'notas': [7, 6.5, 9, 4.5]
    },
    {
        'nome': 'Eric',
        'notas': [6.5, 6, 5, 7]
    },
    {
        'nome': 'Camila',
        'notas': [7, 8, 9, 10]
    },
    {
        'nome': 'Lucas',
        'notas': [8, 5.5, 6, 7]
    },
    {
        'nome': 'Nicolas',
        'notas': [9, 8, 10, 10]
    },
    {
        'nome': 'Natalia',
        'notas': [5.5, 4.5, 6, 4]
    },
    {
        'nome': 'Renan',
        'notas': [4, 7, 5.5, 6.5]
    }
]

valor = (alunos[0]['notas'])
print(valor)

media = 6

for aluno in alunos:
    soma_nota = 0 
    for nota in aluno['notas']:
        soma_nota += nota

    
    aluno_media = soma_nota / len(aluno['notas'])
    
    if aluno_media >= media:
        print(f'o aluno {aluno["nome"]} foi aprovado com a média de {aluno_media}')
    elif aluno_media < media:
        print(f'o aluno {aluno["nome"]} não passou com a média de {aluno_media}')
