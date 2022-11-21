from collections import defaultdict,deque

def dijk(road,des):              #BFS 노드별 도달 시간 기록
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
    
    res = dijk(road,destination) #목적지를 출발지역으로 입력
    for s in sources:
        if res[s]:               #도달 가능시 시간 기록
            answer.append(res[s])
        else:
            if s == destination: #목적지 출발지 같을 때
                answer.append(0)
            else:                #도달 불가능
                answer.append(-1)
    return answer
