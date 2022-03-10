'''
n개의 음이 아닌 정수들이 있습니다. 이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서
타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을
쓸 수 있습니다.

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를
적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.
'''


# numbers = [1, 1, 1, 1, 1]
# target = 3

numbers = [4, 1, 2, 1]
target = 4

from collections import deque

def solution(numbers, target):
	answer = 0
	queue = deque()
	queue.append(numbers[0])
	queue.append(-numbers[0])
	for i in range(1, len(numbers)):
		while len(queue) < 2 ** (i + 1):
			num = queue.popleft()
			queue.append(num + numbers[i])
			queue.append(num - numbers[i])
	return queue.count(target)

print(solution(numbers, target))
