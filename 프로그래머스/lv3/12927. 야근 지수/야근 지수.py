import heapq

def solution(n, works):
    if sum(works) < n:
        return 0
    hq = []
    
    for num in works:
        heapq.heappush(hq, -num)
    
    while n > 0 and hq:
        x = heapq.heappop(hq)
        n -= 1
        x += 1
        heapq.heappush(hq, x)
    print(hq)
    return sum([num**2 for num in hq])