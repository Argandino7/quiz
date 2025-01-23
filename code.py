score = 0
score += 1
question = "What is the capital of Argentina?"
print(question)
user_answer = input("Your answer: ")
if user_answer.lower() == "buenos aires":
    print( "Correct!")
else:
    print("Oops! The correct answer is Buenos Aires.")