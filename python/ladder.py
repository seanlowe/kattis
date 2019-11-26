#!/bin/python3

import math

h, v = map(int, input().split())
v = v * (math.pi/180.0)

print(math.ceil(h/math.sin(v)))