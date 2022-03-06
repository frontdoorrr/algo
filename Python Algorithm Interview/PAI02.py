'''
높이를 입력받아 비가 온 후, 얼마나 많은 물이 쌓일 수 있는지 계산하라.
'''

# arr = list(map(int,input().split()))

def solution(height):
	volume = 0

	left, right = 0, len(height) - 1
	left_max, right_max = height[left], height[right]

	while left < right:
		print(f"left : {left} / right : {right}")
		print(f"left_max : {left_max} / right_max : {right_max}")
		print(f"height[left] : {height[left]} / height[right] : {height[right]}")

		left_max, right_max = max(height[left], left_max), max(height[right], right_max)
		if left_max <= right_max:
			print("left_max <= right_max")
			volume += left_max - height[left]
			left += 1
		else:
			print("left_max > right_max")
			volume += right_max - height[right]
			right -= 1
		print(f"volume : {volume}")
		print("\n\n")
	return volume



print(f"answer is  {solution([0,1,0,2,1,0,1,3,2,0,2,1])}")


'''
투 포인터를 사용해서 O(n)에 풀이가 가능하도록 한다.
left_max <= right_max 조건은 큰 의미는 없고 연산 횟수를 위함
좌우 어느 쪽이든 낮은 쪽은 높은 쪽을 향해서 포인터가 가운데로 점점 이동함
'''
