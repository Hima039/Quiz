
quiz = [
    {
        "question":"1. Who developed Python Programming Language?",
        "options" : ["A.Guido van Rossum","B.Nyx Violeta","C.Eren","D.Luxme"],
        "answer":"A"
    },
    {
        "question":"2. Which of the following character is used to give single-line comments in Python?",
        "options": ["A.#","B.","C.","D."],
        "answer":"A"
    },
    {
        "question": "3. What does pip stand for in python?",
        "options": ["A.Preferred Installer Program","B.Pip Installs Packages","C.Pipe Install Program","D.None of the above"],
        "answer": "B"
    },
    {
        "question": "4. Which of the following functions is a built-in function in python?",
        "options": ["A.sqrt()","B.loop()","C.print()","D.math()"],
        "answer": "C"
    },
    {
        "question": "5. What arithmetic operators cannot be used with strings in Python?",
        "options": ["A.+","B.*","C.-","D.All the above"],
        "answer": "C"
    }
]

def run_quiz(quiz):
    score = 0
    for question in quiz:
        print(question["question"])
        for option in question["options"]:
            print(option)
        answer = input("write your answer: ").upper()
        if answer == question["answer"]:
            print("Correct answer!\n")
            score += 1
        else:
            print(f"Wrong answer, the correct answer is {question['answer']}\n")
    print(f"Your score is {score} out of {len(quiz)}")

run_quiz(quiz)      
