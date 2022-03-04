'''
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고,
kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.
'''

n = int(input())
words = []
for _ in range(n):
	words.append(input())


def is_group_word(s):
	length = len(s)
	c_list = []

	for i in range(length):
		if i == length - 1:
			c_list.append(s[i])
		elif s[i] != s[i + 1]:
			c_list.append(s[i])

	if len(set(c_list)) == len(c_list):
		return True
	return False


def solution(words):
	cnt = 0
	for word in words:
		if is_group_word(word):
			cnt += 1
	return cnt

print(solution(words))
