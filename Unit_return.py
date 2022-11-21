from collections import defaultdict,deque

def dijk(road,des):
    res = defaultdict(int)
    visited = defaultdict(bool)
    que = deque()
    que.append((des,0))
    res[des]=1
    visited[des]=1
    
    while que:
        now,t = que.popleft()
        for r in road[now]:
            if not visited[r]:
                visited[r] = 1
                que.append((r,t+1))
                res[r] = t+1
    return res
                

def solution(n, roads, sources, destination):
    road = [[] for _ in range(n+1)]
    for r1,r2 in roads:
        road[r1].append(r2)
        road[r2].append(r1)
    
    answer = []
    
    res = dijk(road,destination)
    for s in sources:
        if res[s]:
            answer.append(res[s])
        else:
            if s == destination:
                answer.append(0)
            else:
                answer.append(-1)
    return answer
