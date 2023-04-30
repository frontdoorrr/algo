def solution(elements):
    length = len(elements)
    elements += elements
    ans = set()
    
    for i in range(length):
        for j in range(i, i + length + 1):

            ans.add(sum(elements[i:j]))
    
    return len(ans) - 1