
import random
import re

def subset_word_list():
    easy = []
    normal = []
    hard = []
    with open('/usr/share/dict/words', 'r') as f:
        for word in f:
            word = word.strip("\n").upper()
            if len(word) <= 5:
                easy.append(word)
            elif len(word) >= 5 and len(word) <= 7:
                normal.append(word)
            else:
                hard.append(word)
    word_list = [easy, normal, hard]
    return word_list

#returns a word based on difficulty
def random_word(difficulty):
    easy, normal, hard = subset_word_list()
    if difficulty == "e":
        return random.choice(easy)
    elif difficulty == "n":
        return random.choice(normal)
    else:
        return random.choice(hard)

# returns length of mystery word
def length_of_word(word):
    placeholder = []
    for i in word:
        placeholder.append(" _ ")
    return placeholder

# if guess letter matches, returns the index of the word in a list
def index_in_word(a_letter, word):
    index = []
    for i in range(len(word)):
        if word[i] in a_letter:
            index.append(i)
    return index

# returns partially filled guessed word in a list
def fill_in_letter(a_letter, clue, word):
    index = index_in_word(a_letter, word)
    for i in index:
        clue[i] = a_letter
    return clue

# if user's guess letter matches anything in the word. returns t/f
def does_letter_match(a_letter, word):
    return a_letter in word

# change a list into a str for clue to display
def list_to_str(placeholder):
    return "".join(placeholder)

# check len of guessed letter, making sure its less than 1 letter and if letter in guessed letter
def validate_input(a_letter, guessed_letters):
    clean_text = re.sub("[^A-Za-z]+", "", a_letter)
    if len(clean_text) > 1:
        print ("Just pick one letter!")
        return False

    if clean_text in guessed_letters:
        print ("You already guessed this!")
        return False

    if clean_text == "":
        print ("Numbers and special characters don't count!")
        return False

    return True

# checks if your guess matches clue, if true, returns congrats
def win_game(word, clue):
    if clue.strip() == word:
        print ("Congratulations, you win!!")
        return True

def lost_game(tries, word):
    if tries == 0:
        print ("Sorry! you lost! The word was: {}".format(word))
        return True

def play_again():
    play = input("Do you want to play again? [y]es or [n]o ").upper()
    if "Y" == play:
        return True

def start_game():
        tries = 8
        guessed_letters = []
        difficulty = input("Choose a level of difficulty: [E]asy, [N]ormal or [H]ard mode?").lower()
        chosen_word = random_word(difficulty).upper()
        clue = length_of_word(chosen_word)
        return [tries, guessed_letters, difficulty, chosen_word, clue]



def main():

    tries, guessed_letters, difficulty, chosen_word, clue = start_game()

    while tries > 0:
        print ("You have {} tries.".format(tries))
        guessed_letter = input("Pick a letter: ").upper()

        valid = validate_input(guessed_letter, guessed_letters)
        if valid is False:
            continue
        #does the letter match the word
        letter_match = does_letter_match(guessed_letter, chosen_word)

        if letter_match == True:
            index_in_word(guessed_letters, chosen_word)

        fill = fill_in_letter(guessed_letter, clue, chosen_word)
        display_clue = list_to_str(fill)
        print("Your clue: ", display_clue)

        guessed_letters += guessed_letter

        tries -=1

        used_letter = list_to_str(guessed_letters)
        print ("Used Letters: ", used_letter)

        print ("_________________")
        print ("computer word: ", chosen_word)

        game_win = win_game(display_clue, chosen_word)
        if game_win == True:
            if play_again == True:
                tries, guessed_letter, difficulty, chosen_word, clue = start_game()
                continue
            else:
                break

        game_lost = lost_game(tries, chosen_word)
        if game_lost == True:
            if play_again == True:
                tries, guessed_letter, difficulty, chosen_word, clue = start_game()
                continue
            else:
                break




if __name__ == '__main__':
    main()
