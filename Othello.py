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
        self.blank = "."
        self.board = [[self.blank for i in range(self.columns)] for j in range(self.rows)]
        self.turn = "Black"
        
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
                if j == self.blank:
                    return True
                else:
                    continue
        return False

    # Place the users piece on the board
    def placePiece(self, dest):
        try:
            i = int(dest[0])
            j = (ord(dest[1])-65)
            if self.board[i][j] == self.blank:
                self.board[i][j] = self.turn[0]
                if (self.turn == "White"):
                    self.turn = "Black"
                else:
                    self.turn = "White"
            else:
                print("Please select an empty location.\n")  
        except:
            print("Input typed incorrectly \nPlease type your destination as such:   5F   \n")


def main():
    b = Board()

    while (b.isNotFull()):
        b.startGame()

        b.printBoard()
        move = input("(" + b.turn + ") " + "Enter the row and column of where you would like to set your piece: ")

        if move == "exit":
            exit()
        else:
            b.placePiece(move)
    
if __name__ == "__main__":
    main()
