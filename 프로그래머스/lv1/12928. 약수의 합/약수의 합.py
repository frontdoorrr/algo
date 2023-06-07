def solution(n):
    ans = n
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            ans+=i
    return ans