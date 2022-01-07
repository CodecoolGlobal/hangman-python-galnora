import random
import sys

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
        choice_theme = input("Please choose if you want countries or capitals (co/ca):  ")
        if choice_theme == "co" or choice_theme == "ca":
            good_input_theme = True
            while good_input_diff is False:
                print("Easy: 1 Medium: 2, Hard: 3")
                choice_diff = input("Please choose a difficulty level: ")
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
        letter = input("Guess a letter or type 'quit' to exit the game: ")
        if letter.isalpha() == True and len(letter) == 1:
            good_input = True
        else:
            if letter == "quit":
                print("Thanks for playing! Bye!")
                sys.exit()
            print("Try a letter!")
    return letter

def check_letter(letter, word):
    if not letter in word.lower():
        print("This letter is not in the word :(")
        return False
    

def letter_replace(word, letter_list, secret_word, letter):
    index=[]
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
        print(f"You've already tried this letter: {letter}")
        pass
    else:
        if letter.isalpha() and len(letter) == 1:
            letter_list.append(letter)
    return(f"You've already tried these letters: {letter_list} \n"  )
    

def lose_life(lives):
    lives -= 1
    return lives


def draw_hangman(lives, start_lives, hangman):
    if lives > 3:
        while True:
            hangman = "   |  \n   |  \n" + hangman
            return hangman
    if lives == 3:
        hangman = "    _____ \n" + hangman
        return hangman
    if lives == 2:
        hangman = '''   _____
  |     |
  |     |
  |     |
  |  
  |  
  |  
__|__
'''
        return hangman
    if lives == 1:
        hangman = '''   _____
  |     |
  |     |
  |     |
  |     O
  |  
  |  
__|__
'''

        return hangman
    if lives == 0:
        hangman = ("   _____ \n"
                   "  |     | \n"
                   "  |     |\n"
                   "  |     | \n"
                   "  |     O \n"
                   "  |    /|\ \n"
                   "  |    / \ \n"
                   "__|__\n")

        return hangman       
        

def win(secret_word):
    if "_" in list(secret_word):
        return False
    else:
        win_message = "You won!"
        return win_message


def lose(lives, word):
    if lives == 0:
        lose_message = f"Game over! The word was: {word}"
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
    hangman=" __|__"
    while win(secret_word) is False:
        letter = letter_input()
        print('\n'f"Your guess is: {letter}"'\n')
        check_letter_fun = check_letter(letter, word)
        if check_letter_fun is False:
            lives = lose_life(lives)
            hangman = (draw_hangman(lives,start_lives_1, hangman))
            print(hangman)
        letter_replace_list, secret_word = letter_replace(word, letter_list, secret_word, letter)
        print(secret_word)
        print(f"lives: {lives}")
        already_tried_letter = tried_letter(letter_list, letter)
        print(already_tried_letter)
        if lose(lives, word):
            print(lose(lives, word))
            break  
    if not lose(lives, word):
        print(win(secret_word))
       
main()
