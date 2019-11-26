#!/bin/python3
 
# ki, qu, ro, bi, kn, pa
# 0   1   2   3   4   5   # arr indexes
# 1   1   2   2   2   8   # wanted values

actual_values = list(map(int, input().split()))
expected_values = [1, 1, 2, 2, 2, 8]
ans = ""

for i in range(0, len(actual_values)):
    if (actual_values[i] == expected_values[i]):
        ans += "0 "
    else:
        temp = -1 * (actual_values[i] - expected_values[i])
        ans += str(temp) + " "
 
print(ans)