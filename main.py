import random

gameboard = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
rows = 3
cols = 3

number_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def show_gameboard():
    for x in range(rows):
        print("\n+---+---+---+")
        print("|", end="")
        for y in range(cols):
            print("", gameboard[x][y], end=" |")
    print("\n+---+---+---+")


def modify_gameboard(x, y):
    if x == "user":
        if y == "1":
            gameboard[0][0] = "x"
        elif y == "2":
            gameboard[0][1] = "x"
        elif y == "3":
            gameboard[0][2] = "x"
        elif y == "4":
            gameboard[1][0] = "x"
        elif y == "5":
            gameboard[1][1] = "x"
        elif y == "6":
            gameboard[1][2] = "x"
        elif y == "7":
            gameboard[2][0] = "x"
        elif y == "8":
            gameboard[2][1] = "x"
        elif y == "9":
            gameboard[2][2] = "x"
    elif x == "pc":
        if y == "1":
            gameboard[0][0] = "o"
        elif y == "2":
            gameboard[0][1] = "o"
        elif y == "3":
            gameboard[0][2] = "o"
        elif y == "4":
            gameboard[1][0] = "o"
        elif y == "5":
            gameboard[1][1] = "o"
        elif y == "6":
            gameboard[1][2] = "o"
        elif y == "7":
            gameboard[2][0] = "o"
        elif y == "8":
            gameboard[2][1] = "o"
        elif y == "9":
            gameboard[2][2] = "o"


# game = True


def check_winner():
    if gameboard[0][0] == "x" and gameboard[0][1] == "x" and gameboard[0][2] == "x":
        return "user"
    elif gameboard[0][0] == "o" and gameboard[0][1] == "o" and gameboard[0][2] == "o":
        return "pc"
    elif gameboard[1][0] == "x" and gameboard[1][1] == "x" and gameboard[1][2] == "x":
        return "user"
    elif gameboard[1][0] == "o" and gameboard[1][1] == "o" and gameboard[1][2] == "o":
        return "pc"
    elif gameboard[2][0] == "x" and gameboard[2][1] == "x" and gameboard[2][2] == "x":
        return "user"
    elif gameboard[2][0] == "o" and gameboard[2][1] == "o" and gameboard[2][2] == "o":
        return "pc"
    elif gameboard[0][0] == "x" and gameboard[1][0] == "x" and gameboard[2][0] == "x":
        return "user"
    elif gameboard[0][0] == "o" and gameboard[1][0] == "o" and gameboard[2][0] == "o":
        return "pc"
    elif gameboard[0][1] == "x" and gameboard[1][1] == "x" and gameboard[2][1] == "x":
        return "user"
    elif gameboard[0][1] == "o" and gameboard[1][1] == "o" and gameboard[2][1] == "o":
        return "pc"
    elif gameboard[0][2] == "x" and gameboard[1][2] == "x" and gameboard[2][2] == "x":
        return "user"
    elif gameboard[0][2] == "o" and gameboard[1][2] == "o" and gameboard[2][2] == "o":
        return "pc"
    elif gameboard[0][0] == "x" and gameboard[1][1] == "x" and gameboard[2][2] == "x":
        return "user"
    elif gameboard[0][0] == "o" and gameboard[1][1] == "o" and gameboard[2][2] == "o":
        return "pc"
    elif gameboard[0][2] == "x" and gameboard[1][1] == "x" and gameboard[2][0] == "x":
        return "user"
    elif gameboard[0][2] == "o" and gameboard[1][1] == "o" and gameboard[2][0] == "o":
        return "pc"
    else:
        return "continue"


print("Welcome to Tic Tac Toe Game")
print("*-------------------------*")

while True:
    show_gameboard()
    print("\nPlayer Turn : User")
    pick_number = input("\nPick a number from the game board: ")
    turn_user = "user"
    number_list.remove(pick_number)
    modify_gameboard(turn_user, pick_number)
    show_gameboard()
    winner = check_winner()
    if winner != "continue":
        print("\nGame over. User Won!")
        break
    if number_list:
        print("\nPlayer Turn : Computer")
        random_number = random.choice(number_list)
        turn_pc = "pc"
        number_list.remove(random_number)
        modify_gameboard(turn_pc, random_number)
        show_gameboard()
        winner = check_winner()
        if winner != "continue":
            print("\nGame over. Computer Won!")
            break
    else:
        print("\nGame over. It's a draw!")
        break


