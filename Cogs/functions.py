"""
This module regroups multiple functions used throughout the project.
It was created as part of a class project given to the first year
students (L1) at EFREI Paris on november 2022.

It will NOT be maintained by the authors.

__authors__ = "Dragan Constantin (EFREI Promo 2027), Somphone Isabelle (EFREI Promo 2027)"
__copyright__ = "Copyright (c) 2022 Dragan Constantin and Somphone Isabelle"
__license__ = "MIT"
__emails__ = ["constantin.dragan@efrei.net", "isabelle.somphone@efrei.net"]
"""


# included libraries
import os
import platform
import string


# -----------------------------------------
# --- Custom Errors
# -----------------------------------------
class InvalidInput(Exception):
    """Raised when the given input is invalid"""
    def __str__(self):
        return "Invalid Input."


# -----------------------------------------
# --- Clear Function (works on most types of OS)
# -----------------------------------------
"""Clears the terminal with the appriopriate command depending the user's OS."""
clear = lambda: os.system("cls" if platform.system()=="Windows" else "clear")



# -----------------------------------------
# --- Secured Inputs
# -----------------------------------------
def secInput(msg: str) -> int:
    """Prompts the user for an input. If any error is raised, it return -1."""
    try: return int(input(msg))
    except (TypeError, ValueError): return -1


def choiceInput(msg: str) -> int:
    """
    Prompts the user for an input, checks if the lowercase version of the letter is the list of ascii lowercase character.
    Then, it will return the index of said ascii character in the list.
    If any error is raised, it return -1.
    
    @var a: The user input.
    """
    try:
        a = input(msg)
        if a.lower() in string.ascii_lowercase: return string.ascii_lowercase.index(a.lower())+1
        else: raise InvalidInput
    except (TypeError, ValueError, InvalidInput): return -1


# -----------------------------------------
# --- Display Single Block
# -----------------------------------------
def singleBlock(block):
    """
    Used for testing, has no purpose in the current state of the project
    
    @var block: the block you wish to be displayed as a combination of ■ (1s) and blank spaces (0s).
    """
    arrays = [[' ' if x == 0 else '■' for x in i] for i in block]
    for i in arrays: print(*i, sep=" ", end="\n")