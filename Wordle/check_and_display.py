from wonderwords import RandomWord
red = '🚨'
yellow = '🚧'                 
green = '💚'

def check_and_display_letters(guess, answer):
    index = 0
    correct = 0

    for letter in guess:
        if letter == answer[index]:
            print(letter,"-",green)
            correct += 1
        elif (letter in answer) and letter != answer[index]:
            print(letter,"-",yellow)
        else:
            print(letter,"-",red)             
        index += 1  

    return True if correct == 5 else False
        