def parse(s):
    string, num, tail = '', '', '' 
    for i in range(len(s)):
        if s[i].isnumeric() == True:
            string = s[:i]
            break
    print(string)
    for j in range(i, len(s)):
        if s[j].isnumeric() == False:
            print(s, s[j])
            num = s[i:j]
            tail = s[j:]
            break
    if num == '':
        num = s[i:]
        
        
    return string.lower(), int(num), tail,  s

    
def solution(files):
    
    arr = []
    for file in files:
        info = parse(file)
        print(info)
        arr.append(info)
    arr.sort(key=lambda x : (x[0], x[1]))
    return [i[3] for i in arr]

        
