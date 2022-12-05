import fileinput

for line in fileinput.input(files='day1.1input.txt'):
    integer = int(line)

element1 = 1
sumlist = [element1] 

print(max(sumlist))