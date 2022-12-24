# included libraries
import os
import platform
import time
import json
from Cogs.functions import *


# -----------------------------------------
# --- list of all menus
# -----------------------------------------
menu1 = ['Play', 'Tutorial', 'Scoreboard', 'Exit']
menu2 = ['Diamond', 'Circle', 'Triangle (please don\'t)', 'Back', 'Exit']
menu3 = ['Size 1', 'Size 2', 'Size 3', 'Back', 'Exit']
menu4 = ['Display 3 random blocs', 'Display all blocs', 'Back', 'Exit']


# -----------------------------------------
# --- Game Over Screen
# -----------------------------------------
def gameOver(score, best):
    print(f"\n\n  GAME OVER\nFinal Score: {score}\nBest Score: {best}")
    time.wait(5)


# -----------------------------------------
# --- Print Menu
# -----------------------------------------
def pMenu(menu, msg=None):
    clear()
    if msg!=None: print(msg)
    for index, item in enumerate(menu): print(f"{index+1}]- {item}")
    req = secInput("Choice: ")
    return req if (req > 0 and req<=(len(menu))) else pMenu(menu, msg)


# -----------------------------------------
# --- Welcome Screen
# -----------------------------------------
def welcomeScreen():
    clear()
    print("\n\nTEXT-TRIS")
    time.sleep(2)
    # mainMenu()  # redirects to the mainMenu() function


# -----------------------------------------
# --- Exit Screen
# -----------------------------------------
def exitScreen():
    clear()
    print("\n\nTHANKS 4 PLAYING")
    time.sleep(2)
    exit(0)


# -----------------------------------------
# --- Main Menu
# -----------------------------------------
def mainMenu():
    clear()
    # print("PLAY\n")
    choice=pMenu(menu1)
    match choice:
        case 1: return gridTypeMenu()
        case 2: return tutorialScreen()
        case 4: exitScreen()
        case _: return mainMenu()


# -----------------------------------------
# --- Tutorial Screen
# -----------------------------------------
def tutorialScreen():
    clear()
    print("this is a tutorial")
    input("press enter to go back to the main menu")
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
    if gsize!=None: blocMenu()


# -----------------------------------------
# --- Bloc Display Menu
# -----------------------------------------
def blocMenu():
    global bdisplay
    clear()
    choice=pMenu(menu4, msg="Choose how you want the next bloc(s) to be displayed:")
    match choice:
        case 1: bdisplay = 1
        case 2: bdisplay = 2
        case 3: return gridSizeMenu()
        case 4: return exitScreen()
        case _: return blocMenu()


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
    # print(f"type: {gtype}\nsize: {gsize}\nbloc display: {bdisplay}")
    return gtype, gsize, bdisplay