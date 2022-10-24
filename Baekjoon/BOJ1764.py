"""
김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때,
듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.
첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다.
이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과,
N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다.
이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하이다.
N, M은 500,000 이하의 자연수이다.
듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.
듣보잡의 수와 그 명단을 사전순으로 출력한다.
"""


n, m = map(int, input().split())
arr1, arr2 = [], []
for _ in range(n):
    arr1.append(input())
for _ in range(m):
    arr2.append(input())

arr2.sort()


def binary_search(arr, tar, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == tar:
            return arr[mid]
        elif arr[mid] < tar:
            start = mid + 1
        else:
            end = mid - 1
    return None


def solution(arr1, arr2):
    ans = []
    for name in arr1:
        dbj = binary_search(arr2, name, 0, len(arr2) - 1)
        if dbj:
            ans.append(dbj)
    return ans


ans = solution(arr1, arr2)
ans = sorted(ans)


print(len(ans))
for i in ans:
    print(i)
