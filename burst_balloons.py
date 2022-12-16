from math import inf

def leftmin(lista):
    leftlist = []
    lmin = inf
    for i in lista[:-1]:
        if i < lmin:
            lmin = i
        leftlist.append(lmin)
    leftlist.insert(0,inf)
    return leftlist

def rightmin(lista):
    rightlist = []
    rmin = inf
    for i in lista[:0:-1]:
        if i < rmin:
            rmin = i
        rightlist.append(rmin)
    rightlist.insert(0,inf)
    return rightlist
    

def minmax(num,left,right):
    if num < max(left,right):       #둘중 하나라도 현재 풍선보다 크면
        return 1                    #기회 소모없이 터트릴 수 있음
    return 0    

def solution(a):
    answer = 0
    lena = len(a)
    leftlist = leftmin(a)        #0~index-1 범위의 최소값 (dp) / index 낮은순 저장
    rightlist = rightmin(a)      #index+1~lena 범위의 최소값 / index 높은순 저장
    for i in range(lena):
        lmin = leftlist[i]
        rmin = rightlist[-(i+1)]    #right은 역순으로 저장
        answer += minmax(a[i],lmin,rmin)    #해당 풍선의 양옆 풍선들의 최소값 풍선을 제외하고 기회 소모없이 제거가능
    return answer
