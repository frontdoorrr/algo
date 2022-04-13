'''
https://programmers.co.kr/learn/courses/30/lessons/42586#
'''
from collections import deque

def solution(progresses, speeds):
	cnt = 0
	ans = []
	queue, speeds = deque(progresses), deque(speeds)
	while queue:
		for i in range(len(queue)):
			queue[i] += speeds[i]
		while queue[0] >= 100:
			queue.popleft()
			speeds.popleft()
			cnt += 1
			if not queue:
				break
		if cnt != 0:
			ans.append(cnt)
		cnt = 0
	return ans

progresses = [99, 30, 99, 95, 55, 40, 90]
speeds     = [1, 30, 1, 5, 5, 40, 10]
print(solution(progresses, speeds))
