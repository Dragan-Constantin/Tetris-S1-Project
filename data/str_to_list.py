from os import system
system("cls")

with open("data/t", "r") as f:
    a = f.readlines()

for i in range(len(a)):
    a[i] = a[i].split(' ')
for i in range(len(a)):
    for j in range(len(a[i])):
        if "\n" in a[i][j]:
            a[i][j]= a[i][j].replace("\n", '')

with open("data/t2", 'w') as f:
    for i in a:
        for j in i:
            f.write(f'"{j}", ')
        f.write("\n")