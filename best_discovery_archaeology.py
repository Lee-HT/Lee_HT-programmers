from copy import deepcopy
import math

count = 0

def make_4(num,num_len):
    clock_l = []        #해당 인덱스의 숫자가 행의 시곗바늘 방향
    for _ in range(num_len):   # 4진법의 역순으로 변환
        clock_l.append(num%4)  # 4로 나누며 나머지 저장
        num = num // 4
    
    return clock_l

def rotate_clock(clock,h,w,rot_count,max_len): # 5개의 시계 회전
    if rot_count == 0:   # 회전 횟수가 0번일 시 바로 리턴
        return
    global count
    count += rot_count   #회전 횟수만큼 조작 횟수 +
    
    pos = [(-1,0),(1,0),(0,0),(0,1),(0,-1)]    # 12시,6시,현재,3시,9시
    for p in pos:     #각 방향을 순회
        hp = h+p[0]
        wp = w+p[1]
        if 0<=hp<max_len and 0<=wp<max_len:         #퍼즐 범위 내라면
            clockhands = clock[hp][wp] + rot_count  #회전 횟수만큼 회전
            clock[hp][wp] = clockhands if clockhands < 4 else clockhands-4  # 4이상 일시 0~3의 범위로 변경
    

def clock_match(clock,max_len):
    for c in range(max_len-1):
        for i in range(max_len):
            if clock[c][i] != 0:      #윗행 동일 열이 0이 아니라면
                rotate_clock(clock,c+1,i,4-clock[c][i],max_len)   #윗행을 0으로 만들만큼 회전리처리

def zero_check(clock):        # 퍼즐 전체를 순회
    for clock_line in clock:
        for c in clock_line:
            if c != 0:        # 0이 아닌 수가 존재하면
                return False  # False 리턴
    return True

def clock_rotate(clock):
    global count
    
    answer = math.inf
    max_len = len(clock[0])
    for r in range(4**max_len):      # 1행의 시곗바늘 경우의 수
        count = 0                    # 현재 경우의 수의 조작 횟수
        new_clock = deepcopy(clock)
        clocks = make_4(r,max_len)   # r을 시곗바늘들의 방향이 저장된 리스트로 변환
        for i,rot_count in enumerate(clocks):             # clock를 순회하여
            rotate_clock(new_clock,0,i,rot_count,max_len) # 첫번째 행을 회전 시킴
        clock_match(new_clock,max_len)   # 나머지 행을 윗행 방향 기준으로 회전

        if zero_check(new_clock):        # 모두 12시방향(0)으로 회전되어 있다면
            answer = min(answer,count)   # 퍼즐 해결이므로 조작 횟수를 기존의 최소값과 비교(초깃값 inf, 해결 가능만 주어짐)

    return answer  #최소 조작횟수 리턴

def solution(clockHands):
    return clock_rotate(clockHands)
