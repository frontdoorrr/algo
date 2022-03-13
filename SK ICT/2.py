


def fill_numbers(i, j, arr, direction, nb):
	dx = [1, 0, -1, 0]  # 동, 남, 서, 북
	dy = [0 ,1, 0, -1]

	arr[i][j] = nb
	if arr[i + dx[direction]][j + dx[direction]] == 0:
		fill_numbers(i, j, arr, direction, nb + 1)
	elif arr[i + dx[direction]][j + dx[direction]] != 0:
		if direction != 3:
			fill_numbers(i, j, arr, direction, nb + 1)
		else:
			fill_numbers(i, j, arr, 0, nb + 1)
	else:
		return






def solution(n, clockwise):
	arr = [[0 for i in range(n)] for j in range(n)]
	arr[0][0], arr[0][n - 1], arr[n - 1][0], arr[n - 1][n - 1] = 1, 1, 1, 1
	fill_numbers(0, 1, arr, 0, 2)
	fill_numbers(1, n - 1, arr, 1, 2)
	fill_numbers(n - 1, n - 2, arr, 2, 2)
	fill_numbers(n - 2, 0, arr, 3, 2)


	return arr






print(solution(5, True))
# print(solution(6, False))
# print(solution(9, False))
