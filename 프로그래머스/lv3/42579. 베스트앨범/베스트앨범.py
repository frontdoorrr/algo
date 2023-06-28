def solution(genres, plays):
    answer = []
    dic = dict()
    gen = dict()
    for i, play in enumerate(plays):
        if gen.get(genres[i]):
            gen[genres[i]] += play
            dic[genres[i]].append((i, play))
        else:
            gen[genres[i]] = play
            dic[genres[i]] = [(i, play)]
    
    for val in dic.values():
        val.sort(key=lambda x: -x[1])
    ret = []
    gen = sorted(list(gen.items()), key=lambda x: -x[1])
    
    for g in gen:    
        ans = [i[0] for i in dic[g[0]][:2]]
        ret += ans
    return ret