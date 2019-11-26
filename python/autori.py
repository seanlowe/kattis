#!/bin/python3

arr = list(input().split("-"))
ans = ""
for i in range(0, len(arr)):
    ans += arr[i][0]

print(ans)