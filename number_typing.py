from collections import defaultdict
import math

def weight(num,target):                       #가중치 리스트
    weights = [[1, 7, 6, 7, 5, 4, 5, 3, 2, 3],
               [7, 1, 2, 4, 2, 3, 5, 4, 5, 6],
               [6, 2, 1, 2, 3, 2, 3, 5, 4, 5],
               [7, 4, 2, 1, 5, 3, 2, 6, 5, 4],
               [5, 2, 3, 5, 1, 2, 4, 2, 3, 5],
               [4, 3, 2, 3, 2, 1, 2, 3, 2, 3],
               [5, 5, 3, 2, 4, 2, 1, 5, 3, 2],
               [3, 4, 5, 6, 2, 3, 5, 1, 2, 4],
               [2, 5, 4, 5, 3, 2, 3, 2, 1, 2],
               [3, 6, 5, 4, 5, 3, 2, 4, 2, 1]]
    
    return weights[num][target]

def new(dp,des):                              #다음번 가중치 계산
    ndp = defaultdict(lambda : math.inf)
    
    for key,value in dp.items():
        npos1 = tuple(sorted([key[1],des]))   #손가락이 반대 이기만 한 경우 제외
        npos2 = tuple(sorted([key[0],des]))
        if key[0] == des or key[1] == des:    #눌러야 할 숫자에 이미 올려져 있는 경우
            ndp[key] = min(ndp[key],value + 1)
            continue
            
        ndp[npos1] = min(ndp[npos1],value + weight(key[0],des))   #양쪽 손가락을 각각 움직였을 경우 최소값
        ndp[npos2] = min(ndp[npos2],value + weight(key[1],des))
    
    return ndp
    

def solution(numbers):
    dp = defaultdict(int)
    dp[(4,6)] = 0
    
    for n in numbers:
        n = int(n)
        dp = new(dp,n)
    
    answer = min(dp.values())
    return answer
