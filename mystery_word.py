import random
import re

# divide word list into difficulty and returns a list with 3 difficulty
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
    if difficulty == "E":
        return random.choice(easy)
    elif difficulty == "N":
        return random.choice(normal)
    else:
        return random.choice(hard)

# returns length of mystery word in a list
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

# if user's guess letter matches anything in the word. returns t/f
def does_letter_match(a_letter, word):
    return a_letter in word

# returns partially filled guessed word in a list
def fill_in_letter(a_letter, clue, word):
    index = index_in_word(a_letter, word)
    for i in index:
        clue[i] = a_letter
    if a_letter in clue:
       print ("Good Guess! {} is in the mystery word.".format(a_letter))
    return clue

# if user gets correct letter, user doesn't lose a try
def dont_lose_guess(a_letter, word):
    return a_letter in word

# change a list into a str
def list_to_str(placeholder):
    return "".join(placeholder)

def list_to_str_used_letter(placeholder):
    return ", ".join(placeholder)

# checks len of guessed letter, making sure its less than 1 letter and if letter in guessed letter
def validate_input(a_letter, guessed_letters):
    clean_text = re.sub("[^A-Za-z]+", "", a_letter)
    if len(clean_text) > 1:
        print ("Just pick one letter! Try again!")
        return False

    if clean_text in guessed_letters:
        print ("You already guessed {}".format(a_letter))
        print ("\n")
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

# checks for tries left and returns true if there's no more tries
def lost_game(tries, word):
    if tries == 0:
        print ("Sorry! You ran out of tries! The word was: {}".format(word))
        return True

# asks if user wants to play again, returns true if they want to play
def play_again():
    while True:
        play = input("Do you want to play again? [Y]es or [N]o ").upper()
        if "Y" == play or "YES" == play:
            return True
        elif "N" == play or "NO" == play:
            return False
        else:
            continue

# ensure user puts in difficulty to get mystery from the right category
def validate_difficulty():
    while True:
        difficulty = input("Choose a level of difficulty: [E]asy, [N]ormal or [H]ard mode?").upper()
        print ("\n")

        clean_text = re.sub("[^A-Za-z]+", "", difficulty)

        if len(clean_text) > 1:
            print ("Just pick one letter! Try again!")
            continue

        if difficulty == "E" or difficulty == "N" or difficulty == "H":
            return difficulty
        else:
            continue

# initalize game variables
def start_game():
    tries = 8
    guessed_letters = []
    difficulty = validate_difficulty()
    chosen_word = random_word(difficulty).upper()
    clue = length_of_word(chosen_word)
    print ("The mystery word has {} letters.".format(len(clue)))

    return [tries, guessed_letters, difficulty, chosen_word, clue]


def main():

    tries, guessed_letters, difficulty, chosen_word, clue = start_game()

    while tries > 0:
        print ("You have {} guesses.".format(tries))
        guessed_letter = input("Please pick a letter: ").upper()

        if validate_input(guessed_letter, guessed_letters) is False:
            continue

        if does_letter_match(guessed_letter, chosen_word) is True:
            index_in_word(guessed_letters, chosen_word)

        display_word = list_to_str(fill_in_letter(guessed_letter, clue, chosen_word))
        print(display_word)

        guessed_letters += guessed_letter
        print ("Used Letters: ", guessed_letters)
        print ("\n")

        if dont_lose_guess(guessed_letter, chosen_word) is True:
            continue

        tries -=1

        if win_game(display_word, chosen_word) == True:
            if play_again() == True:
                tries, guessed_letters, difficulty, chosen_word, clue = start_game()
                continue
            else:
                break

        if lost_game(tries, chosen_word) == True:
            if play_again() == True:
                tries, guessed_letters, difficulty, chosen_word, clue = start_game()
                continue
            else:
                break

if __name__ == '__main__':
    main()
