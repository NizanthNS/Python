questions = ("How many elements are in the Periodic Table?: ",
             "Which animal lays the largest EGG?: ",
             "What is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in a Human Body?: ",
             "Which Planet in the Solar System is the Hottest?: ")

options = (("A. 112","B. 118","C. 119","D. 117"),
           ("A. Whale","B. Crocodile","C. Ostrich","D. Elephant"),
           ("A. Nitrogen","B. Oxygen","C. Carbon-Dioxide","D. Hydrogen"),
           ("A. 206","B. 207","C. 208","D. 209"),
           ("A. Mercury","B. Venus","C. Saturn","D. Mars"))

answers = ("B", "C", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter your guess (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("WRONG!")
        print(f"{answers[question_num]} is the correct answer!.")
    question_num += 1

print("-------------------------------------")
print("               RESULTS               ")
print("-------------------------------------")

print("Answers: ", end = " ")
for answer in answers:
    print(answer, end = " ")
print()

print("Guesses: ", end = " ")
for guess in guesses:
    print(guess, end = " ")
print()

score = (score / len(answers) * 100)
print(f"Your final score is: {score}%")
