#!/bin/python3

x = int(input())
n = int(input())
arr = []

# x is total MB allowed
# n is number of months

for i in range(0, n):
    # each input is number of MB used in that month
    arr.append(int(input()))

#print(arr)

amount_left = 0
for item in arr:
    current_usage = item
    amount_left += (x - current_usage)

print(amount_left+x)