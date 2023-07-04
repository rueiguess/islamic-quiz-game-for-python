# updated version of my islamic quiz game :) reduced from 60 lines ahhh
# using arrays to randomize questions and provides better spacing in the code hehe

import random

print("Welcome to my quiz game")

playing = input("Do you want to play? ")

if playing.lower() == 'yes':
    print("Great, let's play!")
else:
    exit()

score = 0

# Define an array or list of question-answer tuples
quiz_questions = [
    ("How many surahs are in the Quran?", "114"),
    ("How many juz are in the Quran?", "30"),
    ("What month comes before Ramadan?", "Shaban"),
    ("What is the name of our Beloved Prophet?", "Muhammad")
]

# Randomize the array of questions and answers
random.shuffle(quiz_questions)

tries = 3

for question, answer in quiz_questions:
    for _ in range(tries):
        print()
        user_answer = input(question + "\n").lower()

        if user_answer == answer.lower():
            print("Allahumma Barik, good job!")
            score += 1
            break
        else:
            print("Are you sure?")
            print("Try again, InshaAllah")

# Display the final score
print("Quiz finished!")
print("Your score:", score)
print("Allahumma Barik, you got", score, "points! May Allah increase you in knowledge!")
