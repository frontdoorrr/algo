"""
널리 잘 알려진 자료구조 중 최대 힙이 있다. 최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

배열에 자연수 x를 넣는다.
배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.
"""

from typing import List
import heapq
import sys

n = int(sys.stdin.readline())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))


def solution(nums: List) -> List:
    heap = []
    ans = []
    for num in nums:
        if num == 0:
            if heap:
                n = heapq.heappop(heap)
                print(n[1])
            else:
                print(0)
        else:
            heapq.heappush(heap, (-num, num))


solution(nums)
