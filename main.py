import os
from random import *

print("NOTE: don't use any punctuation in your answers! (except apostrophes)")

# https://www.greenwichsu.co.uk/pageassets/welcome/activitypack/Finshthelyrics_Full.pdf

# 80s set (10 cards)
Girls_Just_Wanna_Have_Fun = "The phone rings, in the middle of the night. My father yells..."
Dont_Stop_Believin = "Just a small town girl livin' in a lonely world..."
Never_Gonna_Give_You_Up = "Never gonna give you up. Never gonna let you down..."
Livin_On_A_Prayer = "She says, we've gotta hold on to what we've got. It doesn't make a difference if we make it or not..."
Total_Eclipse_Of_The_Heart = "And I need you now tonight. And I need you more than ever. And if you only hold me tight..."
I_Wanna_Dance_With_Somebody = "Oh, I wanna dance with somebody. I wanna feel the heat with somebody. Yeah, I wanna dance with somebody..."
Every_Breath_You_Take = "Every breath you take. And every move you make. Every bond you break, every step you take..."
Material_Girl = "'Cause we are living in a material world..."
In_The_Air_Tonight = "And I can feel it coming in the air tonight..."
Karma_Chameleon = "Karma karma karma karma karma chameleon..."


songs_80s = {
    Girls_Just_Wanna_Have_Fun : "what you gonna do with your life",
    Dont_Stop_Believin : "she took the midnight train going anywhere",
    Never_Gonna_Give_You_Up : "never gonna run around and desert you",
    Livin_On_A_Prayer : "we've got each other and that's a lot for love",
    Total_Eclipse_Of_The_Heart : "we'll be holding on forever",
    I_Wanna_Dance_With_Somebody : "with somebody who loves me",
    Every_Breath_You_Take : "i'll be watching you",
    Material_Girl : "and i am a material girl",
    In_The_Air_Tonight : "oh lord",
    Karma_Chameleon : "you come and go"
}
prompt_80s = list(songs_80s.keys())
answer_80s = list(songs_80s.values())


number_options = None
correct_questions = []
incorrect_questions = []

def set():
    global number_options
    # number_options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    number_options = [0, 1]
    return input("Which decade set do you want to play? (80s) ")
decade = set()

def update_file(filename, new_information):
    if os.path.isfile(filename):
        with open(filename, "r") as f:
            old_stats = f.read()
        new_stats = old_stats + new_information
    else:
        new_stats = new_information
    with open(filename, "w") as f:
        f.write(f"{new_stats}\n")

def finish_the_lyric():
    global number_options
    global decade
    while len(number_options) > 0:
        number = choice(number_options)
        if decade == "80s":
            prompt = prompt_80s[number]
            lyric = input(prompt)
            number_options.remove(number)
            if lyric == answer_80s[number]:
                print("Correct! ✅")
                update_file("correct.txt", prompt)
                correct_questions.append(prompt)

            else:
                print("Incorrect ❌")
                update_file("incorrect.txt", prompt)
                incorrect_questions.append(prompt)
        else:
            break

    num_correct = len(correct_questions)
    num_incorrect = len(incorrect_questions)
    num_total = num_correct + num_incorrect

    if num_total > 0:
        print("\n")
        print(f"You got {num_correct} out of {num_total} correct!")
        for question in correct_questions:
            print(question)
        print("\n")
        print(f"You got {num_incorrect} out of {num_total} incorrect!")
        for question in incorrect_questions:
            print(question)
        
        play_more = input("Would you like to keep playing? (yes or no) ")
        if play_more == "yes":
            decade = set()
            finish_the_lyric()

finish_the_lyric()