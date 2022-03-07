'''
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다.
지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.
'''

n = int(input())
grid = []
for _ in range(n):
	grid.append(list(map(int, input())))


def dfs(grid, x, y, cnt):
	if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
		return
	if grid[x][y] != 1:
		return
	if grid[x][y] == 1:
		grid[x][y] = cnt
		dfs(grid, x, y - 1, cnt)
		dfs(grid, x, y + 1, cnt)
		dfs(grid, x - 1, y, cnt)
		dfs(grid, x + 1, y, cnt)


def count_grid(grid):
	if not grid:
		return 0
	cnt = 2
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 1:
				dfs(grid, i, j, cnt)
				cnt += 1
	return cnt - 2

def solution(grid):
	ans = count_grid(grid)
	cnt = [0] * ans
	for i in range(len(grid)):
		for j in range(2, ans + 2):
			cnt[j - 2] += grid[i].count(j)
	print(ans)
	for i in sorted(cnt):
		print(i)

solution(grid)

