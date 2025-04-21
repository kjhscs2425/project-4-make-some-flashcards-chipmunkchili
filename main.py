import os
import json
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



# 2010s set (10 cards)
Roar = "I got the eye of the tiger, a fighter. Dancing through the fire. 'Cause I am a champion..."
What_Makes_You_Beautiful = "The way that you flip your hair gets me overwhelmed. But when you smile at the ground, it ain't hard to tell. You don't know, oh-oh,..."
Call_Me_Maybe = "I threw a wish in the well. Don't ask me, I'll never tell. I looked to you as it fell..."
California_Gurls = "You could travel the world. But nothing comes close to the golden coast. Once you party with us..."
Baby = "Are we an item? Girl, quit playin'. We're just friends..."
Diamonds = "Find light in the beautiful sea, I choose to be happy. You and I, you and I, we're like..."
Let_It_Go = "I don't care what they're going to say. Let the storm rage on..."
Someone_Like_You = "Don't forget me, I beg. I remember you said, Sometimes it lasts in love, but..."
Me = "Girl, there ain't no I in team. But..."
Somebody_That_I_Used_To_Know = "Have your friends collect your records and then change your number. Guess that I don't need that, though..."



songs_2010s = {
    Roar : "and you're gonna hear me roar",
    What_Makes_You_Beautiful : "you don't know you're beautiful",
    Call_Me_Maybe : "and now you're in my way",
    California_Gurls : "you'll be falling in love",
    Baby : "what are you sayin'",
    Diamonds : "diamonds in the sky",
    Let_It_Go : "the cold never bothered me anyway",
    Someone_Like_You : "sometimes it hurts instead",
    Me : "you know there is a me",
    Somebody_That_I_Used_To_Know : "that i used to know"
}
prompt_2010s = list(songs_2010s.keys())
answer_2010s = list(songs_2010s.values())


number_options = None
correct_questions = []
incorrect_questions = []

def set():
    global number_options
    number_options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    return input("Which decade set do you want to play? (80s, 2010s) ")
decade = set()


def read_past_questions(filename, decade):
    if not os.path.isfile(filename):
        return []
    
    with open(filename, "r") as f:
        all_questions = json.load(f)
    key = f"lyrics_{decade}"
    if key in all_questions.keys():
        decade_questions = all_questions[key]
    else:
        decade_questions = []
    return decade_questions
    
def find_lyric_in_lyrics_list(lyrics_list, target_lyric):
    for index, lyric in enumerate(lyrics_list):
        if lyric == target_lyric:
            return index
    return None


def update_file(filename, new_information, set):
    key = f"lyrics_{set}"
    if os.path.isfile(filename):
        with open(filename, "r") as f:
            old_stats = json.load(f)
        new_stats = old_stats
        
        if key in new_stats.keys():
            new_stats[key].append(new_information)
        else:
            new_stats[key] = [new_information]
    else:
        new_stats = {key: [new_information]}
    with open(filename, "w") as f:
        json.dump(new_stats, f, indent = 2)

def finish_the_lyric():
    global number_options
    global decade
    
    correct_past = read_past_questions("correct.json", decade)
    incorrect_past = read_past_questions("incorrect.json", decade)

    for lyric in correct_past: 
        while lyric in incorrect_past:
            index = find_lyric_in_lyrics_list(incorrect_past, lyric)
            del incorrect_past[index]

    if decade == "80s":
        questions = prompt_80s
    elif decade == "2010s":
        questions = prompt_2010s

    for lyric in incorrect_past:    
        index = find_lyric_in_lyrics_list(questions, lyric)
        number_options.append(index)
       
    while len(number_options) > 0:
        number_index = choice(range(len(number_options)))
        number = number_options[number_index]
        if decade == "80s":
            prompt = prompt_80s[number]
            lyric = input(prompt)
            del number_options[number_index]
            if lyric == answer_80s[number]:
                print("Correct! ✅")
                update_file("correct.json", prompt, "80s")
                correct_questions.append(prompt)

            else:
                print("Incorrect ❌")
                update_file("incorrect.json", prompt, "80s")
                incorrect_questions.append(prompt)
        elif decade == "2010s":
            prompt = prompt_2010s[number]
            lyric = input(prompt)
            del number_options[number_index]
            if lyric == answer_2010s[number]:
                print("Correct! ✅")
                update_file("correct.json", prompt, "2010s")
                correct_questions.append(prompt)

            else:
                print("Incorrect ❌")
                update_file("incorrect.json", prompt, "2010s")
                incorrect_questions.append(prompt)
        else:
            break

    num_correct = len(correct_questions)
    num_incorrect = len(incorrect_questions)
    num_total = num_correct + num_incorrect

    if num_total > 0:
        print(f"\nYou got {num_correct} out of {num_total} correct! 🥳")
        for question in correct_questions:
            print(question)
        print(f"\nYou got {num_incorrect} out of {num_total} incorrect! 😢")
        for question in incorrect_questions:
            print(question)


def summary_stats(filename, status, set):
    with open(filename, "r") as f:
        past_stats = json.load(f)
    key = f"lyrics_{set}"
    if key in past_stats.keys():
        questions = past_stats[key]
        print(f"\n{status} PAST {set} questions:")
        lyric_counts = {}
        for lyric in questions:
            if lyric in lyric_counts:
                lyric_counts[lyric] += 1
            else:
                lyric_counts[lyric] = 1
        for lyric in lyric_counts:
            print(f"{lyric} (x{lyric_counts[lyric]})")


if os.path.isfile("correct.json") and os.path.isfile("incorrect.json"):
    finish_the_lyric()
    summary_stats("correct.json", "Correct 🥳", "80s")
    summary_stats("incorrect.json", "Incorrect 😢", "80s")
    summary_stats("correct.json", "Correct 🥳", "2010s")
    summary_stats("incorrect.json", "Incorrect 😢", "2010s")
else:
    finish_the_lyric()