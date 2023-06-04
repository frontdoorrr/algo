def solution(weights):
    ans = 0
    dic = {}
    
    for i in weights:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1

    for n in dic:
        if dic[n] > 1:
            ans += dic[n] * (dic[n] - 1) /2
        if n * 2 in dic.keys():
            ans += dic[n] * dic[n * 2]
        if n * 2 / 3 in dic.keys():
            ans += dic[n] * dic[n * 2 / 3]
        if n * 3 / 4 in dic.keys():
            ans += dic[n] * dic[n * 3 / 4]
    return ans
    
    
    