'''
https://programmers.co.kr/learn/courses/30/lessons/42587
'''
from collections import deque

def solution(priorities, location):
	p = deque(priorities)
	cnt = 0
	while p:
		if p[0] == max(p):
			p.popleft()
			cnt += 1
			location -= 1
			if location < 0:
				return cnt
		else:
			p.append(p.popleft())
			location -= 1
			if location < 0:
				location = len(p) - 1
	return 0

pr = [2, 1, 3, 2]
l = 2

print("answer :",solution(pr, l))
