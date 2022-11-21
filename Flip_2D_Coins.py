from collections import deque

def width(board,n):           #열 뒤집기
    for i in range(len(board)):
        board[i][n] = 0 if board[i][n] else 1

def solution(beginning, target):
    hlen = len(beginning)
    wlen = len(beginning[0])
    answer = []
    
    flip = [[0 for _ in range(wlen)]for _ in range(hlen)]
    for h in range(hlen):                #뒤집은 행렬 생성
        for w in range(wlen):
            if beginning[h][w]:
                flip[h][w] = 0
            else:
                flip[h][w] = 1
                
    for i in range(2**hlen): #가능한 열 배치 수
        count = 0
        copied = []
        n = i
        index = 0
        que = deque()
        for _ in range(hlen): #진수 변환
            cur = n % 2
            n = n // 2
            if cur:
                que.append(1)
            else:
                que.append(0)
        
        for i in range(hlen): #2진수로 가능한 열 배 생성
            index
            cur = que.pop()
            if cur:
                copied.append(flip[i][:])
                count += 1
            else:
                copied.append(beginning[i][:])
        
        
        for w in range(wlen): #행 뒤집기
            equal = True
            for h in range(hlen):
                if copied[h][w] != target[h][w]:
                    equal = False
                    break
            if not equal:          #현재 행이 정답과 다를 시 뒤집기
                width(copied,w)
                count += 1
        
        if copied == target:
            answer.append(count)
    
    return min(answer) if answer else -1
