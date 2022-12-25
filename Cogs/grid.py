# included libraries
import string
import json
import random
from Cogs.functions import *


# -----------------------------------------
# --- Variables
# -----------------------------------------
top = string.ascii_lowercase
down = string.ascii_uppercase
topline = ["‾", "‾", "‾", "‾", "‾", "‾", "‾", "‾", "‾", "‾", "‾", "‾", "‾", "‾", "‾", "‾", "‾", "‾", "‾", "‾", "‾", "‾", "‾", "‾", "‾"]


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
get_grid = lambda gtype, gsize: json.load(open(f'data/grids.json'))[f"{gtype}"][f"{gsize}"]


# -----------------------------------------
# --- Get the Block List
# -----------------------------------------
getBlockList = lambda gtype: json.load(open(f'data/block_list.json'))["any"] + json.load(open(f'data/block_list.json'))[f"{gtype}"]


# -----------------------------------------
# --- Get block coordinates
# -----------------------------------------
def get_coords(gsize):
    print("Please enter x and y coordinates (column and line) on which you want to put your block.\nCaution: it must be for the bottom left corner of the block")
    x, y = choiceInput("x: "), choiceInput("y: ")
    if 0<x<=gsize and 0<y<=gsize: return x, y
    else: return get_coords(gsize)


# -----------------------------------------
# --- Check if line is full
# -----------------------------------------
def check_grid(a, s):
    check=False
    for line in range(len(a)-1, -1, -1):
        for i in range(len(a)-1, -1, -1):
            if all(item == 0 or item == 2 for item in a[i]):
                check, full = True, i ; s+=(a[i].count(2))
            if check==True:
                if i<len(a)-1:
                    for j in range(len(a[i])):
                        if i==full:
                            if a[i+1][j]==0 and a[i][j]==2:
                                a[i][j]=1
                            elif a[i+1][j]==2 and a[i][j]==2:
                                a[i][j]=1
                            elif a[i+1][j]==1 and a[i][j]==2:
                                a[i+1][j]=1 ; a[i][j]=1
                        if i!=full:
                            if a[i+1][j]==0 and a[i][j]==2:
                                a[i][j]=2
                            elif a[i+1][j]==2 and a[i][j]==2:
                                a[i+1][j]=2 ; a[i][j]=2
                            elif a[i+1][j]==1 and a[i][j]==2:
                                a[i+1][j]=2 ; a[i][j]=1
                elif i==(len(a)-1):
                    for j in range(len(a[i])):
                        if a[i][j]==2: a[i][j]=1
        check=False
    return a, s


# -----------------------------------------
# --- Add block to grid
# -----------------------------------------
def add_block(ogrid, block, score):
    cgrid = ogrid.copy()
    size = len(cgrid[0])
    x, y = get_coords(size)
    x-=1; y-=1; k = len(block)-1; l = 0
    try:
        while k > -1:
            for i in range((len(cgrid)-1), -1, -1):
                if k == -1: break
                l = 0
                if i <= y and i >= 0:
                    for j in range(len(cgrid[i])):
                        if len(block) > 1:
                            if j >= x and j <= (x + len(block[0]) - 1):
                                if cgrid[i][j]==0 and block[k][l]!=0: raise InvalidBlockPos
                                else: cgrid[i][j]+=block[k][l]
                                if l < (len(block[0]) - 1):
                                    l += 1
                        else:
                            if j >= x and j <= (x + len(block[0]) - 1):
                                if cgrid[i][j]==0 and block[k][l]!=0: raise InvalidBlockPos
                                else: cgrid[i][j]+=block[k][l]
                                if l <= len(block[0]):
                                    l += 1
                        if cgrid[i][j]>2:
                            cgrid[i][j] = 2
                            raise BlockOverlap
                    k-=1
        res, score = check_grid(cgrid.copy(), score)
        return res, 0, score
    except (InvalidBlockPos, BlockOverlap) as e:
        print(e)
        return ogrid, 1, score


# -----------------------------------------
# --- Display the blocks
# -----------------------------------------
def display_blocks(block_list):
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
    sgrid = grid.copy()
    # clear the terminal
    clear()
    # transform the grid into symbols
    d_grid = [[' ' if x == 0 else ('■' if x == 2 else '∙') for x in i] for i in grid]
    # display the grid in the terminal
    print("     ", end="")
    for i in range(0, len(d_grid[0])):
        if i==len(d_grid[0])-1: print(top[i], end=f"\t\t\tYour Score: {current_score}\n")
        else: print(top[i], end=" ")
    print("  |‾‾", end="")
    for i in range(0, len(d_grid[0])):
        if i==len(d_grid[0])-1: print(topline[i], end=f"‾‾|\t\tBest Score: {best_score}\n")
        else: print(topline[i], end="‾")
    for i in range(0, len(d_grid)):
        print(down[i], end=" ")
        print("|", end="  ")
        print(*d_grid[i], sep=" ", end="  |\n")
    print("  |", end="")
    for i in range(0, len(d_grid[0])): print("  ", end="")
    print("   |")
    print("   ‾‾", end="")
    for i in range(0, len(d_grid[0])):
        if i==len(d_grid[0])-1: print(topline[i], end="‾‾\n")
        else: print(topline[i], end="‾")

    dBlocks = random.sample(getBlockList("diamond"), sample)
    display_blocks(dBlocks)
    blockId = secInput("\nChoose a block among the following (1 being the first on the left)\nChoice: ")
    if 0 < blockId <= sample: return dBlocks[blockId - 1]
    else: return show_grid(sgrid, sample, current_score, best_score)
