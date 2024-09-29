#wordle
from check_and_display import check_and_display_letters
from wonderwords import RandomWord


answer = RandomWord().word(word_min_length=5, word_max_length=5)
num_of_guesses = 1

while True:
    if num_of_guesses <=6: 
            guess = input("Enter your 5-letter guess: ")
            if check_and_display_letters(guess, answer):
                print("You got it right. You took {} attempt(s).".format(num_of_guesses))
                break
    else: 
        print("Sorry, you lost. The answer is {}.".format(answer))
        break
    print()
    num_of_guesses += 1