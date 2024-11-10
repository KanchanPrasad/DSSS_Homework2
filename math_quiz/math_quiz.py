import random

def Number_Generator(min_val, max_val):
    """
    Generates a random number between min_val and max_val.
    """
    return random.randint(min_val, max_val)

def Operator_Generator():
    """
    Chooses a random operator from '+', '-', '*'.
    """
    return random.choice(['+', '-', '*'])

def Problem_Solution_Generator(n1, n2, operator):
    """
    Generates a math problem and its correct answer based on the given numbers and operator.
    """
    problem = f"{n1} {operator} {n2}"
    if operator == '+':
        answer = n1 + n2
    elif operator == '-':
        answer = n1 - n2
    else:
        answer = n1 * n2
    return problem, answer

def math_quiz():
    score = 0
    total_questions = 5

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        n1 = Number_Generator(1, 10)
        n2 = Number_Generator(1, 5)
        operator = Operator_Generator()

        problem, correct_answer = Problem_Solution_Generator(n1, n2, operator)
        print(f"\nQuestion: {problem}")

        try:
            user_answer = int(input("Your answer: "))
            if user_answer == correct_answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {correct_answer}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
