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

