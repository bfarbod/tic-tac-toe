from __future__ import print_function
import sys
import random



#-----------------------------------------------------------------------------------
# player_input
# -----------------------------------------------------------------------------------

def display_board(board_list):
    """
    display_board: display a list in board like manner
    IN: board_list a list of numbers or characters
    RETURN: Nothing
    MODIFIES: Nothing
    CALL: Nothing
    Description: It prints a list of numbers or characters in a try/except situation
    if it's a number it's going to add 1 to it and turn it into integer if it couldn't
    turn it into an integer then it's a character and it's going to print it
    """
    count = 0

    print ()

    for cell in board_list:
        # if you're in the 3rd column then print a new line
        if count > 2:
            print()
            count = 0

        print ("|",cell,"|" ,end="")

        count = count + 1


# -----------------------------------------------------------------------------------
# player_input
# -----------------------------------------------------------------------------------

def player_input():
    """
    player_input: It asks the user to enter an input
    IN: Nothing
    RETURN: input = an integer that player has chosen
    MODIFIES: Nothing
    CALL: Nothing
    Description: If the input that was provided was greater than 9 or less than 1
    it asks the user for the input again. If the input was -1 it breaks the while loop
    and quits the program. If the input was between 1 and 9 then it returns the input
    """
    while True:
        print()
        input = raw_input("Enter a cell number( enter -1 to quit): ")
        try:
            input = int(input)
        except:
            print ("Enter an integer!")
            continue

        if input == -1:
            answer = raw_input("Do you want to quit? (y/n): ")
            answer = answer.strip()
            answer = answer.lower()

            # if it's yes exit the program
            if answer[0] == "y":
                sys.exit(0)
            # anything else continue at the top of while loop
            elif answer[0] == "n":
                continue
            else:
                print ("\nYou didn't provide the sufficient answer!(y or n)\n")
                continue

        if input < 1 or input > 9:
            print ("Input must be 1 <= input <= 9")
            continue
        else:
            return input

# -----------------------------------------------------------------------------------
# place_marker
# -----------------------------------------------------------------------------------

def place_marker (board_list, marker, position):
    """
    place_marker: places "X" or "O" in the board_list
    IN; board_list = a list of cell to be filled with "X" or "O", marker = "X" or "O" character, position = integer as in where to put the marker
    RETURN: board_list = a list of cells
    MODIFIES: board_list
    CALL: Nothing
    Description: It places "X" or "O" into its position in the list but because list's index starts from
    zero I need to subtract one from it.
    """

    board_list[position - 1] = marker
    return board_list

# -----------------------------------------------------------------------------------
# win_check
# -----------------------------------------------------------------------------------
def win_check (board_list, mark):
    """
    win_check: Checks to see if any 3 cells in horizental, vertical or diameter manner are matched
    IN; board_list = a list of cell to be filled with "X" or "O", mark = "X" or "O" character
    RETURN: True or False
    MODIFIES: Nothing
    CALL: Nothing
    Description: It checkes to see if any 3 cells in horizental, vertical and diameter have the same mark
    and it returns true if that's the case otherwise returns false.
    Horizental: It checks 0,1,2  ,  3,4,5  ,  6,7,8   of list index.
    Vertical: It checks 0,3,6  ,  1,4,7  ,  2,5,8   of list index.
    Diameters: It checks 0,4,8  ,  2,4,6   of list index.
    """

    # Check the horizental cells
    for step in xrange (0,7,3):
        if board_list[0 + step] == mark and board_list[1 + step] == mark and board_list[2 + step] == mark:
            return True

    # Check the vertical cells
    for step in xrange (0,3):
        if board_list[0 + step] == mark and board_list[3 + step] == mark and board_list[6 + step] == mark:
            return True

    # Check the diameters of board
    for step in xrange (0,3,2):
        if board_list[0 + step] == mark and board_list[4] == mark and board_list[8 - step] == mark:
            return True


    # If 3 cells match coulnd't be found
    return False


# -----------------------------------------------------------------------------------
# choose_first
# -----------------------------------------------------------------------------------
def choose_first ():
    """
    choose_first: It randomly selects which player ("X" or "O") should go first.
    IN;Nothing
    RETURN: "X" or "O"
    MODIFIES: Nothing
    CALL: random.randint () function from import library
    Description: Based on randint function between 1 <= number <= 2 and it returns one of them and we return
    "X" or "O" based on that choice
    """

    choice = random.randint (1,2)
    if choice == 1:
        return "X"
    else:
        return "O"


# -----------------------------------------------------------------------------------
# space_check
# -----------------------------------------------------------------------------------
def space_check (board_list, position):
    """
    space_check: It checks to see if the position that you applied is available or not.
    IN;board_list = a list of cell to be filled with "X" or "O", position = an integer for board_list index
    RETURN: True of False
    MODIFIES: Nothing
    CALL: Nothing
    Description: It checks to see if the position is available or not and remember
    that list starts with index 0 so we need to subtract 1 from position, also we filled the list with string numbers
    so we are going to check if the position is digit.
    """

    if board_list[position - 1].isdigit():
        return True

    # If it's not a number then (if it's not empty)
    return False


# -----------------------------------------------------------------------------------
# full_board_check
# -----------------------------------------------------------------------------------
def full_board_check (board_list):
    """
    space_check: It checks if the board is full and returns a boolean value. True if full, False otherwise.
    IN;board_list = a list of cell to be filled with "X" or "O" .
    RETURN: True of False
    MODIFIES: Nothing
    CALL: Nothing
    Description: It checks to see if the board is full of "X"s or "O"s and returns True if that's the case. Since the board_list is full of string numbers
    then isdigit() function is the best option to check if there's any number in the list.
    """

    for cell in board_list:
        if cell.isdigit ():
            return False

        return True
#-----------------------------------------------------------------------------------
#player_choice
#-----------------------------------------------------------------------------------
def player_choice (board_list):
    """
    player_choice: It checks to see if the place that you have chosen is free or not.
    IN;board_list = a list of cell to be filled with "X" or "O" .
    RETURN: input (player's input)
    MODIFIES: Nothing
    CALL: player_input and space_check functions
    Description: It checks to see if the place that you have chosen is free or not.
    """

    while True:
        input = player_input()
        if space_check (board_list, input):
            return input
        else:
            print ("Number ",input, " cell has been taken!")
            continue


#-----------------------------------------------------------------------------------
#replay
#-----------------------------------------------------------------------------------
def replay ():
    """
    replay: It asks the player if they want to play again
    IN; Nothing
    RETURN: True of False
    MODIFIES: Nothing
    CALL: Nothing
    Description: It asks the player if they want to play again and returns True if they
    want to play again
    """

    while True:
        answer = raw_input ("\n\nDo you want to play again? (y or n): ")
        answer = answer.strip()
        answer = answer.lower()

        if answer[0] == "y":
            return True
        elif answer[0] == "n":
            sys.exit (0)
        else:
            print ("\nplease answer \"y\" or \"n\"!\n")
            continue

#-----------------------------------------------------------------------------------
#preparation
#-----------------------------------------------------------------------------------
def preparation ():
    """
    preparation: It puts string numbers into the list
    IN; Nothing
    RETURN: board_list = a list of cell to be filled with numbers from 1 to 9.
    MODIFIES: board_list
    CALL: Nothing
    Description: In order for player to see which cell needs to be selected we are
    going to fill it with string numbers from 1 to 9. Also in this way you consume less
    memory instead of hard coding list with string numbers and I know it's not much memroy
    that we need to be concern about but it's good practice.
    """

    number = 1
    board_list = []

    for cell in xrange (0,9):
        number_str = str (number)
        board_list.append (number_str)
        number = number + 1

    return board_list



# -----------------------------------------------------------------------------------
# main
# -----------------------------------------------------------------------------------

def main():
    board_list = preparation ()
    display_board (board_list)
    print ( replay () )



if __name__ == "__main__":
    main()
