def cal(h,w,abh,abw,cdict):
    if h>0:
        cdict['d'] += abh
    elif h<0:
        cdict['u'] += abh
    if w<0:
        cdict['l'] += abw
    elif w>0:
        cdict['r'] += abw
        
def route(cdict,h,w,n,m,over,k):
    
    for o in range(over//2):
        if h + cdict['d'] < n:     #가장 아래일 경우가 n 이하라면
            cdict['d'] += 1        #(더 내려갈 수 있으면)
            cdict['u'] += 1        #d와 l을 우선하는 가능한 왕복 명령 추가
        else:
            cdict['l'] += 1
            cdict['r'] += 1
    
    res = []
    
    ch, cw = h,w
    for l in range(k):                 #이동해야 할 거리만큼 순회
        if ch < n and cdict['d'] > 0:    #세로 범위 내 확인  and 명령 가능 횟수 확인
            res.append("d")
            cdict['d'] -= 1
            ch += 1
        elif cw > 1 and cdict['l'] > 0:  #가로 범위 내 확인  and 명령 가능 횟수 확인
            res.append("l")
            cdict['l'] -= 1
            cw -= 1
        elif cdict['r'] > 0:
            res.append("r")
            cdict['r'] -= 1
            cw += 1
        elif cdict['u'] > 0:
            res.append("u")
            cdict['u'] -= 1
            ch -= 1
        
    return ''.join(res)    #리스트 문자열 변환해 리턴
    
    

def solution(n, m, x, y, r, c, k):
    cdict = {'d':0,'l':0,'r':0,'u':0}    #실행 해야할 명령별 개수 기록
    h = r-x
    w = c-y
    abh = abs(h)    #
    abw = abs(w)
    cal(h,w,abh,abw,cdict)          #cdict에 도착에 필요한 명령 입력
    
    over = k-(abh+abw)              #도착 후 초과하는 이동거리
    if over < 0:
        return 'impossible'         #k가 도착에 필요한 거리보다 부족할 시 impossible 리턴
    
    if over % 2 == 0:
        return route(cdict,x,y,n,m,over,k)
    else:
        return "impossible"         #over가 2의 배수가 아니라면 탈출 불가
