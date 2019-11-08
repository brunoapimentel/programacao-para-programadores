from ex7_functions import calculate_weights, get_selected_profession, get_percentual
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
     },
    {   "name": "Bruno",
        "answers": ['a', 'a', 'c']
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
    accumulated_weights = calculate_weights(person['answers'], quizz)
    selected_profession = get_selected_profession(accumulated_weights)
    scores = get_percentual(accumulated_weights)
   
    print(f'O {person["name"]} é {scores[selected_profession]}% {selected_profession}!')    
    #print(accumulated_weights)
    #print(scores)
