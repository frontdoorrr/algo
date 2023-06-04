from collections import deque

def check(dp, n):
    if n > len(dp) - 1:
        return False
    if dp[n] == 0:
        dp[n] = 1
        return True
    else:
        return False

def solution(x, y, n):
    dp = [0 for i in range(y + 1)]
    q = deque()
    num = -1
    cnt = 0
    q.append((x, 0))
    while q:
        num, cnt = q.popleft()
        # print(num, cnt)
        if num < y:
            for i in range(3):
                if i == 1:
                    new = num + n
                elif i == 2:
                    new = num * 2
                else:
                    new = num * 3
                if check(dp, new):
                    q.append((new, cnt + 1))
        
        elif num == y:
            return cnt
                    
    return -1