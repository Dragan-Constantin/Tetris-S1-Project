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
def clear():
    os.system("cls" if platform.system()=="Windows" else "clear")


# -----------------------------------------
# --- Secured Input
# -----------------------------------------
def secInput(msg: str) -> int:
    try: return int(input(msg))
    except (TypeError, ValueError): return -1

def choiceInput(msg: str) -> int:
    try:
        a = input(msg)
        if a.lower() in string.ascii_lowercase: return string.ascii_lowercase.index(a.lower())+1
        else: raise InvalidInput
    except (TypeError, ValueError, InvalidInput): return -1


# -----------------------------------------
# --- Display Single Block
# -----------------------------------------
def singleBlock(block):
    arrays = [[' ' if x == 0 else '■' for x in i] for i in block]
    for i in arrays: print(*i, sep=" ", end="\n")