def calculate_weights(answers, questions):
    accumulated_weights = {"coach": 0, "startupeiro": 0, "gourmet": 0, "blogueiro": 0}

    for current_question in range(len(questions)):
        question = questions[current_question]
        answer = answers[current_question]
        
        selected_weights = select_weights_for_answer(question, answer)
        
        for profession in selected_weights:
            accumulated_weights[profession] += selected_weights[profession]
    
    return accumulated_weights

def select_weights_for_answer(question, answer):
    for alternative in question['alternatives']:
        if alternative['option'] == answer:
            return alternative['weights']

def get_selected_profession(weights):
    highest_weight = 0
    selected_profession = None
    
    for profession in weights:
        weight = weights[profession]
        if weight > highest_weight:
            highest_weight = weight
            selected_profession = profession
    
    return selected_profession

def get_percentual(accumulated_weights):
    scores = {"coach": 0, "startupeiro": 0, "gourmet": 0, "blogueiro": 0}
    total = sum(accumulated_weights.values())
    for profession in accumulated_weights:
        score = accumulated_weights[profession]
        percent = round(score * 100 / total)
        scores[profession] = percent
    return scores        
