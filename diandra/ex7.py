# Exercicio quiz Capricho

quizz = [
    {
        "question_text": "Na sua carreira, você prefere:",
        "alternatives": [
            {
                "option": "a",
                "option_text": "Ajudar as pessoas chegarem nos seus objetivos",
                "weights": {
                    "coach": 3, 
                    "startupeiro": 0, 
                    "gourmet": 1, 
                    "blogueiro": 0
                }
                
            },
            {
                "option": "b",
                "option_text": "Resolver problemas que ninguém resolve",
                "weights": {
                    "coach": 0, 
                    "startupeiro": 3,
                    "gourmet": 3,
                    "blogueiro": 0
                }
            },
            {
                "option": "c",
                "option_text": "Ser positivo todos os dias",
                "weights": {
                    "coach": 3, 
                    "startupeiro": 1,
                    "gourmet": 1, 
                    "blogueiro": 2
                }
            },
            {
                "option": "d",
                "option_text": "Ser reconhecido por todos",
                "weights": {
                    "coach": 0, 
                    "startupeiro": 2, 
                    "gourmet": 2,
                    "blogueiro": 3
                }
            },
        ]
    },

    {
        "question_text": "No seu dia a dia, como você age com as pessoas:",
        "alternatives": [
            {
                "option": "a",
                "option_text": "Você aconselha todo mundo",
                "weights": {
                    "coach": 3, 
                    "startupeiro": 0,
                    "gourmet": 0, 
                    "blogueiro": 2
                }
            },
            {
                "option": "b",
                "option_text": "Você é um bom ouvinte",
                "weights": {
                    "coach": 0, 
                    "startupeiro": 1,
                    "gourmet": 3, 
                    "blogueiro": 1
                }
            },
            {
                "option": "c",
                "option_text": "Você toma iniciativa",
                "weights": {
                    "coach": 1, 
                    "startupeiro": 3,
                    "gourmet": 2, 
                    "blogueiro": 1
                }
            },
            {
                "option": "d",
                "option_text": "Você analisas todas as opções",
                "weights": {
                    "coach": 0,
                    "startupeiro": 1,
                    "gourmet": 3, 
                    "blogueiro": 1
                }
            },
        ]
    },

    {
        "question_text": "Se você fosse um animal, você seria:",
        "alternatives": [
            {
                "option": "a",
                "option_text": "Um papagaio",
                "weights": {
                    "coach": 3, 
                    "startupeiro": 2, 
                    "gourmet": 0, 
                    "blogueiro": 2 
                }
            },
            {
                "option": "b",
                "option_text": "Um leão",
                "weights": {
                    "coach": 0,
                    "startupeiro": 3,
                    "gourmet": 2,
                    "blogueiro": 2
            }
            },
            {
                "option": "c",
                "option_text": "Uma formiga",
                "weights": {
                    "coach": 1,
                    "startupeiro": 2, 
                    "gourmet": 1, 
                    "blogueiro": 3
                }
            },
            {
                "option": "d",
                "option_text": "Um flamingo",
                "weights": {
                    "coach": 1, 
                    "startupeiro": 1,
                    "gourmet": 3, 
                    "blogueiro": 1
                }
            },
        ]
    }
]

people = [
    {   "name": "Eric",
        "answers": ['b', 'd', 'd']
     },

    {   "name": "Roger",
        "answers": ['a', 'b', 'a']
     },

    {   "name": "Nico",
        "answers": ['b', 'c', 'c']
     }
]

# teste = quizz[0]['alternatives'][0]['weights']
# print(teste.values())

#resolução di

# for person in people:
#     for answer in person['answers']:
#         print(f'O {person["name"]} respondeu {answer}')

# for question in quizz:
#     soma = 0
#     for alternative in question['alternatives']:
#         for choosen in alternative['weights'].values():
#             print(choosen)

# resolução

for person in people:
    accumulated_weights = {"coach": 0, "startupeiro": 0, "gourmet": 0, "blogueiro": 0}

    for current_question in range(len(quizz)):
        question = quizz[current_question]
        answer = person['answers'][current_question]
        selected_weights = None

        for alternative in question['alternatives']:
            if alternative['option'] == answer:
                selected_weights = alternative['weights']
        
        for profession in selected_weights:
            accumulated_weights[profession] += selected_weights[profession]
    
    highest_weight = 0
    selected_profession = None
    
    for profession in accumulated_weights:
        weight = accumulated_weights[profession]
        if weight > highest_weight:
            highest_weight = weight
            selected_profession = profession
    
    print(f'O {person["name"]} é um {selected_profession}')    
    print(accumulated_weights)
