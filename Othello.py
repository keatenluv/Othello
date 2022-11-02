################################################################
# Name: Keaton Love
# CWID: 102-57-333
# Assignment: #3
# Description: This program implements the game of Othello as 
# well as Mini-Max algorithim with aplha-beta pruning.
###############################################################

# Class for the board
#
# Can print the current state of board, determine if the board is full.
class Board():

    # Initalize the board with 8 rows and 8 columns. Also fills the board with X's
    def __init__(self):
        self.rows = 8
        self.columns = 8
        self.board = [["X" for i in range(self.columns)] for j in range(self.rows)]
        
    # Prints the current state of the board
    def printBoard(self):
        print("   A  B  C  D  E  F  G  H")
        for idx, i in enumerate(self.board):
            print(idx, end="  ")
            for jdx, j in enumerate(i):
                print(j, end="  ")
            print()

    # Sets the starting pieces
    def startGame(self):
        self.board[3][4] = "W"
        self.board[4][3] = "W"
        self.board[3][3] = "B"
        self.board[4][4] = "B"

    # Checks if board is full. Reutrns false is full. True otherwise
    def isNotFull(self):
        for idx, i in enumerate(self.board):
            for jdx, j in enumerate(i):
                if j == "X":
                    return True
                else:
                    continue
        return False

    # Place the users piece on the board
    def placePiece(self, color, position):
        i = int(position[0])
        j = (ord(position[1])-65)
        if color == "white":
            self.board[i][j] = "W"

            
        

def main():
    b = Board()

    while (b.isNotFull()):
        b.startGame()
        b.printBoard()
        move = input("Enter the row and column of where you would like to set your piece: ")
        print()
        b.placePiece("white", move)

        if move == "exit":
            exit()
        else:
            continue
    
if __name__ == "__main__":
    main()
