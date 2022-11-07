from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import Othello

window = Tk()
frm = ttk.Frame(window, padding=10)
frm.grid()
window.title("Othello")

image1 = ImageTk.PhotoIamge(Image.open("Green_square.png"))


game = Othello.Othello()
game.startGame()
game.printBoard()

def flip():
    ttk.Label(frm, text="B").grid(column = 0, row = 0)

for idx, x in enumerate(game.board):
    for idy, y in enumerate(game.board[idx]):
        window.creat
        if game.board[idx][idy] != game.blank:
            print()
            
button = ttk.Button(window, text="Change the first row/col", command=flip)
button1 = ttk.Button(window, text="Start")
button.grid(column= 0,row = 11)
button1.grid(column=1,row=11)

window.mainloop()