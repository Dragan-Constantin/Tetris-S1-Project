# included libraries
from Cogs.menus import display_menu, gameOver
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
        with open("data/player.json", 'r') as f: self.best = json.load(f)["Best"]

    def decrease(self):
        self.lives -= 1
        if self.lives == 0: self.dead = True
    
    def update(self):
        if self.best > self.score:
            with open("data/player.json", 'r') as f: data = json.load(f)
            data["Best"] = self.score
            with open("data/player.json", 'w') as f: json.dump(data, f, index=4)


# -----------------------------------------
# --- Variables
# -----------------------------------------
grid_type=None ; grid_size=None ; bloc_display=None


# -----------------------------------------
# --- Play Function
# -----------------------------------------
def play(g, s, score, best):
    chosen_block = show_grid(g, s, score, best)
    g_copy = g
    try: g_copy = add_block(g_copy, chosen_block)
    except (InvalidBlockPos, BlockOverlap) as e:
        print(e)
        p.decrease()
        if p.lives>0:
            input(f"You have lost one life\nLives remaining {p.lives}/3\nPress enter to keep playing")
            play(g, s, score, best)
        else:
            if p.dead==True: clear()
            gameOver()
            return
            # exit(0)
    score +=1
    play(g, s, score, best)


# -----------------------------------------
# --- Get the Game Data
# -----------------------------------------
def getGameData():
    # grid_type, grid_size, bloc_display = ("diamond", 3, 1)
    grid_type, grid_size, bloc_display = display_menu()
    # var_display=f"\n   type: {grid_type}\n   size: {grid_size}\n   display: {bloc_display}"; print("mdata: {", var_display, "\n   }\n")
    grid = get_grid(grid_type, grid_size)
    sample_size = 3 if bloc_display == 1 else 10
    return grid, sample_size


if __name__=="__main__":
    while True:
        clear()
        grid, sample = getGameData()
        p = Player()
        play(grid, sample, p.score, p.best)


    # display_blocks([[chosen_block]])
    # singleBlock(chosen_block)
