from collections import defaultdict,deque

def light_check(num,lists,light):
    if light[num] == True:
        return True
    for l in lists:
        if light[l] == True:
            return True
    return False

def solution(n, lighthouse):
    path = {_ : [] for _ in range(1,n+1)}
    path_leaf = deque()
    light = defaultdict(bool)
    
    for l1,l2 in lighthouse:
        path[l1].append(l2)
        path[l2].append(l1)
        
    for k,v in path.items():
        if len(v) == 1:
            path_leaf.append(k)
        
    while path_leaf:
        num = path_leaf.popleft()
        if not path[num]:
            break
        nextn = path[num][0]
        
        path[nextn].remove(num)
        
        if not light_check(num,path[num],light):
            light[nextn] = True
            
        if len(path[nextn]) == 1:
            path_leaf.append(nextn)
    
    answer = list(light.values()).count(True)
    return answer
