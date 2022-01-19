'''
한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고,
각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과
동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다.
이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.
'''

n = int(input())

meetings = []
for _ in range(n):
	s, e= map(int, input().split())
	meetings.append([s,e])


def solution(meetings):
	cnt = 0
	end_time = 0
	meetings = sorted(meetings, key=lambda x: (x[1], x[0]))
	for s, e in meetings:
		if s >= end_time:
			cnt += 1
			end_time = e
	return cnt


print(solution(meetings))


# 회의의 end_time을 다음 회의의 시작시간과 비교하고 갱신해주는 방향으로 푼다.
