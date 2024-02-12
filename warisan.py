import random

def gen_warisan():
    # Generate 10 unique division questions from the 9x9 multiplication table that result in whole numbers
    division_questions_set = set()

    while len(division_questions_set) < 10:
        num1 = random.randint(1, 9)  # Dividend
        num2 = random.randint(1, 9)  # Divisor
        if (num1 * num2) <= 81 and num1 != 1:  # Ensure the result is within the 9x9 table and not trivial
            question = (num1 * num2, num1)  # Format as (dividend, divisor)
            division_questions_set.add(question)

    # Format questions for display
    division_questions_list = [f"{q[0]} ÷ {q[1]}" for q in division_questions_set]

    return division_questions_list
