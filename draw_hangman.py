#\033[1;34m \033[0;0m
def draw_hangman(lives, start_lives, hangman):
    if lives > 3:
        while True:
            hangman = "\033[1;34m   |  \n   |  \n\033[0;0m" + hangman
            return hangman
    if lives == 3:
        hangman = "\033[1;34m    _____ \033[0;0m\n" + hangman
        return hangman
    if lives == 2:
        hangman = '''\033[1;34m   _____
  |     |
  |     |
  |     |
  |  
  |  
  |  
__|__
\033[0;0m'''
        return hangman
    if lives == 1:
        hangman = '''\033[1;34m   _____
  |     |
  |     |
  |     |
  |     O
  |  
  |  
__|__
\033[0;0m'''

        return hangman
    if lives == 0:
        hangman = ("\033[1;34m   _____ \n"
                   "  |     | \n"
                   "  |     |\n"
                   "  |     | \n"
                   "  |     O \n"
                   "  |    /|\ \n"
                   "  |    / \ \n"
                   "__|__\n \033[0;0m")

        return hangman       

