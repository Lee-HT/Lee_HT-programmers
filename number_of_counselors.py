from collections import deque
from heapq import heappop, heappush
from itertools import combinations_with_replacement

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
    
    # case 1
    # 1명을 추가했을 때 대기 시간이 많이 줄어드는 유형에 멘토 추가
    counts = [0 for _ in range(k)]
    for i in range(mento):
        maxs = 0
        max_idx = 0
        for j in range(k):
            cur = cons_times[j][counts[j]]-cons_times[j][counts[j]+1]
            if maxs < cur:
                max_idx = j
                maxs = cur
        counts[max_idx] += 1
        
    answer = 0
    # 유형별 대기시간 합 계산
    for i,cons in enumerate(cons_times):
        answer += cons[counts[i]]
    
    # case 2
    # 멘토의 가능한 상담 유형 조합
    # answer = 1e+10
    # for combi in find_combination(mento,k):
    #     time_sum = 0
    #     for i,c in enumerate(combi):
    #         time_sum += cons_times[i][c]
    #     answer = min(answer,time_sum)
    
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

    # 추가 가능한 멘토가 n명, 유형이 k개일 때 조합 
def find_combination(n,k):
    result = []
    mento_type = combinations_with_replacement(range(k),n)
    for m in mento_type:
        combi = [0 for _ in range(k)]
        for i in m:
            combi[i] += 1
        result.append(combi)
    return result
