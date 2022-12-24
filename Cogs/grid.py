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
get_grid = lambda gtype, gsize: json.load(open(f'data/{gtype}.json'))[f"{gsize}"]


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
def check_grid(a, score):
    for i in range((len(a) - 1), -1, -1): score += 1 if all(item==0 or item==2 for item in a[i]) else 0
    for i in range((len(a) - 1), -1, -1):
        # for j in range(len(a[i])):
        if  all(item == 0 or item == 2 for item in a[i]):
            for k in range(i, -1, -1):
                for l in range(len(a[k])):
                    if a[k-1][l] == 0 and a[k][l]==2: a[k][l]=1
                    elif a[k-1][l] == 1 and a[k][l]==2: a[k][l]=1
                    elif a[k-1][l] == 2 and a[k][l]==1: a[k][l]=2
    return a, score


# -----------------------------------------
# --- Add block to grid
# -----------------------------------------
def add_block(ogrid, block):
    cgrid = ogrid
    size = len(ogrid[0])
    x, y = get_coords(size)
    x-=1; y-=1; k = len(block)-1; l = 0
    while k > -1:
        for i in range((len(cgrid) - 1), -1, -1):
            if k == -1: break
            l = 0
            if i <= y and i >= 0:
                for j in range(len(cgrid[i])):
                    if len(block) > 1:
                        if j >= x and j <= (x + len(block[0]) - 1):
                            # print(i, j, k, l)
                            if cgrid[i][j]==0 and block[k][l]!=0: raise InvalidBlockPos
                            else: cgrid[i][j]+=block[k][l]
                            # cgrid[i][j]+=block[k][l]
                            if l < (len(block[0]) - 1):
                                l += 1
                    else:
                        if j >= x and j <= (x + len(block[k]) - 1):
                            # print(i, j, k, l)
                            if cgrid[i][j]==0 and block[k][l]!=0: raise InvalidBlockPos
                            else: cgrid[i][j]+=block[k][l]
                            # cgrid[i][j]+=block[k][l]
                            if l <= len(block[0]):
                                l += 1
                    if cgrid[i][j]>2:
                        print(down[i], top[j])
                        cgrid[i][j] = 1
                        raise BlockOverlap
                k-=1
    return cgrid


# -----------------------------------------
# --- Display the blocks
# -----------------------------------------
def display_blocks(block_list):
    arrays = [[[' ' if x == 0 else '■' for x in i] for i in array] for array in block_list]
    line = 0
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
    grid, current_score = check_grid(grid, current_score)
    # clear the terminal
    clear()
    # transform the grid into symbols
    d_grid = [[' ' if x == 0 else ('■' if x == 2 else '∙') for x in i] for i in grid]
    # display the grid in the terminal
    # for i in range(0, len(grid)): print(*d_grid[i], sep=" ", end="\n")
    print("     ", end="")
    for i in range(0, len(d_grid[0])):
        if i==len(d_grid[0])-1: print(top[i], end=f"\t\tYour Score: {current_score}\n")
        else: print(top[i], end=" ")
    print("  |‾‾", end="")
    for i in range(0, len(d_grid[0])):
        if i==len(d_grid[0])-1: print(topline[i], end=f"‾‾|\t\tBest Score: {best_score}\n")
        else: print(topline[i], end="‾")
    for i in range(0, len(d_grid)):
        a = i
        print(down[i], end=" ")
        print("|", end="  ")
        print(*d_grid[i], sep=" ", end="  |\n")
        # print("|")
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
    else: return show_grid(grid, sample, current_score, best_score)