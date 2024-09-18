# List of questions and their corresponding answers
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Paris", "B) Rome", "C) Madrid", "D) Berlin"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["A) Charles Dickens", "B) J.K. Rowling", "C) William Shakespeare", "D) Mark Twain"],
        "answer": "C"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
        "answer": "D"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["A) Oxygen", "B) Gold", "C) Silver", "D) Iron"],
        "answer": "A"
    }
]

def run_quiz(questions):
    score = 0
    for i, question_data in enumerate(questions):
        print(f"\nQuestion {i+1}: {question_data['question']}")
        for option in question_data['options']:
            print(option)

        # User input for answer
        answer = input("Enter your answer (A, B, C, or D): ").upper()

        # Check if the answer is correct
        if answer == question_data['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question_data['answer']}.")

    # Display the final score
    print(f"\nQuiz finished! Your final score is {score} out of {len(questions)}.")

if __name__ == "__main__":
    run_quiz(quiz_questions)
