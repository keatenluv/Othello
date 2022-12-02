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
import Othello

#Settings
ABPruning = True
DEBUG = False
count = 0

#Controls the users moves
def userMove(b):
    global DEBUG
    global ABPruning
    # Inital user input
    move = input("(" + b.turn + ") " + "Enter the row and column of where you would like to set your piece: ")
    if move == "exit":
        exit()
        # Access settings to turn on debug and ABpruning
    if move == "settings":
        while (move != "back"):
            print("\nSETTINGS:")
            print("\n\tDEBUG:", DEBUG)
            print("\tAlpha Beta pruning:", ABPruning)
            move = input("\nWhat would you like to do? \n\tType 'back' to return to game \n\tDEBUG to switch debug (on/off) \n\tABPruning to switch pruning (on/off)\n")
            if move == "DEBUG":
                if DEBUG:
                    print("Switching DEBUG to OFF")
                    DEBUG = False
                else:
                    print("Switching DEBUG to ON")
                    DEBUG = True
            if move == "ABPruning":
                if ABPruning:
                    print("Switching ABPruning to OFF")
                    ABPruning = False
                else:
                    print("Switching ABPruning to ON")
                    ABPruning = True
            time.sleep(2)
    # Place user piece
    else:
        b.placePiece(move)
        return True

# Contols the AI (minimax)
def controllerBot():
    b = Othello.Othello()
    depthSearch = int(input("What would you like the search depth to be? "))
    userColor = input("What color would you like to play as? ")
    print()

    # Run game until board is full
    while (b.isNotFull()):
        b.printBoard()

        # User turn
        if userColor == b.turn:
            userMove(b)

        # AI turn
        else:
            print("Preforming Minimax to find best move\n")
            time.sleep(2)
            moves = []
            global count
            count = 0

            # Iterate through all possible moves, first max 
            for idx, i in enumerate(b.allValidMoves()):
                boardCopy = copy.deepcopy(b)
                boardCopy.placePiece(i)
                moves.append(minimax(i, depthSearch, boardCopy, b.turn, -math.inf, math.inf))

            # Find best move
            bestMove = np.max(moves)
            for idx, i in enumerate((moves)):
                if i == bestMove:
                    print("\nBest move is ", b.allValidMoves()[idx])
                    print("Total States searched:", count)
                    b.placePiece(b.allValidMoves()[idx])
                    break
    
    # End game processing
    b.printBoard()
    if b.countPieces()[0] > b.countPieces()[1]:
        print("White Wins!")
    elif b.countPieces()[0] < b.countPieces()[1]:
        print("Black Wins!")
    else:
        print("Tie Nobody Wins!")
    print("Game Over")

# minimax function
def minimax(position, depth, boardCopy, botColor, alpha, beta):
    global count
    count += 1

    # if no more depth or the board is full return heuristic value
    if (depth == 0 or not boardCopy.isNotFull()):
        return(heuristic(boardCopy, position))
    
    # Max
    if (boardCopy.turn != botColor):
        maxEval = -math.inf
        for idx, i in enumerate(boardCopy.allValidMoves()):
            bCopy = copy.deepcopy(boardCopy)
            bCopy.placePiece(position)
            eval = minimax(i, depth-1, bCopy, botColor, alpha, beta)
            maxEval = max(maxEval, eval)
            if ABPruning:
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return maxEval

    # Min
    else:
        minEval = math.inf
        for idx, i in enumerate(boardCopy.allValidMoves()):
            bCopy = copy.deepcopy(boardCopy)
            bCopy.placePiece(position)
            eval = minimax(i, depth-1, bCopy, botColor, alpha, beta)
            minEval = min(minEval, eval)
            if ABPruning:
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return minEval

# Heuristic function
def heuristic(board, position):
    # Total heuristic value
    weight = 0

    # Total piece heurisitc
    if board.turn == "White":
        weight += board.countPieces()[1] - board.countPieces()[0]
    else:
        weight += board.countPieces()[0] - board.countPieces()[1]
    
    # Edge position heuristic
    for i in range(7):
        if board.board[i][0] == board.turn[0] or board.board[0][i] == board.turn[0] or board.board[6][i] == board.turn[0] or board.board[i][6] == board.turn[0]:
            weight += 30
        elif board.board[i][0] == board.opposite()[0] or board.board[0][i] == board.opposite()[0] or board.board[6][i] == board.opposite()[0] or board.board[i][6] == board.opposite()[0]:
            weight -= 20
    
    # Corner position heuristic
    if board.board[0][0] == board.turn[0] or board.board[0][6] == board.turn[0] or board.board[6][0] == board.turn[0] or board.board[6][6] == board.turn[0]:
        weight += 200
    elif board.board[0][0] == board.opposite()[0] or board.board[0][6] == board.opposite()[0] or board.board[6][0] == board.opposite()[0] or board.board[6][6] == board.opposite()[0]:
        weight -= 50
    if DEBUG:
        print("Considering", position, "with weight", weight)
    return weight

def controller():
    b = Othello.Othello()
    while (b.isNotFull()):
        b.printBoard()
        userMove(b)         

def main():
    print("\n\nWelcome to an Intelligent Othello Player")
    time.sleep(1)
    bot = input("Would you like to play against a bot? (y/n): ")
    while bot != "y" and bot != "n":
        print("Input not recognized.\n")
        bot = input("Would you like to play against a bot? (y/n): ")
    if bot == "y":
        controllerBot()
    else:
        controller()

if __name__ == "__main__":
    main()
