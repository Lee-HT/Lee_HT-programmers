from math import sqrt
from collections import defaultdict

def max_(lists,start,end):
    dicti = {}
    nmax = 0
    mnum = -1
    for n in range(end,start-1,-1):     #e에 가까운 순으로 max값 기록
        if nmax <= lists[n]:
            nmax = lists[n]
            mnum = n
        dicti[n] = mnum
    return dicti

def cal(res,e): #곱해서 e 이하인 수들 카운트
    for i in range(2,e+1):
        for j in range(1,min(e//i+1,i)):      #제곱수를 제외한 e 이하의 수 탐색
            res[i*j] += 2
    for i in range(1,int(sqrt(e+1))):     #제곱해서 e 이하인 수 탐색
        res[i**2] += 1

def solution(e, starts):
    result = [0 for _ in range(e+1)]
    cal(result,e)
    
    ans = {}
    
    ans = max_(result,min(starts),e)   #ans의 index에서 e까지 중 가장 많이 등장하는 수
    
    return [ans[s] for s in starts]
