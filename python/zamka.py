#!/bin/python3

# l -> lower bound
# d -> upper bound
# x -> number to find via adding digits
 
l = int(input())
d = int(input())
x = int(input())
 
# n -> min num required to reach x
# m -> max num required to reach x
n = l
m = d
 
count = l
while count < d:
    if sum(map(int, str(n))) == x:
        break
    count += 1
    n += 1 

count = d
while count > l:
    if sum(map(int, str(m))) == x:
        break
    count -= 1
    m -= 1

print(n)
print(m)