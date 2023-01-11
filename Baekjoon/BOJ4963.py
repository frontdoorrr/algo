"""
정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.

한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다.

두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.
"""
import sys
sys.setrecursionlimit(10000)

def dfs(board, x, y):
    if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
        return
    if board[x][y] == 0:
        return

    board[x][y] = 0

    dfs(board, x, y - 1)
    dfs(board, x, y + 1)
    dfs(board, x - 1, y)
    dfs(board, x + 1, y)
    dfs(board, x + 1, y + 1)
    dfs(board, x + 1, y - 1)
    dfs(board, x - 1 , y + 1)
    dfs(board, x - 1, y - 1)


def solution(board):
    cnt = 0

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                dfs(board, i, j)
                cnt += 1
    return cnt

def dfs_sol():
    w, h = map(int, input().split())

    board = []
    for _ in range(h):
        board.append(list(map(int,input().split())))

    ans = solution(board)
    return ans


while True:
    try:
        print(dfs_sol())
    except:
        break
