import string
import json

with open('data/diamond.json') as f:
    data = json.load(f)
    c_grid = data["circle"]

top = string.ascii_lowercase
down = string.ascii_uppercase

c_grid1 = c_grid
for i in c_grid1:
    for j in range(len(i)): i[j] = " " if i[j] == '0' else '∙'

topline = ["‾", "‾", "‾", "‾", "‾", "‾", "‾", "‾", "‾", "‾", "‾", "‾", "‾", "‾", "‾", "‾", "‾", "‾", "‾", "‾", "‾", "‾", "‾", "‾", "‾"]

def show_grid():
    print("     ", end="")
    for i in range(0, len(c_grid[0])):
        if i==len(c_grid[0])-1: print(top[i], end="\n")
        else: print(top[i], end=" ")
    print("  |‾‾", end="")
    for i in range(0, len(c_grid[0])):
        if i==len(c_grid[0])-1: print(topline[i], end="‾‾|\n")
        else: print(topline[i], end="‾")
    for i in range(0, len(c_grid)):
        a = i
        print(down[i], end=" ")
        print("|", end="  ")
        print(*c_grid1[i], sep=" ", end="  |\n")
        # print("|")
    print("  |", end="")
    for i in range(0, len(c_grid[0])): print("  ", end="")
    print("   |")
    print("   ‾‾", end="")
    for i in range(0, len(c_grid[0])):
        if i==len(c_grid[0])-1: print(topline[i], end="‾‾\n")
        else: print(topline[i], end="‾")

# show_grid()