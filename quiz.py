import random

# Quiz questions and their corresponding answers
quiz_questions = {
    "What is the capital of France?": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
    "Which planet is known as the 'Red Planet'?": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
    "What is the largest mammal in the world?": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Lion"],
    "Who painted the Mona Lisa?": ["A. Leonardo da Vinci", "B. Vincent van Gogh", "C. Pablo Picasso", "D. Michelangelo"],
    "What is the chemical symbol for water?": ["A. H2O", "B. CO2", "C. O2", "D. NaCl"],
    "What is the largest planet in our solar system?": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
    "Which country is known as the 'Land of the Rising Sun'?": ["A. China", "B. Japan", "C. South Korea", "D. Thailand"],
    "What is the primary language spoken in Brazil?": ["A. Portuguese", "B. Spanish", "C. English", "D. French"],
    "Which scientist formulated the theory of relativity?": ["A. Isaac Newton", "B. Albert Einstein", "C. Galileo Galilei", "D. Nikola Tesla"],
    "What is the symbol for the element oxygen?": ["A. O", "B. Ox", "C. O2", "D. Oh"]
}

# Correct answers for each question
correct_answers = {
    "What is the capital of France?": "A",
    "Which planet is known as the 'Red Planet'?": "B",
    "What is the largest mammal in the world?": "B",
    "Who painted the Mona Lisa?": "A",
    "What is the chemical symbol for water?": "A",
    "What is the largest planet in our solar system?": "C",
    "Which country is known as the 'Land of the Rising Sun'?": "B",
    "What is the primary language spoken in Brazil?": "A",
    "Which scientist formulated the theory of relativity?": "B",
    "What is the symbol for the element oxygen?": "A"
}

def print_question(question, options):
    print(question)
    for option in options:
        print(option)

def get_user_choice():
    while True:
        choice = input("Enter the letter of your answer (A, B, C, or D): ").upper()
        if choice in ["A", "B", "C", "D"]:
            return choice
        print("Invalid input. Please enter a valid option (A, B, C, or D).")

def run_quiz():
    questions = list(quiz_questions.keys())
    random.shuffle(questions)
    score = 0

    for question in questions[:10]:  # Only ask the first 10 questions
        options = quiz_questions[question]
        print_question(question, options)
        user_choice = get_user_choice()

        if user_choice == correct_answers[question]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_answers[question]}.\n")

    print(f"You answered {score} out of 10 questions correctly.")

if __name__ == "__main__":
    print("Welcome to the Quiz Game!")
    print("Test your knowledge with these multiple-choice questions.")
    run_quiz()