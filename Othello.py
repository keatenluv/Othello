################################################################
# Name: Keaton Love
# CWID: 102-57-333
# Assignment: #3
# Description: This program implements the game of Othello as 
# well as Mini-Max algorithim with aplha-beta pruning.
###############################################################
import math
import numpy as np
import copy
import time

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

# Class for the game of Othello
# Can print the current state of board, determine if the board is full
class Othello():

    # Initalize the board with 8 rows and 8 columns. Also fills the board with X's
    def __init__(self):
        self.rows = 8
        self.columns = 8
        self.blank = "."
        self.board = [[self.blank for i in range(self.columns)] for j in range(self.rows)]
        self.turn = "Black"
        self.board[3][4] = "B"
        self.board[4][3] = "B"
        self.board[3][3] = "W"
        self.board[4][4] = "W"
        
    def countPieces(self):
        totalW = 0
        totalB = 0
        for idx, i in enumerate(self.board):
            for jdx, j in enumerate(i):
                if j == "W":
                    totalW += 1
                elif j == "B":
                    totalB += 1
        return[totalW, totalB]
    
    # Prints the current state of the board
    def printBoard(self):
        print("   A  B  C  D  E  F  G  H")
        for idx, i in enumerate(self.board):
            print(idx, end="  ")
            for jdx, j in enumerate(i):
                print(j, end="  ")
            print()
        totals = self.countPieces()
        print("White =",totals[0], "Black =", totals[1])

    # Checks if board is full. Reutrns false is full. True otherwise
    def isNotFull(self):
        for idx, i in enumerate(self.board):
            for jdx, j in enumerate(i):
                if j == self.blank:
                    return True
                else:
                    continue
        return False

    # Returns opposite player color
    def opposite(self):
        return "White" if self.turn == "Black" else "Black"

    # Finds all valid moves for current player
    def allValidMoves(self):
        moves = []

        for i in range(8):
            for j in range(8):
                if self.checkValid(i, j):
                    move = [i, chr(j+65)]
                    moves.append(move)

        return moves

    # changes whos turn it is
    def changePlayer(self):
        if (self.turn == "White"):
            self.turn = "Black"
        else:
            self.turn = "White"

    # Given list for x and y. Check if x, y land on the board
    def onBoard(self, check):
        return 0 <= check[0] < self.rows and 0 <= check[1] < self.rows

    def checkValid(self, i, j):
        # Check if desired position is empty
        if self.board[i][j] != self.blank: 
            return False
        
        # Iterate through all possible directions
        for direction in directions:
            check = [i+direction[0], j+direction[1]]

            # While place being checked is on the board and is the opposite piece
            while (self.onBoard(check) and self.board[check[0]][check[1]] == self.opposite()[0]):

                # move to next spot and check if same color piece exists
                check[0] += direction[0]
                check[1] += direction[1]
                if (self.onBoard(check)):
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
                
                self.changePlayer()
                if len(self.allValidMoves()) == 0:
                    self.changePlayer()
                    print("No moves exists it remains", self.turn, "s Turn." )
        except:
            print("Input typed incorrectly \nPlease type your destination as such:   5F   \n")

    # Flips necessary pieces
    def flip(self, direction, i, j):
        check = [i+direction[0], j+direction[1]]
        while (self.board[check[0]][check[1]] == self.opposite()[0]):
            self.board[check[0]][check[1]] = self.turn[0]
            check[0] += direction[0]
            check[1] += direction[1]


def userMove(b):
    move = input("(" + b.turn + ") " + "Enter the row and column of where you would like to set your piece: ")
    if move == "exit":
        exit()
    else:
        b.placePiece(move)

def controllerBot():
    b = Othello()
    depthSearch = int(input("What would you like the search depth to be? "))
    userColor = input("What color would you like to play as? ")
    while (b.isNotFull()):
        b.printBoard()
        if userColor == b.turn:
            userMove(b)
        else:
            moves = []
            for idx, i in enumerate(b.allValidMoves()):
                boardCopy = copy.deepcopy(b)
                boardCopy.placePiece(i)
                moves.append(minimax(i, depthSearch-1, boardCopy, b.turn, -math.inf, math.inf))
            bestMove = np.max(moves)
            for idx, i in enumerate((moves)):
                if i == bestMove:
                    b.placePiece(b.allValidMoves()[idx])
                    break

    b.printBoard()
    print("Game Over")


def minimax(position, depth, boardCopy, botColor, alpha, beta):
    if (depth == 0 or not boardCopy.isNotFull()):
        return(heuristic(boardCopy))
    
    if (boardCopy.turn == botColor):
        maxEval = -math.inf
        for idx, i in enumerate(boardCopy.allValidMoves()):
            eval = minimax(i, depth-1, boardCopy, botColor, alpha, beta)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = math.inf
        for idx, i in enumerate(boardCopy.allValidMoves()):
            eval = minimax(i, depth-1, boardCopy, botColor, alpha, beta)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval

def heuristic(board):
    if board.turn == "White":
        return board.countPieces()[1] - board.countPieces()[0]
    else:
        return board.countPieces()[0] - board.countPieces()[1]

def controller():
    b = Othello()

    while (b.isNotFull()):
        b.printBoard()
        userMove(b)         

def startGame():
    print("Welcome to an Intelligent Othello Player")
    bot = input("Would you like to play against a bot? (y/n): ")
    while bot != "y" and bot != "n":
        print("Input not recognized.\n")
        bot = input("Would you like to play against a bot? (y/n): ")
    if bot == "y":
        controllerBot()
    else:
        controller()


def main():
    startGame()


if __name__ == "__main__":
    main()
