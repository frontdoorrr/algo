from collections import deque

def dfs(x, y, maps, m, n, visited):
    visited[x][y] = 1
    q = deque()
    q.append((x, y))
    
    cnt = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        if maps[x][y] != 'X':
            cnt += int(maps[x][y])
            
        maps[x][y] = 'X'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                pass
            elif maps[nx][ny] == 'X' or visited[nx][ny] == 1:
                pass
            else:
                q.append((nx, ny))
                visited[nx][ny] = 1
    return cnt
        

def solution(maps):
    q = deque()
    m, n = len(maps), len(maps[0])
    maps  = [list(row) for row in maps]
    answer = []
    visited = [[0] * n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            if maps[i][j] != "X" and visited[i][j] == 0:
                answer.append(dfs(i, j, maps, m, n, visited))
    if answer:
        return sorted(answer)
    return [-1]
    