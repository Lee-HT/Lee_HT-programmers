from collections import defaultdict
from heapq import heappop, heappush
import math

def BFS(start,path,loc):
    visited = defaultdict(bool)
    intensity = 0
    hq = []
    heappush(hq,(0,start))    #출발지 푸시
    
    while hq:
        inte,now = heappop(hq)             #heapq를 이용해 intensity가 낮은것 부터 순회
        if visited[now]:
            continue
        visited[now] = 1
        intensity = max(intensity,inte)    #현재 intensity 갱신
        if loc[now] == 1:
            return [intensity,now]         #현재 위치가 산봉우리일 시 산봉우리 번호와 intensity 최소값 리턴
        for n in path[now].keys():
            if not (visited[n] or loc[n] == 2):    #방문 한곳, 출발지를 제외하고 힙큐에 푸시
                heappush(hq,(path[now][n],n))
    return [math.inf,0]
    
def solution(n, paths, gates, summits):
    path = {_ : {} for _ in range(1,n+1)}
    loc = {_ : 0 for _ in range(1,n+1)}
    for i,j,w in paths:    #양방향 그래프 생성
        path[i][j] = w
        path[j][i] = w
        
    for s in summits:      #산봉오리 == 1
        loc[s] = 1
    for g in gates:        #게이트(출발지) == 2
        loc[g] = 2
    
    gate_inte = []
    
    for g in gates:
        gate_inte.append(BFS(g,path,loc))
    answer = min(gate_inte)                  #intensity가 최소인 값
    answer = [answer[1],answer[0]]           #리턴값을 위해 위치 변경
    return answer
