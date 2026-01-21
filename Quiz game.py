print("WELCOME TO THE QUIZ GAME!")
print("-------------------------")

questions = [
    {
        "question": "What is the capital of nigeria",
        "options": ["A) Paris", "B) Abuja", "C) Lokoja", "D) Calabar"],
        "answer": "B" 
    },
    {
        "question": "Which language is used for web styling?",
        "options": ["A) Python", "B) CSS", "C) SQL", "D) Java"],
        "answer": "B"
    },
    {
        "question": "Who created Python?",
        "options": ["A) Elon Musk", "B) Mark Zuckerberg", "C) Guido van Rossum", "D) Jeff Bezos"],
        "answer": "C"
    }
]

score = 0

for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)

    user_input = (input("Choose the correct options (A/B/C/D): ")).upper()
    if user_input == q["answer"]:
       print("Correct!")
       score += 1 
    else:
       print(f"Wrong! correct answer is {q["answer"]}")


print("-------------------------------------------")
print(f"You scored {score} out of {len(questions)}")
print("-------------------------------------------")       


