def convert(n, k):
    ret = []
    if n < k:
        return [str(n)]
    nn = ''
    while n > 0:
        nn += str(n % k)
        n = n // k
    
    return nn[::-1].split('0')

def is_prime(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    m = int(x ** 0.5) + 1
    for i in range(2, m):
        if x % i == 0:
            return False 
    return True 

def solution(n, k):
    s =  convert(n, k)
    cnt = 0
    for c in s:
        if c in ['', '1', '0']:
            continue
        n = int(c)
        if is_prime(n):
            
            cnt += 1
            
    return cnt
    