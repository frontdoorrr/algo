'''
1을 육지로, 0을 물로 가정한 2D 그리드 맵이 주어졌을 때, 섬의 갯수를 계산하라.
'''

grid_map = [[1,1,1,1,0],
			[1,1,0,1,0],
			[1,1,1,0,0],
			[0,0,1,0,1]]


def dfs(maps, x, y):
	if x < 0 or x >= len(maps) or y < 0 or y >= len(maps[0]):
		return
	if maps[x][y] != 1:
		return
	if maps[x][y] == 1:
		maps[x][y] = 0
		dfs(maps, x + 1, y)
		dfs(maps, x, y + 1)
		dfs(maps, x - 1, y)
		dfs(maps, x, y - 1)

def solution(maps):
	if not maps:
		return 0
	count = 0
	for i in range(len(maps)):
		for j in range(len(maps[0])):
			if maps[i][j] == 1:
				dfs(maps, i, j)
				count += 1
	return count

print(solution(grid_map))

'''
최종적으로 dfs가 종료되면 count가 올라가는 방식으로 섬 1개를 판단한다.
'''
