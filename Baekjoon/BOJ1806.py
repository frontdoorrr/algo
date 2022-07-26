'''
10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다.
이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.
'''

import sys
n, s = map(int, sys.stdin.readline().split())
num_arr = list(map(int, sys.stdin.readline().split()))

def solution(n, s, arr):
	tot = 0
	length = n
	for i in range(n - 1):

		j = i + 1
		total = arr[i]
		while total < s:
			total += arr[j]
			j += 1
			if j == n:
				return length
			# print(f"total: {total} / i , j : {i}, {j}")
		tmp_len = j - i
		if length > tmp_len:
			length = tmp_len
		# print(f"length : {length}")
	return length

print(solution(n, s, num_arr))
