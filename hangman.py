import random
import sys
from draw_hangman import draw_hangman

def split_lists():
    f=list(open('countries-and-capitals.txt','r'))
    all_countries=[]
    all_capitals=[]
    for n in f:
        all_countries.append(n.split("|")[0])
        all_capitals.append(n.split("|")[1])
    countries_list= [[] for _ in range(3)]
    capitals_list = [[] for _ in range(3)]
    for m in all_countries:
        if len(m) <= 7:
            countries_list[0].append(" "+m)
        elif len(m) <= 10:
            countries_list[1].append(" "+m)
        else:
            countries_list[2].append(" "+m)
    for i in all_capitals:
        if len(i) <= 7:
            capitals_list[0].append(i.rstrip())
        elif len(i) <=10:
            capitals_list[1].append(i.rstrip())
        else:
            capitals_list[2].append(i.rstrip())

    return (countries_list, capitals_list)
    

def difficulty():
    good_input_theme = False
    good_input_diff = False
    while good_input_theme is False:
        choice_theme = input("Please choose if you want countries or capitals (co/ca)  \n \033[1;31m (If you want to exit type quit) \033[0;0m \n")
        if choice_theme == "quit":
            print("\033[1;33m Bye!")
            sys.exit()
        if choice_theme == "co" or choice_theme == "ca":
            good_input_theme = True
            while good_input_diff is False:
                print("Easy: 1 Medium: 2, Hard: 3")
                choice_diff = input("Please choose a difficulty level \n \033[1;31m (If you want to exit type quit) \033[0;0m \n")
                if choice_diff == "quit":
                    print("\033[1;33m Bye!")
                    sys.exit()
                if choice_diff == "1" or choice_diff == "2" or choice_diff == "3": 
                        good_input_diff = True
                else:
                    print("You can chose 1, 2 or 3")
        else:
            print("You can chose 'co' or 'ca'")
    return choice_theme, int(choice_diff)
    

def word_to_guess(theme, diff):
    countries, capitals = split_lists()
    if theme == "co":
        return random.choice(countries[diff-1])
    return random.choice(capitals[diff-1])
    

def start_lives(choice_diff):
    lives = 0
    if choice_diff == 1:
        lives += 8
        start_lives_1 = lives
        print(f'Lives: {lives}')
    elif choice_diff == 2:
        lives += 7
        start_lives_1 = lives
        print(f'Lives: {lives}')
    elif choice_diff == 3:
        lives += 6
        start_lives_1 = lives
        print(f'Lives: {lives}')
    return lives, start_lives_1
    

def replace(word):
    secret_word = ""
    num_letters = len(word)
    for letter in word:
        if letter == " ":
            secret_word += "  "
        elif letter == "-":
            secret_word += "-"
        else:
            secret_word += "_ "
    return secret_word


def letter_input(): 
    good_input = False
    letter = ""
    while good_input is False:
        letter = input("Guess a letter \n \033[1;31m (or type 'quit' to exit the game) \033[0;0m \n")
        if letter.isalpha() == True and len(letter) == 1:
            good_input = True
        else:
            if letter == "quit":
                print("\033[1;33m Thanks for playing! Bye!")
                sys.exit()
            print("Try a letter!")
    return letter

def check_letter(letter, word, letter_list):
    if letter in letter_list:
        return True
    if not letter in word.lower():
        print("\033[1;31m This letter is not in the word :( \n")
        return False
    

def letter_replace(word, letter_list, secret_word, letter):
    index=[]
    origin_word = list(word)
    word=word.lower()
    for x in range(len(word)):
        if word[x] == letter:
            index.append(x*2)
    for y in range(len(secret_word)):
        for z in index:
            if y == z:
                if not y == 2:
                    s= list(secret_word)
                    s[y] = letter
                    secret_word= "".join(s)
                else:
                    s= list(secret_word)
                    s[y] = letter.upper()
                    secret_word= "".join(s)

    return letter_list, secret_word


def tried_letter(letter_list, letter):
    if letter in letter_list:
        print(f"\033[1;31m You've already tried this letter: {letter} \033[0;0m\n")
    else:
        if letter.isalpha() and len(letter) == 1:
            letter_list.append(letter)
    return(f"You've already tried these letters: \033[1;36m  {letter_list} \033[0;0m \n"  )
    

def lose_life(lives):
    lives -= 1
    return lives
     

def win(secret_word):
    if "_" in list(secret_word):
        return False
    else:
        win_message = "\033[0;32m Congrats! You won! \n"
        return win_message


def lose(lives, word):
    if lives == 0:
        lose_message =  f"\033[1;31m Game over! The word was: {word} \n"
        return lose_message


def main():
    split_lists()
    choice_theme, choice_diff = difficulty()
    word = word_to_guess(choice_theme, choice_diff)
    # print(word)
    lives, start_lives_1 = start_lives(choice_diff)
    secret_word = replace(word)
    print(secret_word)
    letter_list = []
    hangman="\033[1;34m __|__\033[0;0m"
    while win(secret_word) is False:
        letter = letter_input()
        print('\n'f"Your guess is: {letter}"'\n')
        check_letter_fun = check_letter(letter, word, letter_list)
        if check_letter_fun is False:
            lives = lose_life(lives)
            hangman = (draw_hangman(lives,start_lives_1, hangman))
            print(hangman)
        letter_replace_list, secret_word = letter_replace(word, letter_list, secret_word, letter)
        print(secret_word)
        print(f"\033[1;35;40m lives: {lives} \033[0;0m")
        already_tried_letter = tried_letter(letter_list, letter)
        print(already_tried_letter)
        if lose(lives, word):
            print(lose(lives, word))
            break  
    if not lose(lives, word):
        print(win(secret_word))
       
main()

