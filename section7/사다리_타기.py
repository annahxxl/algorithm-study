import sys

sys.stdin = open("section7/input/사다리_타기.txt", "rt")

def dfs(x, y):
    visited[x][y] = True
    if x == 0:
        print(y)
    else:
        if ((y - 1) >= 0) and (ladder[x][y - 1] == 1) and (not visited[x][y - 1]):
            dfs(x, y - 1)
        elif ((y + 1) < 10) and (ladder[x][y + 1] == 1) and (not visited[x][y + 1]):
            dfs(x, y + 1)
        else:
            dfs(x - 1, y)

ladder = [list(map(int, input().split())) for _ in range(10)]

visited = [[False] * 10 for _ in range(10)]

for j in range(10):
    if ladder[9][j] == 2:
        dfs(9, j)
