#!/bin/python3

def rotate(direction, board):
    if direction == 1:
        return list(zip(*board[::-1]))
    else:
        return list(zip(*board))[::-1]

def zeros_correct(row, index):
    for item in row[index]:
        if item != 0:
            return False
    return True

def handle_zeros(row, index): 
    while True:
        if zeros_correct(row, index):
            break
        if row[index] == 0:
            row.pop(index)
            row.append(0)
            continue
        break

def merge(board):
    for i in range(4):
        line = list(board[i])
        for j in range(4):
            handle_zeros(line, j)
            if j != 0 and line[j] == line[j-1]:
                line[j-1] = int(line[j-1]*2)
                line.pop(j)
                line.append(0)
                handle_zeros(line, j)
            board[i] = list(line)
    return board
    
board = [list(map(int, input().split())) for _ in range(4)]
swipe = int(input())

for i in range(swipe):
    board = rotate(0, board)

board = merge(board)

for i in range(swipe):
    board = rotate(1, board)

for j in range(4):
    print(*board[j])