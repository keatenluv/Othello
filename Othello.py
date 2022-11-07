################################################################
# Name: Keaton Love
# CWID: 102-57-333
# Assignment: #3
# Description: This program implements the game of Othello as 
# well as Mini-Max algorithim with aplha-beta pruning.
###############################################################


# All possible directions
directions = [
    (0, -1),
    (1, -1),
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
]

# Class for the board
# Can print the current state of board, determine if the board is full.
class Othello():

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
        self.board[3][4] = "B"
        self.board[4][3] = "B"
        self.board[3][3] = "W"
        self.board[4][4] = "W"

    # Checks if board is full. Reutrns false is full. True otherwise
    def isNotFull(self):
        for idx, i in enumerate(self.board):
            for jdx, j in enumerate(i):
                if j == self.blank:
                    return True
                else:
                    continue
        return False

    def opposite(self):
        return "White" if self.turn == "Black" else "Black"

    def checkValid(self, i, j):
        # Check if desired position is empty
        if self.board[i][j] != self.blank: 
            print("\nPlease select an empty location\n")
            return False
        
        # Iterate through 
        for direction in directions:
            check = [i+direction[0], j+direction[1]]
            while 0 <= check[0] < self.rows and 0 <= check[1] < self.rows and self.board[check[0]][check[1]] == self.opposite()[0]:
                check[0] += direction[0]
                check[1] += direction[1]
                if self.board[check[0]][check[1]] == self.turn[0]:
                    return True
        return False

    # Place the users piece on the board
    def placePiece(self, dest):
        try:
            i = int(dest[0])
            j = (ord(dest[1])-65)
            if self.checkValid(i, j):
                self.board[i][j] = self.turn[0]
                for direction in directions:
                    check = [i+direction[0], j+direction[1]]
                    while 0 <= check[0] < self.rows and 0 <= check[1] < self.rows:
                        if self.board[check[0]][check[1]] == self.blank:
                            break
                        if self.board[check[0]][check[1]] == self.turn[0]:
                            self.flip(direction, i, j)
                            break
                        check[0] += direction[0]
                        check[1] += direction[1]
                if self.check_move_exists:
                    if (self.turn == "White"):
                        self.turn = "Black"
                    else:
                        self.turn = "White"
                else:
                    print("No moves exists it remains", self.turn, "s Turn." )
                    
        except:
            print("Input typed incorrectly \nPlease type your destination as such:   5F   \n")

    def flip(self, direction, i, j):
        check = [i+direction[0], j+direction[1]]
        while (self.board[check[0]][check[1]] == self.opposite()[0]):
            self.board[check[0]][check[1]] = self.turn[0]
            check[0] += direction[0]
            check[1] += direction[1]

    def check_move_exists(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.checkValid(i, j):
                    return True
        return False




def main():
    b = Othello()
    b.startGame()

    while (b.isNotFull()):
        b.printBoard()
        move = input("(" + b.turn + ") " + "Enter the row and column of where you would like to set your piece: ")
        
        if move == "exit":
            exit()
        else:
            b.placePiece(move)

    totalW = 0
    totalB = 0
    for idx, i in enumerate(b.board):
        for jdx, j in enumerate(i):
            if j == "W":
                totalW += 1
            else:
                totalB += 1
    
    if (totalB > totalW):
        print("Black Wins!")
    elif (totalW > totalB):
        print("White Wins!")
    else:
        print("Tie! Nobody Wins!")
    
#if __name__ == "__main__":
    #main()
