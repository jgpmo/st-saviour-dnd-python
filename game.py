import random
import time

from draw import draw_d20, draw_d6, draw_d4

def print_dramatic_text(text: str, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

if __name__ == '__main__':
    # create character by collecting user input (name + class)
    # print character sheet
    # specify roll that must be beat and enemy initiative by collecting user input
    # any buffs / debuffs?
    # any critical success / failure?

    name = input('Name: ')
    role = input('Role: ')

    score = 0

    print('Your name is ' + name + ' and your role is ' + role + '.')
    print_dramatic_text('Welcome to my trivia game!')

    answer = input('Question 1: What is Mr. Mazey\'s favorite animal? ')
    #put space between ? and ' so player can have room to type
    if answer.lower()== 'fox':
        #i put all my answers in lowercase because people are lazy
        score += 1
        print_dramatic_text('Correct!')
    else:
        print_dramatic_text('Incorrect ...')

    # input('Press Enter to roll a d6.')
    # roll = random.randint(1, 6)
    # draw_d6(roll)

    print_dramatic_text('Congratulations ' + name + ' you scored ' + str(score) + '!')

    answer = input('Question 2: What is Mr. Mazey\'s favorite color? ')
    if answer == 'evergreen':
        score += 2
        print_dramatic_text('Correct!')
    else:
        print_dramatic_text('Incorrect ...')
#congradulations and list new or no points
    print_dramatic_text('Congratulations ' + name + ' you scored ' + str(score) + '!')

    answer = input('Question 3: What is Mr. Mazey\'s first name? ')
    if answer == 'brandon':
        score += 3
        print_dramatic_text('Correct!')
    else:
        print_dramatic_text('Incorrect ...')

    print_dramatic_text('Congratulations ' + name + ' you scored ' + str(score) + '!')

    answer = input('Question 4: What is Mr. Mazey\'s favorite Anime? ')
    if answer == 'hunter hunter':
        score += 4
        print_dramatic_text('Correct!')
    else:
        print_dramatic_text('Incorrect ...')

    print_dramatic_text('Congratulations ' + name + ' you scored ' + str(score) + '!')

    answer = input('Question 5: What is Mr. Mazey\'s least favorite subject? ')
    if answer == 'spanish':
        score += 5
        print_dramatic_text('Correct!')
    else:
        print_dramatic_text('Incorrect ...')

    print_dramatic_text('Congratulations ' + name + ' you scored ' + str(score) + '!')

    answer = input('Question 6: Where did Mr. Mazey go to college? ')
    if answer == 'nyu':
        score += 7
        print_dramatic_text('Correct!')
    else:
        print_dramatic_text('Incorrect ...')

    print_dramatic_text('Congratulations ' + name + ' you scored ' + str(score) + '!')

