from pyfiglet import Figlet

f = Figlet(font = 'slant')
print(f.renderText('tic tac toe'))
print('tic tac toe')

def show():
    for i in game_board:
        for j in i:
            print(j, end=" ")
        print()


def check_gameplayer1():
    #ofoghi
    if game_board[0][0] =="x" and game_board[0][1] == "x" and game_board[0][2]== "x":
        print("player1 won!!!!")
    if game_board[1][0] == "x" and game_board[1][1] == "x" and game_board[1][2] == "x":
        print("player 1 won!!!")
    if game_board[2][0] == "x" and game_board[2][1] == "x" and game_board[2][2] == "x":
        print("player 1 won!!!!")
    #amoodi
    if game_board[0][0] == "x" and game_board[1][0] == "x" and game_board[2][0] == "x":
        print("player 1 won!!!")
    if game_board[0][1] == "x" and game_board[1][1] == "x" and game_board[2][1] == "x":
        print("player 1 won!!!")
    if game_board[0][2] == "x" and game_board[1][2] == "x" and game_board[2][2] == "x":
        print("player1 won!!!")
    #movarab
    if game_board[0][0] == "x" and game_board[1][1] == "x" and game_board[2][2]== "x":
        print("player 1 won!!!!")
        


def check_gameplayer2():
    #ofoghi
    if game_board[0][0] =="o" and game_board[0][1] == "o" and game_board[0][2]== "o":
        print("player2 won!!!!")
    if game_board[1][0] == "o" and game_board[1][1] == "o" and game_board[1][2] == "o":
        print("player 2 won!!!")
    if game_board[2][0] == "o" and game_board[2][1] == "o" and game_board[2][2] == "o":
        print("player 2 won!!!!")
    #amoodi
    if game_board[0][0] == "o" and game_board[1][0] == "o" and game_board[2][0] == "o":
        print("player 2 won!!!")
    if game_board[0][1] == "o" and game_board[1][1] == "o" and game_board[2][1] == "o":
        print("player 2 won!!!")
    if game_board[0][2] == "o" and game_board[1][2] == "o" and game_board[2][2] == "o":
        print("player2 won!!!")
    #movarab
    if game_board[0][0] == "o" and game_board[1][1] == "o" and game_board[2][2]== "o":
        print("player 2 won!!!!")


def mosavi():
    if "-" not in game_board:
        print("mosavi!!!")

game_board =[["-", "-", "-"], 
            ["-", "-", "-"],
            ["-", "-", "-"]]
print("*****************************************")
show()
while True:
    #player1
    print("player1")
    while True:
        row = int(input("enter row player1:" ))
        col = int(input("enter col player1: "))
        if 0 <= row <= 2 and 0 <= col <=2:

            if game_board[row][col] == "-":
                game_board[row][col] = "x"
                show()
                check_gameplayer1()
                break
            else:
                print(" select another !!!")
        else:
            print("select between 0 to 2!!!")
        
    #player2 
    print("player2")
    while True:
        row = int(input("enter row player 2"))
        col = int(input("enter col player2"))
        if 0 <= row <= 2 and 0 <= col <=2:
            if game_board[row][col] == "-":
                game_board[row][col] = "o"
                show()
                check_gameplayer2()
                break
            else:
                print(" select another !!!")
        else:
            print("select between 0 to 2!!!")   
           

mosavi()