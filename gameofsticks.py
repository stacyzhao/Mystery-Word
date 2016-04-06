
import random
import sys

def starting_number_sticks():
    while True:
        sticks = input("How many sticks do you want to start with? ")
        if sticks == "":
            print("Looks like you didn't give me a number. Try again.")
            continue
        try:
            int(sticks)
            return int(sticks)
        except:
            print("Looks like you didn't give me a whole number. Try again.")
            continue

def user_picks_sticks():
    while True:
        player1 = input("How many sticks do you want to pick up from the table (1-3)? ")
        if player1 == "":
            print("Looks like you didn't give me a number. Try again.")
            continue
        elif player1 == '0':
            print("Your number of sticks needs to be more than 0. Try again.")
            continue
        try:
            int(player1)
            return int(player1)
        except:
            print("Looks like you didn't give me a whole number. Try again.")
            continue
        if int(player1) > 3 or int(player1) < 1:
            print ("Looks like you didn't give me a number from 1 to 3. Try again.")
            continue

def determine_turn(number_of_turns):
    if number_of_turns % 2 == 1:
        #user turn
        return True
    elif number_of_turns % 2 == 0:
        #AI turn
        return False

def play_again():
    "Asks user if they want to play the game again."

    play_again = input("Do you want to play Mystery Word again? [y/N] \n")

    if play_again.lower().strip() == "y":
        main()

    else:
        sys.exit()


def main():
    total_number_sticks = 0
    number_of_turns = 1

    print ("Welcome to the Game of Sticks!")

    while True:
        total_number_sticks = starting_number_sticks()
        while total_number_sticks > 0:
            print("There are {} sticks on the board.".format(total_number_sticks))
            if determine_turn(number_of_turns):
                total_number_sticks -= user_picks_sticks()
            else:
                ai_sticks = ai_picks_sticks(total_number_sticks, game_dict, ai_dict)
                total_number_sticks -= ai_sticks
                print("AI picked {} stick(s).".format(ai_sticks))
            number_of_turns +=1

        else:
            print("Last player to take a turn loses!")
            play_again()

if __name__ == '__main__':
    main()
