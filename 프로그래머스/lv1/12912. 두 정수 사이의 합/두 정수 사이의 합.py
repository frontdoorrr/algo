def solution(a, b):
    m, n  = min(a, b), max(a, b)
    if m != n:
        return sum([x for x in range(m, n + 1)])
    return a
        
    return answer