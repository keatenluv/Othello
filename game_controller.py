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

class Controller():

    # Checks if board is full. Reutrns false is full. True otherwise
    def isNotFull(self):
        for idx, i in enumerate(self.board):
            for jdx, j in enumerate(i):
                if j == self.blank:
                    return True
                else:
                    continue
        return False

    def hey():
        return "hey"

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
                if (self.turn == "White"):
                    self.turn = "Black"
                else:
                    self.turn = "White"
        except:
            print("Input typed incorrectly \nPlease type your destination as such:   5F   \n")

    def flip(self, direction, i, j):
        check = [i+direction[0], j+direction[1]]
        while (self.board[check[0]][check[1]] == self.opposite()[0]):
            self.board[check[0]][check[1]] = self.turn[0]
            check[0] += direction[0]
            check[1] += direction[1]