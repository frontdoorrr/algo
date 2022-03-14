'''
N×M크기의 배열로 표현되는 미로가 있다.
1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다.
이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때
지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로
이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는
시작 위치와 도착 위치도 포함한다.
'''

from collections import deque

n, m = map(int,input().split())
board = []
for _ in range(n):
	board.append(list(map(int, input())))

def solution(board):
	queue = deque()
	queue.append([0,0])
	dx = [1, -1, 0, 0]
	dy = [0, 0, -1, 1]
	while queue:
		x, y = queue.popleft()
		for i in range(4):
			nx, ny = x + dx[i], y + dy[i]
			if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
				if board[nx][ny] == 1:
					queue.append([nx, ny])
					board[nx][ny] = board[x][y] + 1
	return board[len(board) - 1][len(board[0]) - 1]

print(solution(board))
