"""
백준이는 동생에게 "가운데를 말해요" 게임을 가르쳐주고 있다.
백준이가 정수를 하나씩 외칠때마다 동생은 지금까지 백준이가 말한 수 중에서 중간값을 말해야 한다.
만약, 그동안 백준이가 외친 수의 개수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 한다.

예를 들어 백준이가 동생에게 1, 5, 2, 10, -99, 7, 5를 순서대로 외쳤다고 하면,
동생은 1, 1, 2, 2, 2, 2, 5를 차례대로 말해야 한다. 백준이가 외치는 수가 주어졌을 때, 동생이 말해야 하는 수를 구하는 프로그램을 작성하시오.
"""


from heapq import heappush, heappop
import sys
from typing import List

n = int(sys.stdin.readline())
nums = list()
for _ in range(n):
    nums.append(int(sys.stdin.readline()))


def solution(nums: List):
    mid = nums[0]
    greater, less = [], []
    for num in nums:
        if len(greater) == len(less):
            heappush(less, (-num, num))
        else:
            heappush(greater, (num, num))
        if greater and less[0][1] > greater[0][1]:
            left = heappop(less)[1]
            right = heappop(greater)[1]
            heappush(less, (-right, right))
            heappush(greater, (left, left))
        print(less[0][1])


solution(nums)
