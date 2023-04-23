def jaccard(set1, set2):
    if len(set2) == 0:
        return 1
    return len(set1) / len(set2)
    
def parse(s):
    ret = list()
    for i in range(len(s) - 1):
        parsed =  s[i: i + 2]
        if parsed.isalpha():
            while parsed.upper() in ret:
                parsed += '@'
            ret.append(parsed.upper())
    return set(ret)
    
def solution(str1, str2):
    r1, r2 = parse(str1), parse(str2)
    union = r1 | r2
    inter = r1 & r2
    j = jaccard(inter, union)
    return int(j * 65536)