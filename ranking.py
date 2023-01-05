from collections import defaultdict,deque

def DFS(start,graph,n):            #승리가 확정된 선수
    res = [0 for i in range(n)]
    stack = deque([start])
    while stack:
        n = stack.pop()
        res[n] = 1
        for g in graph[n]:
            if not res[g]:
                stack.append(g)
    return res

def solution(n, results):
    graph = [[] for i in range(n)]
    for r1,r2 in results:
        graph[r1-1].append(r2-1)     #그래프 입력
    res = []
    for i in range(n):
        res.append(DFS(i,graph,n))   #DFS로 i번째 선수가 승리한 선수 &그 선수가 승리한 다른 선수
                                     #A -> B -> C  == A -> C
    answer = 0
    
    for i in range(n):
        check = 0
        for j in range(n):
            if res[i][j] or res[j][i]:   #승리 가능 선수 i,j 패배 확정 선수 j,i
                check += 1
        if check == n:          #모든 선수와 승리 패배가 확정되어 있다면
            answer += 1
        
    return answer
