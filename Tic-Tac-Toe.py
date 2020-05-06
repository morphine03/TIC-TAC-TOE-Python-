def drawField(field):
    for row in range(5):
        if row % 2 == 0:
            paracR = int(row / 2)
            for column in range(5):
                if column%2 == 0:
                    if column != 4:
                        paracC = int(column/2)
                        print(field[paracC][paracR], end="")
                    else:
                        print(field[paracC][paracR])
                else:
                        print("|", end="")
        else:
            print("-----")

Player = 1
currentField = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
drawField(currentField)
while(True):
    print("Player ",Player," turn")
    moveRow = int(input("Enter row: "))
    moveColumn = int(input("Enter column: "))
    #PLAYER 1 TURN
    if Player == 1:
        if currentField[moveColumn][moveRow] == " ":
            currentField[moveColumn][moveRow] = "X"
            Player = 2
    #PLAYER 2 TURN
    else:
        if currentField[moveColumn][moveRow] == " ":
            currentField[moveColumn][moveRow] = "O"
            Player = 1

    drawField(currentField)
