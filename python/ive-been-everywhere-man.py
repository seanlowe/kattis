#!/bin/python3

test_cases=int(input())

arr = []
final = ""

for i in range(0, test_cases):
    count=int(input())
    unique = 0
    for j in range(0, count):
        tempstr = input()
        if tempstr not in arr:
            arr.append(tempstr)
            unique += 1
    final += str(unique) + "\n"

print(final, end="")