from itertools import permutations
from math import sqrt

def is_prime_num(n):
	if n in [0, 1]:
		return False
	for i in range(2, int(sqrt(n))):
		if n % i == 0:
			return False
	return True

def solution(numbers):
	cnt = 0
	answer, per_list = [], []
	numbers_list = list(numbers)

	for i in range(1, len(numbers) + 1):
		per_list += list(permutations(numbers_list, i))

	for permutation in per_list:
		num = int(''.join(permutation))
		answer.append(num)

	answer = list(set(answer))

	for a in answer:
		if is_prime_num(a) == True:
			cnt += 1
	return answer, cnt

print(solution("1111111111"))
# print(solution("011"))
