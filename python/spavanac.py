#!/bin/python3

h, m = map(int, input().split())
#arr = list(map(int, input()))
#h, m = int(input()), int(input())

m = m - 45
if m < 0:
    m = 60 + m
    h = h - 1
    if h < 0:
        h = 24 + h

print(h, m)