'''
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오(시간 복잡도가 O(nlogn)인 알고리즘 이용).
'''

n = int(input())
numbers = []
for _ in range(n):
	numbers.append(int(input()))

def merge_sort(arr):
	if len(arr) < 2:
		return arr

	mid = len(arr) //2
	left_arr = merge_sort(arr[:mid])
	right_arr = merge_sort(arr[mid:])

	merged_arr = []
	left, right = 0, 0
	while left < len(left_arr) and right < len(right_arr):
		if left_arr[left] < right_arr[right]:
			merged_arr.append(left_arr[left])
			left += 1
		else:
			merged_arr.append(right_arr[right])
			right += 1
	merged_arr += left_arr[left:]
	merged_arr += right_arr[right:]
	return merged_arr

def solution(numbers):
	answer = merge_sort(numbers)
	return answer

print(solution(numbers))
