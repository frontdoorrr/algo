'''
n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다.
ai의 값은 1보다 크거나 같고, 1000000보다 작거나 같은 자연수이다.
자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수를 구하는 프로그램을 작성하시오.
'''
import sys

n = int(input())
num_arr = list(map(int, sys.stdin.readline().split()))
x = int(input())

def solution(arr, tar):
	arr.sort()
	cnt = 0
	left, right = 0, len(arr) - 1
	while left < right:
		if tar == arr[left] + arr[right]:
			cnt += 1
		if tar > arr[left] + arr[right]:
			left += 1
			continue
		right -= 1
	return cnt

print(solution(num_arr, x))
