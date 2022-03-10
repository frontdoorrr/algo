'''
N×M크기의 직사각형이 있다. 각 칸에는 한 자리 숫자가 적혀 있다.
이 직사각형에서 꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형을 찾는 프로그램을 작성하시오.
이때, 정사각형은 행 또는 열에 평행해야 한다.
'''

n, m = map(int,input().split())
board = []
for i in range(n):
	board.append(input())


def solution(board, n, m):

	ans = 1
	size = min(n, m)
	for i in range(n):
		for j in range(m):
			for l in range(1, size):
				if (n <= i + l) or (m <= j + l):
					break
				if board[i][j] == board[i][j + l] == board[i + l][j] == board[i + l][j + l]:
					if (ans <= (l + 1) * (l + 1)):
						ans = (l + 1) * (l + 1)
	return ans


print(solution(board, n, m))
