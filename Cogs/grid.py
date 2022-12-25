"""
This module regroups multiple functions used throughout the project.
It is responsible for processing and displaying the game grid and blocks.
It was created as part of a class project given to the first year
students (L1) at EFREI Paris on november 2022.

It will NOT be maintained by the authors.

__authors__ = "Dragan Constantin (EFREI Promo 2027), Somphone Isabelle (EFREI Promo 2027)"
__copyright__ = "Copyright (c) 2022 Dragan Constantin and Somphone Isabelle"
__license__ = "MIT"
__emails__ = ["constantin.dragan@efrei.net", "isabelle.somphone@efrei.net"]
"""


# included libraries
import string
import json
import random
from Cogs.functions import *


# -----------------------------------------
# --- Variables
# -----------------------------------------
top = string.ascii_lowercase #: The list of all lowercase letters.
down = string.ascii_uppercase #: The list of all uppercase letters.
topline = ["‾" for i in range(100)] #: A list of 100 "‾" used for decorative purposes in show_grid().


# -----------------------------------------
# --- Custom Errors
# -----------------------------------------
class InvalidBlockPos(Exception):
    """Raised when the block placed ends up out of bounds"""
    def __str__(self):
        return "The block you placed is out of bounds."

class BlockOverlap(Exception):
    """Raised when two blocks are overlapping"""
    def __str__(self):
        return "The block you placed is overlapping with another block."


# -----------------------------------------
# --- Get the grid
# -----------------------------------------
"""
@var gtype: The type of the grid.
@var gsize: The size of the grid.
"""
get_grid = lambda gtype, gsize: json.load(open(f'data/grids.json'))[f"{gtype}"][f"{gsize}"]


# -----------------------------------------
# --- Get the Block List
# -----------------------------------------
"""@var gtype: The type of the grid."""
getBlockList = lambda gtype: json.load(open(f'data/block_list.json'))["any"] + json.load(open(f'data/block_list.json'))[f"{gtype}"]


# -----------------------------------------
# --- Get block coordinates
# -----------------------------------------
def get_coords(gsize):
    """
    Gets the coordinates at which the player wants to
    place the bottom left corner of the chosen block.

    @var x, y: The x and y coordinates chosen by the player.
    """
    print("Please enter x and y coordinates (column and line) on which you want to put your block.)")
    print("Caution: it must be for the bottom left corner of the block")
    x, y = choiceInput("x: "), choiceInput("y: ")
    if 0<x<=gsize and 0<y<=gsize: return x, y #: checks if x and y are valid coordinates to prevent IndexError
    else: return get_coords(gsize)


# -----------------------------------------
# --- Check if line is full
# -----------------------------------------
def check_grid(a, s):
    """
    Checks whether or not a line is full.
    If there is none, it will simply return the grid as is.
    Else, it will reset the line and update the grid accordingly.
    
    @param a: The grid to be checked.
    @param s: The current score of the player.

    @var check: Status of the line (full or not).
    @var full: The index of the full line.
    """
    check=False
    #: iterates over each line of the grid from bottom to top. Ensures every line another time after the grid was modified.
    for line in range(len(a)-1, -1, -1):
        for i in range(len(a)-1, -1, -1): #: iterates over each line of the grid from bottom to top.
            if all(item == 0 or item == 2 for item in a[i]): #: checks if the line contains only 2s and 0s.
                check, full = True, i #: sets check full to the current index.
                s+=(a[i].count(2)) #: adds to the score the number of 2s in the line.
            
            if check==True:
                if i<len(a)-1: #: checks if 'i' is not above the last line's index.
                    
                    for j in range(len(a[i])): #: iterates over the elements of each line.
                        
                        if i==full: #: if it is the full line.
                            if a[i+1][j]==0 and a[i][j]==2: #: if the element under is out of bounds and this one is part of a block:
                                a[i][j]=1 #: resets the element to an empty line.
                            elif a[i+1][j]==2 and a[i][j]==2: #: if both this element and the one under are parts of blocks:
                                a[i][j]=1 #: resets the element to an empty line.
                            elif a[i+1][j]==1 and a[i][j]==2: #: if the element under is empty and this one is part of a block:
                                a[i+1][j]=1 ; a[i][j]=1 #: Both this element and the one under become an empty line.
                        
                        if i!=full: #: if it is not the full line.
                            if a[i+1][j]==0 and a[i][j]==2: #: if the element under is out of bounds and this one is part of a block:
                                a[i][j]=2 #: element becomes a block.
                            elif a[i+1][j]==1 and a[i][j]==2: #: if the element under is empty and this one is part of a block:
                                a[i+1][j]=2 ; a[i][j]=1 #: The one under becomes a block and this one becomes an empty line.
                
                elif i==(len(a)-1): #: checks if 'i' is the last line index.
                    for j in range(len(a[i])): #: iterates over the elements of each line.
                        if a[i][j]==2: a[i][j]=1 #: resets the element to an empty line if it is a block.
        check=False
    return a, s


# -----------------------------------------
# --- Add block to grid
# -----------------------------------------
def add_block(ogrid, block, score):
    """
    Checks whether or not a block can be added.
    It will then do so if enabled before checking if the line is full.

    @param ogrid: The grid to be checked.
    @param block: The block to be placed.
    @param score: The current score of the player.

    @var cgrid: A copy of ogrid.
    @var size: The size of the line in the grid.
    @var x, y: The x and y coordinates chosen by the player.
    @var k, l: Are used to respectively iterate over the lines of a block and over each element of said lines.
    @var i, j: Are used to respectively iterate over the lines of the grid and over each element of said lines.

    @raise InvalidBlockPos: Error raised when the block is placed out of bounds.
    @raise BlockOverlap: Error raised when the block is overlapping another previously placed block.
    """
    cgrid = ogrid.copy()
    size = len(cgrid[0])
    x, y = get_coords(size)
    x-=1; y-=1 #: substract 1 to x and y to get valid values for indexes.
    k = len(block)-1
    l = 0
    try:
        while k > -1: #: Prevents putting part of a block at the top and the rest at the bottom.
            for i in range((len(cgrid)-1), -1, -1): #: iterate from bottom to top over the grid
                if k == -1: break
                l = 0
                if i <= y and i >= 0:
                    for j in range(len(cgrid[i])):
                        if len(block) > 1:
                            if j >= x and j <= (x + len(block[0]) - 1):
                                if cgrid[i][j]==0 and block[k][l]!=0: raise InvalidBlockPos #: if the block is out of bounds
                                else: cgrid[i][j]+=block[k][l]
                                if l < (len(block[0]) - 1): l += 1
                        else:
                            if j >= x and j <= (x + len(block[0]) - 1):
                                if cgrid[i][j]==0 and block[k][l]!=0: raise InvalidBlockPos #: if the block is out of bounds
                                else: cgrid[i][j]+=block[k][l]
                                if l <= len(block[0]): l += 1
                        if cgrid[i][j]>2:
                            cgrid[i][j] = 2
                            raise BlockOverlap #: if the block is overlapping with an already present block.
                    k-=1
        res, score = check_grid(cgrid.copy(), score) #: check if the line is full
        return res, 0, score
    except (InvalidBlockPos, BlockOverlap) as e:
        print(e) #: print the error message
        return ogrid, 1, score


# -----------------------------------------
# --- Display the blocks
# -----------------------------------------
def display_blocks(block_list):
    """
    Displays the blocks among a list of blocks to the player.

    @param block_list: The list of blocks to be displayed.

    @var arrays: The a modified version of block_list containing ■ and blank spaces.
    @var lmax: The maximum length of a line in a block.
    @var array: A block.
    """
    arrays = [[[' ' if x == 0 else '■' for x in i] for i in array] for array in block_list]
    lmax = max(len(array) for array in arrays)
    for line in range(lmax):
            for array in arrays:
                try:
                    print(*array[line], sep=' ', end='   ')
                except IndexError:
                    print('  ' * len(array[0]), end='  ')
            print()


# -----------------------------------------
# --- Display Grid
# -----------------------------------------
def show_grid(grid, sample, current_score, best_score):
    """
    Displays the full grid to the player along with their score and the best score.
    It will also display the blocks for them to choose from and prompt them to select one
    before return the chosen block.

    @param grid: The grid to be displayed.
    @param sample: The sample size.
    @param current_score: The current score of the player.
    @param best_score: The best score on file.

    @var sgrid: A copy of the grid.
    @var d_grid: A modified version of sgrid where 0s are blank spaces, 1s are '∙' and 2s are '■'.
    @var dBlocks: A sample of blocks among all possible blocks and of size=sample.
    @var blockId: The index of the block chosen by the player (between 1 and sample).
    """

    clear() #: clear the terminal
    sgrid = grid.copy()
    d_grid = [[' ' if x == 0 else ('■' if x == 2 else '∙') for x in i] for i in sgrid] #: Transform the grid of 2s, 1s and 0s into a grid of symbols.

    #: Display the grid in the terminal.
    print("     ", end="")
    for i in range(0, len(d_grid[0])): #: Print the whole ordinate section.
        if i==len(d_grid[0])-1: print(top[i], end=f"\t\t\tYour Score: {current_score}\n")
        else: print(top[i], end=" ")
    print("  |‾‾", end="")
    for i in range(0, len(d_grid[0])): #: Print the top part of the frame.
        if i==len(d_grid[0])-1: print(topline[i], end=f"‾‾|\t\tBest Score: {best_score}\n")
        else: print(topline[i], end="‾")
    for i in range(0, len(d_grid)): #: Print each line of the grid.
        print(down[i], end=" ") #: Print abscissa section.
        print("|", end="  ")
        print(*d_grid[i], sep=" ", end="  |\n")
    print("  |", end="")
    for i in range(0, len(d_grid[0])): print("  ", end="")
    print("   |")
    print("   ‾‾", end="")
    for i in range(0, len(d_grid[0])): #: Print the bottom part of the frame.
        if i==len(d_grid[0])-1: print(topline[i], end="‾‾\n")
        else: print(topline[i], end="‾")

    dBlocks = random.sample(getBlockList("diamond"), sample)
    display_blocks(dBlocks)
    blockId = secInput("\nChoose a block among the following (1 being the first on the left)\nChoice: ")
    if 0 < blockId <= sample: return dBlocks[blockId - 1] #: Return the chosen block if its index exists.
    else: return show_grid(grid, sample, current_score, best_score)
