'''
세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.
그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.
괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.
'''

input_exp = input()

def str_add(s):
	if '+' in s:
		nums = map(int, s.split('+'))
		return sum(nums)
	else:
		return int(s)


def solution(string):
	value = 0
	input_value = string.split('-')
	ans = [str_add(input_value[0])]

	for i in range(1, len(input_value)):
		ans.append(-str_add(input_value[i]))

	return sum(ans)



print(solution(input_exp))
print(solution('55-50+40'))
print(solution('10+20+30+40'))
print(solution('00009-00009'))


