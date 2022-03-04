'''
주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
'''

s = input()

def solution(s):
	strs = []
	for c in s:
		if c.isalnum():
			strs.append(c.lower())

	for i in range(len(strs) // 2):
		if strs[i] != strs[-1 - i]:
			return False
	return True


print(solution(s))
