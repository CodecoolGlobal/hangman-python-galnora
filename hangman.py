import random

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
            countries_list[0].append(m)
        elif len(m) <= 10:
            countries_list[1].append(m)
        else:
            countries_list[2].append(m)
    for i in all_capitals:
        if len(i) <= 7:
            capitals_list[0].append(i.rstrip())
        elif len(i) <=10:
            capitals_list[1].append(i.rstrip())
        else:
            capitals_list[2].append(i.rstrip())

    return (countries_list, capitals_list)
    

def difficulty():
    choice_theme = input("Please choose if you want countries or capitals (co/ca):  ")
    print("Easy: 1 Medium: 2, Hard: 3")
    choice_diff = int(input("Please choose a difficulty level: "))
    return choice_theme, choice_diff
    

def word_to_guess(theme, diff):
    countries, capitals = split_lists()
    if theme == "co":
        return random.choice(countries[diff-1])
    return random.choice(capitals[diff-1])
    

def start_lives(choice_diff):
    lives = 0
    if choice_diff == 1:
        lives += 7
        print(f'Lives: {lives}')
    elif choice_diff == 2:
        lives += 6
        print(f'Lives: {lives}')
    elif choice_diff == 3:
        lives += 5
        print(f'Lives: {lives}')
    return lives
    

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
    letter = input("Guess a letter: ")
    return letter.lower()


def check_letter(letter, word):
    if not letter in word.lower():
        print("This letter is not in the word :(")
        return False
    if letter == "quit":
        print("Thanks for playing! Bye!")
        exit


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


def tried_letter(letter_list,letter):
    if letter in letter_list:
        print("You've already tried this letter")
        pass
    else:
        letter_list.append(letter)
    return(f"You've already tried these letters: {letter_list}")
    

def lose_life(lives):
    lives -= 1
    return lives

def draw_hangman(lives):
    if lives == 6:
    hangman =    ("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
    
def win(secret_word):
    if "_" in list(secret_word):
        return False
    else:
        win_message = "You won!"
        return win_message

def lose(lives):
    if lives == 0:
        lose_message = "Game over!"
        return lose_message

# if the letter is not present in the word decrease the value in the lives variable
# and display a hangman ASCII art. You can search the Internet for "hangman ASCII art",
# or draw a new beautiful one on your own.

def main():
    split_lists()
    choice_theme, choice_diff = difficulty()
    word = word_to_guess(choice_theme, choice_diff)
    print(word)
    lives = start_lives(choice_diff)
    secret_word = replace(word)
    print(secret_word)
    letter_list = []
    while win(secret_word) is False:
        letter = letter_input()
        check_letter_fun = check_letter(letter, word)
        if check_letter_fun is False:
            lives = lose_life(lives)
        letter_replace_list, secret_word = letter_replace(word, letter_list, secret_word, letter)
        print(secret_word)
        print(f"lives: {lives}")
        print(draw_hangman(lives))
        already_tried_letter = tried_letter(letter_list,letter)
        print(already_tried_letter)
        if lose(lives):
            print(lose(lives))
            break  
    if not lose(lives):
        print(win(secret_word))
       
main()


        # elif count == 5:
        #     time.sleep(1)
        #     print("   _____ \n"
        #           "  |     | \n"
        #           "  |     |\n"
        #           "  |     | \n"
        #           "  |     O \n"
        #           "  |    /|\ \n"
        #           "  |    / \ \n"
        #           "__|__\n")
        #     print("Wrong guess. You are hanged!!!\n")
        #     print("The word was:",already_guessed,word)
        #     play_loop()
