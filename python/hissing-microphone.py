#!/bin/python3

word = input()
count = 0

for i in range(0,len(word)):
    if count == 1 and word[i] != 's':
        count += -1
    if word[i] == 's':
        count += 1

if count > 1:
    print("hiss")
else:
    print("no hiss")