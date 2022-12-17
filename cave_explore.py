from queue import Queue
from collections import defaultdict, deque

def iscycle(path):
    visited = defaultdict(bool)
    check = defaultdict(bool)
    can = deque()
    can.append(0)
    
    while can:
        now = can[-1]
        if visited[now]:     #하위 노드가 없으면 한번 더 방문한 뒤
            check[now] = 0   #visited 체크 후 pop수행
            can.pop()        #사이클 체크를 위해 리프노드를 방문한 후 되돌아가며 해당노드 check 복귀
        else:
            visited[now] = 1
            check[now] = 1

        for p in path[now]:
            if not visited[p]:    #연결된 노드가 방문 하지 않았다면 큐에 추가
                can.append(p)
            elif check[p]:        #연결된 노드를 방문 하였는데 check가 1이라면
                return False      #되돌아가지 않은채로 해당노드를 방문한 것이므로 사이클
    
    return True

def tree(path,rpath):
    visited = defaultdict(bool)
    que = deque()
    que.append(0)
    
    while que:
        num = que.pop()
        visited[num] = 1
        for p in path[num]:
            if not visited[p]:
                que.append(p)
                rpath[num].append(p)
            

def solution(n, path, order):
    path_l = defaultdict(list)     #양방향 그래프
    rpath = defaultdict(list)      #트리 생성
    
    for p in path:
        path_l[p[0]].append(p[1])
        path_l[p[1]].append(p[0])
        
    tree(path_l,rpath)
    
    for k,v in order:
        rpath[k].append(v)  #방의 방문순서를 트리에 넣어준다
    
    return iscycle(rpath)   #트리에 사이클이 생성되어 있다면 order를 수행할 수 없음
