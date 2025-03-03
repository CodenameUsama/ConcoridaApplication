import random
board = ['-',  '-', '-',
         '-',  '-', '-',
         '-',  '-', '-',]
currentPlayer = 'X'
Winner = None
gameRunning = True

#Print game Board   
def printBoard() : 
    print('-------------')
    print(board[0] + ' | ', board[1] + ' | ', board[2] + ' | ')
    print('-------------')
    print(board[3] + ' | ', board[4] + ' | ', board[5] + ' | ')
    print('-------------')
    print(board[6] + ' | ', board[7] + ' | ', board[8] + ' | ')
    print('-------------')


# player input
def playerInput() :
    inp = int(input('Entre number from 1 to 9: '))
    if inp >= 1 and inp <= 9 and board[inp-1] == '-':
        board[inp-1] = currentPlayer
        return True
    else :
        print('invalid input, please choose another number') 
        return False



#check for win or tie
def checkHorizontal():
    global winner 
    if board[0] == board[1] == board[2] and board[0] != '-':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != '-':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != '-':
        winner = board[6]
        return True
    
def checkVeritcal():
    global winner
    if board[0] == board[3] == board[6] and board[0] != '-':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != '-':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != '-':
        winner = board[2]
        return True
    
def checkDiagonal():
    global winner
    if board[0] == board[4] == board[8] and board[0] != '-':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != '-':
        winner = board[2]
        return True
    

def checkTie():
    global gameRunning
    if '-' not in board and checkDiagonal() and checkVeritcal() and checkHorizontal():
        printBoard()
        print('its a tie')
        gameRunning = False

def checkWin():
    if checkHorizontal() or checkDiagonal() or checkVeritcal() :
        print('The winner is ' + winner)
        gameRunning = False
        
#switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer = "O"
    else :
        currentPlayer = 'X'


#computer
def computer():
    while currentPlayer == 'O':
        position = random.randint(0, 8)
        if board[position] == '-':
            board[position] = 'O'
            switchPlayer()




#check for win or tie AGAIN
while gameRunning :
    printBoard()
    while not playerInput() :
        pass
    else :
        pass
    checkWin()
    checkTie()
    switchPlayer()
    computer()