import heapq

def solution(operations):
    min_q, max_q = list(), list()
    
    for operation in operations:
        t, n = operation.split()
        if t == 'I':
            heapq.heappush(min_q, int(n))
            heapq.heappush(max_q, (-1 * int(n), int(n)))
        elif t == 'D':
            if len(min_q) == 0:
                pass
            elif n == '1':
                val = heapq.heappop(max_q)[1]
                min_q.remove(val)
            else:
                val = heapq.heappop(min_q)
                max_q.remove((val * (-1), val))

    if len(min_q) == 0:
        return [0,0]
    return [heapq.heappop(max_q)[1], heapq.heappop(min_q)]