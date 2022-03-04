
# -*- coding: utf-8 -*-

'''
N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.
'''
n = int(input())
nums = str(input())

def solution(nums):
	cnt = 0
	for n in nums:
		cnt += int(n)
	return cnt

print(solution(nums))
