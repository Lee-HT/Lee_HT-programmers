from collections import defaultdict

def time_sec(time,sec):
    tsp = list(map(int,time.replace('.',':').split(':')))  #.을 :으로 변경후 : 기준 split하여 map 함수로 int로 변환
    end = tsp[0]*3600000+tsp[1]*60000+tsp[2]*1000+tsp[3]    #시간, 분, 초를 ms로 변환
    start = end-int(float(sec)*1000)-999         #끝시간에서 (처리 시간-1)을 빼주고 범위가 1초임으로 (1000-1)를 추가로 뺌 (시작시간과 끝시간이 처리량에 포함)
    return start,end   #시작시간과 끝시간 ms로 리턴

def solution(lines):
    tline = []
    tdic = defaultdict(int)
    for l in lines:
        l=l.split(' ') #띄어쓰기 스플릿하여 날짜와 시간 구별
        start,end = time_sec(l[1],l[2].replace('s',''))  #끝시간, s를 삭제한 처리시간
        tline.append(start)  #시간 순서로 순회를 위해 시간 추가
        tdic[start] += 1     #현재 시간에 처리해야할 로그 1개 추가됨
        tline.append(end)
        tdic[end] -= 1       #현재 시간에 처리해야할 로그 1개 사라짐

    maxn = 0
    now = 0
    tline  = sorted(set(tline))  #시간 중복 제거
    while tline:     #tline 요소를 더해주며 max값 기록 (해당 시간 처리량)
        t = tline[0]
        tline.pop(0)
        now += tdic[t]
        maxn = max(maxn,now)
    
    return maxn
