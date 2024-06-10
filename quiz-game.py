

questions = [
    {
        "prompt": "What is the capital of Tokyo?",
        "options": ["A. Osaka", "B. Kyoto", "C. Tokyo", "D. Okinawa"],
        "answer": "C"
    },
    {
        "prompt": "Which language is primarily spoken in Brazil?",
        "options": ["A. Spanish", "B. Portuguese", "C. English", "D. French"],
        "answer": "B"
    },
    {
        "prompt": "Who wrote to 'To Kill a Mockingbird?",
        "options": ["A. Harper Lee", "B. Mark Twain", "C. J.K Rowling", "D. Hemingway"],
        "answer": "A"
    }
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        if answer  == question["answer"]:
            print("Correct, hooray!!\n")
            score += 1
        else:
            print("Wrong, LOSERRRRR! The correct answer was", question["answer"], "\n")

    print(f"Your score is: {score} out of {len(questions)} questions correct.")

run_quiz(questions)