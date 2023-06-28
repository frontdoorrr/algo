from collections import deque

def get_diff_1(w1, w2):
    length = len(w1)
    cnt = 0
    for i in range(length):
        if w1[i] != w2[i]:
            cnt += 1
    if cnt == 1:
        return True
    return False

def solution(begin, target, words):
    if target not in words:
        return 0
    q = deque()
    q.append((0, begin))
    while q:
        cnt, w = q.popleft()
        if w == target:
            return cnt
        for word in words:
            if get_diff_1(word, w):
                q.append((cnt + 1, word))
    return answer