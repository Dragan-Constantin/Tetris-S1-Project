# included libraries
import time
import json
from Cogs.functions import *


# -----------------------------------------
# --- list of all menus and variables
# -----------------------------------------
menu1 = ['Play', 'Tutorial', 'Scoreboard', 'Exit']
menu2 = ['Diamond', 'Circle', 'Triangle', 'Back', 'Exit']
menu3 = ['Small', 'Medium', 'Large', 'Back', 'Exit']
menu4 = ['Display 3 random blocs', 'Display all blocs', 'Back', 'Exit']
title = """
     /\‾‾\         /\‾‾\         /\‾‾\         /\‾‾\                     /\‾‾\    
     \:\  \       /::\  \        \:\  \       /::\  \        /\‾‾\      /::\  \   
      \:\  \     /:/\:\  \        \:\  \     /:/\:\  \       \:\  \    /:/\ \  \  
      /::\  \   /::\‾\:\  \       /::\  \   /::\‾\:\  \      /::\__\  _\:\‾\ \  \ 
     /:/\:\__\ /:/\:\ \:\__\     /:/\:\__\ /:/\:\ \:\__\  __/:/\/__/ /\ \:\ \ \__\\
    /:/  \/__/ \:\‾\:\ \/__/    /:/  \/__/ \/_|::\/:/  / /\/:/  /    \:\ \:\ \/__/
   /:/  /       \:\ \:\__\     /:/  /         |:|::/  /  \::/__/      \:\ \:\__\  
   \/__/         \:\ \/__/     \/__/          |:|\/__/    \:\__\       \:\/:/  /  
                  \:\__\                      |:|  |       \/__/        \::/  /   
                   \/__/                       \|__|                     \/__/    
 """
small_title = """
   /\‾‾\     /\‾‾\     /\‾‾\     /'\‾‾\     /\‾‾\     /\‾‾\  
   \ \  \   /  \  \    \ \  \   /   \  \   _\ \  \   /  \  \ 
   /  \__\ /  \ \__\   /  \__\ /  /\ \__\ /\/  \__\ /\ \ \__\\
  / /\/__/ \ \ \/  /  / /\/__/ \/\\\/ /  / \  /\/__/ \ \ \/__/
 / /  /     \ \/  /  / /  /      |  /__/   \ \__\    \  /  / 
 \/__/       \/__/   \/__/        \|__|     \/__/     \/__/  
 """
game = """    ___       ___       ___       ___            ___       ___       ___        ___   
   /\  \     /\  \     /\__\     /\  \          /\  \     /\__\     /\  \     /'\  \  
  /  \  \   /  \  \   / |_ |_   /  \  \        /  \  \   / / _/_   /  \  \   /   \  \ 
 / /\ \__\ /  \ \__\ / /L \__\ /  \ \__\      / /\ \__\ |  L/\__\ /  \ \__\ /  /\ \__\\
 \ \ \/__/ \/\  /  / \/_/ /  / \ \ \/  /      \ \/ /  / |    /  / \ \ \/  / \/\\\/ /  /
  \  /  /    / /  /    / /  /   \ \/  /        \  /  /  |___/__/   \ \/  /    | \/__/ 
   \/__/     \/__/     \/__/     \/__/          \/__/               \/__/      \|__|  
 """
thx = """
         ___       ___       ___       ___       ___       ___        
        /\  \     /\__\     /\  \     /\__\     /\__\     /\  \       
        \:\  \   /:/__/_   /::\  \   /:| _|_   /:/ _/_   /::\  \      
        /::\__\ /::\/\__\ /::\:\__\ /::|/\__\ /::-"\__\ /\:\:\__\     
       /:/\/__/ \/\::/  / \/\::/  / \/|::/  / \;:;-",-" \:\:\/__/     
       \/__/      /:/  /    /:/  /    |:/  /   |:|  |    \::/  /      
                  \/__/     \/__/     \/__/     \|__|     \/__/       
                        ___       ___       ___                       
                       /\  \     /\  \     /\  \                      
                      /::\  \   /::\  \   /::\  \                     
                     /::\:\__\ /:/\:\__\ /::\:\__\                    
                     \/\:\/__/ \:\/:/  / \;:::/  /                    
                        \/__/   \::/  /   |:\/__/                     
                                 \/__/     \|__|                      
    ___       ___       ___       ___       ___       ___       ___   
   /\  \     /\__\     /\  \     /\__\     /\  \     /\__\     /\  \  
  /::\  \   /:/  /    /::\  \   |::L__L   _\:\  \   /:| _|_   /::\  \ 
 /::\:\__\ /:/__/    /::\:\__\  |:::\__\ /\/::\__\ /::|/\__\ /:/\:\__\\
 \/\::/  / \:\  \    \/\::/  /  /:;;/__/ \::/\/__/ \/|::/  / \:\:\/__/
    \/__/   \:\__\     /:/  /   \/__/     \:\__\     |:/  /   \::/  / 
             \/__/     \/__/               \/__/     \/__/     \/__/  
"""

# -----------------------------------------
# --- Game Over Screen
# -----------------------------------------
def gameOver(score, best):
    print(f"\n\n{game}\nFinal Score: {score}\nBest Score: {best}")
    time.sleep(5)


# -----------------------------------------
# --- Print Menu
# -----------------------------------------
def pMenu(menu, msg=None):
    clear()
    print(small_title)
    if msg!=None: print(msg)
    for index, item in enumerate(menu): print(f"{index+1}]- {item}")
    req = secInput("Choice: ")
    return req if (req > 0 and req<=(len(menu))) else pMenu(menu, msg)


# -----------------------------------------
# --- Welcome Screen
# -----------------------------------------
def welcomeScreen():
    clear()
    print(title)
    time.sleep(2)


# -----------------------------------------
# --- Exit Screen
# -----------------------------------------
def exitScreen():
    clear()
    print(f"\n\n{thx}\n")
    time.sleep(2)
    clear()
    exit(0)


# -----------------------------------------
# --- Main Menu
# -----------------------------------------
def mainMenu():
    clear()
    choice=pMenu(menu1)
    match choice:
        case 1: return gridTypeMenu()
        case 2: return tutorialScreen()
        case 3: return scoreboardScreen()
        case 4: exitScreen()
        case _: return mainMenu()


# -----------------------------------------
# --- Tutorial Screen
# -----------------------------------------
def tutorialScreen():
    clear()
    print(small_title)
    print("""\n
This is a Tetris® like game.
On play, you will be given the opportunity to choose different options for 3 kinds of parameters:
the type of the grid, its size, and finally how you want the blocks to choose from to be displayed.

Then the game will start and you'll have to choose between a selection of blocks to place. Once you
have chosen, you will be prompted to give its placement coordinates. Beware, for the coordinates
correspond to the bottom left part of the block.

If the block can indeed be placed at those coordinates and that the line becomes full,
said line will be cleared, the blocks on top will fall down by one line and your score
will increase by the number of blocks you have cleared.

If the block is even partially outside of bounds, you will lose one life out of the three you began
with. The same applies if the block you wish to place is superposed in any way with a block that is
already present on the grid.

Once you reach 0 life, the game is over.
""")
    input("\npress enter to go back to the main menu")
    mainMenu()


# -----------------------------------------
# --- ScoreBoard Screen
# -----------------------------------------
def scoreboardScreen():
    clear()
    print(small_title)
    with open("data/player.json", 'r') as f: print(f"\n\nHere is the current best score: {json.load(f)['best']}")
    input("\npress enter to go back to the main menu")
    mainMenu()


# -----------------------------------------
# --- Grid Type Menu
# -----------------------------------------
def gridTypeMenu():
    global gtype
    clear()
    choice=pMenu(menu2, msg="Choose a grid type:")
    match choice:
        case 1: gtype = "diamond"
        case 2: gtype = "circle"
        case 3: gtype = "triangle"
        case 4: return mainMenu()
        case 5: return exitScreen()
        case _: return gridTypeMenu()
    if gtype!=None: gridSizeMenu()


# -----------------------------------------
# --- Grid Size Menu
# -----------------------------------------
def gridSizeMenu():
    global gsize
    clear()
    choice=pMenu(menu3, msg="Choose a grid size:")
    match choice:
        case 1: gsize = 1
        case 2: gsize = 2
        case 3: gsize = 3
        case 4: return gridTypeMenu()
        case 5: return exitScreen()
        case _: return gridSizeMenu()
    if gsize!=None: blockMenu()


# -----------------------------------------
# --- Bloc Display Menu
# -----------------------------------------
def blockMenu():
    global bdisplay
    clear()
    choice=pMenu(menu4, msg="Choose how you want the next bloc(s) to be displayed:")
    match choice:
        case 1: bdisplay = 3
        case 2: bdisplay = 10
        case 3: return gridSizeMenu()
        case 4: return exitScreen()
        case _: return blockMenu()


# -----------------------------------------
# --- Display the Whole Menu  (+return choices)
# -----------------------------------------
def display_menu():
    global gtype
    global gsize
    global bdisplay
    gtype, gsize, bdisplay = None, None, None
    mainMenu()
    clear()
    return gtype, gsize, bdisplay
