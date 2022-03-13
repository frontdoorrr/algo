from collections import deque

def distance(a, b, routes):
	cnt = 0
	queue = deque()
	queue.append(a)
	visited = [False] * len(routes)
	while queue:
		if b in queue:
			return cnt
		tar = queue.popleft()
		visited[tar] = True
		if b not in queue:
			# cnt += 1
			for i in routes[tar]:
				if visited[i] == False:
					if b in routes[i]:
						cnt += 1
					queue.append(i)
	return cnt


def solution(n, edges):
	routes = [[] for _ in range(n)]
	count = 0
	visited = [False] * n
	for i, j in edges:
		routes[i].append(j)
		routes[j].append(i)
	for i in range(n):
		for j in range(n):
			for k in range(n):
				if i != j and i != k and j != k:
					if distance(i, j, routes) + distance(j, k, routes) == distance(i, k, routes):
						count += 1
	return count

print(solution(5, [[0,1], [0,2], [1,3], [1,4]]))
# print(solution(4, [[2,3],[0,1],[1,2]]))


