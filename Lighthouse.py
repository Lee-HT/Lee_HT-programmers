from collections import defaultdict,deque

def light_check(num,lists,light): #자신과 연결된 노드의 등대가 켜진지 확인
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
    
    for l1,l2 in lighthouse: #트리 생성
        path[l1].append(l2)
        path[l2].append(l1)
        
    for k,v in path.items(): #리프 노드 큐에 입력
        if len(v) == 1:
            path_leaf.append(k)
        
    while path_leaf:
        num = path_leaf.popleft()
        if not path[num]:
            break
        nextn = path[num][0]
        
        path[nextn].remove(num) #확정된 리프 노드를 부모 노드에서 제거
        
        if not light_check(num,path[num],light):
            light[nextn] = True
            
        if len(path[nextn]) == 1: #부모 노드가 리프 노드가 될 시 추가
            path_leaf.append(nextn)
    
    answer = list(light.values()).count(True)
    return answer
