# included libraries
from Cogs.menus import *
from Cogs.grid import *
from Cogs.functions import *
import time


# -----------------------------------------
# --- Player Class
# -----------------------------------------
class Player():
    def __init__(self) -> None:
        self.lives = 3
        self.dead = False
        self.score = 0
        with open("data/player.json", 'r') as f: self.best = json.load(f)["best"]

    def decrease(self):
        self.lives -= 1
        if self.lives == 0: self.dead = True
    
    def update(self, score):
        if score > self.best:
            with open("data/player.json", 'w') as f: json.dump({"best":score}, f, indent=4)



# -----------------------------------------
# --- Variables
# -----------------------------------------
grid_type=None ; grid_size=None ; bloc_display=None


# -----------------------------------------
# --- Play Function
# -----------------------------------------
def play(g, s, user):
    g_copy = g.copy()
    chosen_block = show_grid(g_copy, s, user.score, user.best)
    g_copy, error, user.score = add_block(g_copy, chosen_block, user.score)
    if error == 0:
        play(g_copy, s, user)
    else:
        user.decrease()
        if user.lives>0:
            input(f"You have lost one life\nLives remaining {user.lives}/3\nPress enter to keep playing")
            play(g, s, user)
        else:
            return
            # exit(0)


# -----------------------------------------
# --- Get the Game Data
# -----------------------------------------
def getGameData():
    # grid_type, grid_size, bloc_display = ("diamond", 1, 1)
    grid_type, grid_size, bloc_display = display_menu()
    # var_display=f"\n   type: {grid_type}\n   size: {grid_size}\n   display: {bloc_display}"; print("mdata: {", var_display, "\n   }\n")
    grid = get_grid(grid_type, grid_size)
    sample_size = 3 if bloc_display == 1 else 10
    return grid, sample_size


if __name__=="__main__":
    welcomeScreen()
    while True:
        clear()
        grid, sample = getGameData()
        p = Player()
        play(grid, sample, p)
        if p.dead==True:
            p.update(p.score)
            clear()
        gameOver(p.score, p.best)

    # display_blocks([[chosen_block]])
    # singleBlock(chosen_block)
