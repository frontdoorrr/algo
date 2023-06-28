from collections import deque

def solution(n, edge):
    graph = dict()
    visited = [-1 for _ in range(n + 1)] 
    for e in edge:
        if graph.get(e[0]):
            graph[e[0]].append(e[1])
        else:
            graph[e[0]] = [e[1]]
        if graph.get(e[1]):
            graph[e[1]].append(e[0])
        else:
            graph[e[1]] = [e[0]]
    q = deque()
    q.append((1, 0))
    while q:
        node, cnt = q.popleft()
        for nxt in graph.get(node, []):
            if visited[nxt] == -1:
                visited[nxt] = cnt + 1
                q.append((nxt, cnt + 1))
    
    v = visited[2:]
    max_num= max(v)
    return v.count(max(v))
    
    