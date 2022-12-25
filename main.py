"""
This is a Tetris® like puzzle game with a Terminal User Interface.
It was created as part of a class project given to the first year
students (L1) at EFREI Paris on november 2022.

It will NOT be maintained by the authors.

__authors__ = "Dragan Constantin (EFREI Promo 2027), Somphone Isabelle (EFREI Promo 2027)"
__copyright__ = "Copyright (c) 2022 Dragan Constantin and Somphone Isabelle"
__license__ = "MIT"
__version__ = "1.0.0"
__emails__ = ["constantin.dragan@efrei.net", "isabelle.somphone@efrei.net"]
"""


# included libraries
from Cogs.menus import *
from Cogs.grid import *
from Cogs.functions import *
import sys


# -----------------------------------------
# --- Player Class
# -----------------------------------------
class Player():
    def __init__(self) -> None:
        """
        @ivar lives: Current number of lives the player has.
        @ivar dead: Status of the player.
        @ivar score: Current score.
        @ivar best: Best score on file.
        """
        self.lives = 3
        self.dead = False
        self.score = 0
        with open("data/player.json", 'r') as f: self.best = json.load(f)["best"]

    def decrease(self):
        self.lives -= 1
        if self.lives == 0: self.dead = True
    
    def update(self, score):
        """
        @var score: Current score.
        """
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
    """
    @param g: The current grid.
    @param s: The sample size.
    @param user: An instance of the Player class.

    @var g_copy: A copy of the 3D array 'g'.
    @var chosen_block: The block chosen by the user among the sample.
    @var error: A boolean showing whether or not an error was raised.
    """
    g_copy = g.copy()
    chosen_block = show_grid(g_copy, s, user.score, user.best)
    g_copy, error, user.score = add_block(g_copy, chosen_block, user.score)
    
    if error == 0: #: if no error: loop over with updated grid.
        play(g_copy, s, user)
    else:
        user.decrease() #: decrease lives counter by 1.
        if user.lives>0:
            input(f"You have lost one life\nLives remaining {user.lives}/3\nPress enter to keep playing")
            play(g, s, user) #: loop over with previous grid.
        else: #: if player is dead, exit the play() function.
            return None


# -----------------------------------------
# --- Get the Game Data
# -----------------------------------------
def getGameData():
    """
    @var grid_type: The type of the grid.
    @var grid_size: The size of the grid.
    @var sample_size: The size of the sample.
    @var grid: The selected grid
    """
    grid_type, grid_size, sample_size = display_menu()
    grid = get_grid(grid_type, grid_size)
    return grid, sample_size


if __name__=="__main__":
    cli = sys.argv #: gets the command line input from the terminal.
    if len(cli)>=2: #: checks whether or not it should display the welcome screen.
        if cli[1]=="True": welcomeScreen()
    else: welcomeScreen()
    while True:
        clear()
        grid, sample = getGameData() #: gets the grid and sample size data
        p = Player() #: initialise the player
        play(grid, sample, p) #: begin to play
        if p.dead==True:
            p.update(p.score) #: update the current player score
            clear()
        gameOver(p.score, p.best) #: shows the gameOver screen