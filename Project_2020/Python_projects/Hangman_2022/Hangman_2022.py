import random
from words import word_list
import time

word = random.choice(word_list)

name = input("Please introduce your name: ")
time.sleep(1)
print("Hi, " + name + " Its time for some Hangman!!!")
time.sleep(1)
print("its time to guess!!!")
time.sleep(1)

allowed_errors = len(word)
guesses = []
done = False

while not done:
    for letter in word:
        if letter.upper() in guesses:
            print(letter, end=" ")
        else:
            print("*", end =" ")
    print("")
    done = True

    guess = input(f"you have {allowed_errors} left, What is your next guess: ")
    guesses.append(guess.upper())
    if guess.upper() not in word.upper():
        allowed_errors -=1
        if allowed_errors ==0:
            time.sleep(1)
            print(f"You have losse the word was: {word.upper()}")
            break
        else:
            time.sleep(1)
            print(f"You find the word {word.upper()}!")

    done = True
    for letter in word:
         if letter.upper() not in guesses:
            done = False