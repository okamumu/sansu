import random

def tashisan1(m, seed):
    random.seed(seed)
    questions_set = set()
    while len(questions_set) < m:
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        questions_set.add((num1, num2))
    questions_list = [f"{q[0]} + {q[1]} = ?" for q in questions_set]
    return questions_list

def hikisan1(m, seed):
    random.seed(seed)
    questions_set = set()
    while len(questions_set) < m:
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        (num1, num2) = (num1, num2) if num1 <= num2 else (num2, num1)
        questions_set.add((num1 + num2, num2))
    questions_list = [f"{q[0]} - {q[1]} = ?" for q in questions_set]
    return questions_list

def kakesan1(m, seed):
    random.seed(seed)
    questions_set = set()
    while len(questions_set) < m:
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        question = (num1, num2)
        questions_set.add(question)
    questions_list = [f"{q[0]} × {q[1]} = ?" for q in questions_set]
    return questions_list

def warisan1(m, seed):
    random.seed(seed)
    division_questions_set = set()
    while len(division_questions_set) < m:
        num1 = random.randint(1, 9)  # Dividend
        num2 = random.randint(1, 9)  # Divisor
        if (num1 * num2) <= 81 and num1 != 1:
            question = (num1 * num2, num1)
            division_questions_set.add(question)
    division_questions_list = [f"{q[0]} ÷ {q[1]} = ?" for q in division_questions_set]
    return division_questions_list
