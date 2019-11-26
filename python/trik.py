#!/bin/python3 

str = input()
pos = 1

# 1 under left
# 2 under middle
# 3 under right

# A left and middle
# B middle and right
# C left and right

for char in str:
    if char == "A" and pos == 1:
        pos = 2
    elif char == "A" and pos == 2:
        pos = 1
    elif char == "A" and pos == 3:
        a = 1+1

    elif char == "B" and pos == 1:
        a = 1+1
    elif char == "B" and pos == 2:
        pos = 3
    elif char == "B" and pos == 3:
        pos = 2
 
    elif char == "C" and pos == 1:
        pos = 3
    elif char == "C" and pos == 2:
        a = 1+1
    elif char == "C" and pos == 3:
        pos = 1

print(pos)