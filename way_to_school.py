def cal(h,w,check):
    res = 0
    if h != 0:
        res += check[h-1][w]   #윗칸이 존재한다면 위에 도달 가능한 경로 수 +
    if w != 0:
        res += check[h][w-1]   #왼쪽 칸이 존재한다면 왼쪽 칸에 도달 가능한 경로 수 +
    return res
    

def solution(m, n, puddles):
    road = [[0 for m in range(m)] for n in range(n)]   #물에 잠긴 길 확인
    road[0][0] = 1
    check = [[0 for m in range(m)] for n in range(n)]    #누적 경로 수 확인
    check[0][0] = 1
    for p in puddles:
        road[p[1]-1][p[0]-1] = 1
        
    for h in range(n):
        for w in range(m):     #왼쪽부터 1열씩 누적 경로 수 계산
            if road[h][w]:
                continue
            check[h][w] = cal(h,w,check)
        
    
    answer = check[n-1][m-1]   #1~n 1~m 이므로 리스트에선 -1
    return answer%1000000007    #최종 결과 리턴
