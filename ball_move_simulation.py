def q0(p1,p2,m,dx): #w up
    if p1[1] == 0:    #목적지 도달 가능 위치가 가로축의 왼쪽 벽면에 붙어있는 경우
        p2[1] += dx   # 0~m만큼 의 범위가 모두 도달가능
    else:             
        p1[1] += dx   #시작에 붙어있지 않다면 시뮬레이션 역방향으로 이동
        if p1[1] >m-1:    #모든 도달 가능 위치가 범위를 벗어나면 불가능 리턴
            return False
        p2[1] += dx
    if p2[1] > m-1:       #일부 위치가 범위를 벗어나면 초과된 범위 줄임
            p2[1] = m-1
    return True

def q1(p1,p2,m,dx): #w down
    if p2[1] == m-1:   #가로축의 오른쪽 벽면에 붙어있는 경우
        p1[1] -= dx
    else:
        p1[1] -= dx
        p2[1] -= dx
        if p2[1] < 0:
            return False
    if p1[1] < 0:
        p1[1] = 0
    return True

def q2(p1,p2,n,dx): #h up
    if p1[0] == 0:     #세로축의 윗 벽면에 붙어있는 경우
        p2[0] += dx
    else:
        p1[0] += dx
        if p1[0] > n-1:
            return False
        p2[0] += dx
    if p2[0] > n-1:
        p2[0] = n-1
    return True

def q3(p1,p2,n,dx): #h down
    if p2[0] == n-1:    #세로축의 아랫 벽면에 붙어있는 경우
        p1[0] -= dx
    else:
        p1[0] -= dx
        p2[0] -= dx
        if p2[0] < 0:
            return False
    if p1[0] < 0:
        p1[0] = 0
    return True

def solution(n, m, x, y, queries):
    pos1 = [x,y]
    pos2 = [x,y]
    for q in queries[::-1]:          #목적지로 부터 역순으로 가능위치 추적
        fck = True
        if q[0] == 0:                #방향 정보
            fck = q0(pos1,pos2,m,q[1])
        elif q[0] == 1:
            fck = q1(pos1,pos2,m,q[1])
        elif q[0] == 2:
            fck = q2(pos1,pos2,n,q[1])
        elif q[0] == 3:
            fck = q3(pos1,pos2,n,q[1])
        if not fck:
            return 0
    answer = (pos2[0]-pos1[0]+1)*(pos2[1]-pos1[1]+1)      #도달 가능 지점의 총 개수 계산
    return answer
