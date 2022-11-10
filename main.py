# from tetris import game
from Cogs.grid import show_grid
import os

if __name__=="__main__":
    try:
        os.system("cls")
    except:
        os.system("clear")
    # tetris.run()
    show_grid()