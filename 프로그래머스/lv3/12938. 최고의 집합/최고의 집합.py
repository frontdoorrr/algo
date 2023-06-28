def solution(n, s):
    if n > s:
        return [-1]
    arr = [s // n ] * n
    if sum(arr) < s:
        rem = s - sum(arr)
        i = len(arr) - 1
        while rem > 0 and i >= 0:
            rem -=  1
            arr[i] += 1
            i -= 1
    return arr