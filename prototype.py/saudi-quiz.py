print('hi, welcome to the "ARE YOU A TRUE SAUDI" game by Diane, so first question is simple')
answer = input("ARE YOU SAUDI? (yes/no): ").lower() == "yes"

if answer == True:
    print("Hala wallah and welcome to the game!")
elif answer == False:
    print("This game is only for saudis!")
    exit()

score = 0
questions = [
        ("Whats the capital city of saudia? ", "riyadh"),
        ("Whats our country code? ", "966"),
        ("Whats our national dish? ", "kabsa"),
        ("Whats our flag colors? ", "green and white"),
        ("Whats our the foundation year of saudia? (1932/1945): ", "1932"),
        ("Who is the founder of saudia? ", "king abdulaziz"),
        ("When is our national day? ", "23/9")
        
    ]

for question, correct_answer in questions:
        user_answer = input(question).lower().strip()
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        if user_answer != correct_answer.lower().strip():
            print("Incorrect!")
            
print("Your score is: ", score, "/", len(questions))