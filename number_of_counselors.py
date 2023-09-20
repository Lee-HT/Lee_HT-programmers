from collections import deque
from heapq import heappop, heappush

def solution(k, n, reqs):
    # 여유 멘토
    mento = n-k
    k_reqs = [[] for _ in range(k)]
    # 유형, 멘토 별 상담 시간
    cons_times = [[] for _ in range(k)]
    # 상담 유형별 리스트에 저장
    for a,b,c in reqs:
        k_reqs[c-1].append([a,b])
    # 유형, 멘토 기준 대기 시간
    for i,req in enumerate(k_reqs):
        for m in range(mento+1):
            # 해당 상담 유형에 참가자 x 시 0 append
            if req:
                # 유형별 기본 1명 +
                cons_times[i].append(consult(m+1,req))
                # 유형에 참가자 x 시 0 append
            else:
                cons_times[i].append(0)
    
    counts = [0 for _ in range(k)]
    # 각 유형별로 멘토를 1명씩 추가했을 때 가장 많이 줄어드는 유형에 멘토 추가
    for i in range(mento):
        maxs = 0
        max_idx = 0
        for j in range(k):
            # 1명 추가시 줄어드는 대기시간
            cur = cons_times[j][counts[j]]-cons_times[j][counts[j]+1]
            if maxs < cur:
                max_idx = j
                maxs = cur
        counts[max_idx] += 1
        
    answer = 0
    # 유형별 대기시간 합 계산
    for i,cons in enumerate(cons_times):
        answer += cons[counts[i]]
    
    return answer

    # 멘토가 k명 일 때 대기시간
def consult(k,req):
    # 총 대기시간
    waiting_time = 0
    
    # 대기 시작 시간, 상담 시간
    wait = deque()
    
    # 타임 라인 = [상담 시작 시간, 상담 시간(0 == 상담 종료)]
    heap = []     # heap
    for r in req:
        start = r[0]
        cons = r[1]
        heappush(heap,(start,cons))
        
    # mento = [상담 종료 시간]
    mento = []     # heap
    cur_time = 0
    
    while heap:
        cur_time,cons = heappop(heap)
        # 새 참가자
        if cons != 0:
            wait.append((cur_time,cons))          # 대기열 추가
            if len(mento) < k:
                start,cons = wait.popleft()       # 대기열 pop
                heappush(mento,cur_time+cons)     # mento 대기열 push
                heappush(heap,(cur_time+cons,0))  # 종료 시간 타임 라인 push
        # 상담 종료
        else:
            heappop(mento)                        # 상담 종료
            if wait:
                start,cons = wait.popleft()       # 대기열 pop
                waiting_time += cur_time-start    # 상담 시작하는 참가자 대기시간 +
                heappush(mento,cur_time+cons)     # mento 대기열 push
                heappush(heap,(cur_time+cons,0))  # 종료 시간 타임 라인 push
            
    return waiting_time
