from collections import deque

def width(board,n):
    for i in range(len(board)):
        board[i][n] = 0 if board[i][n] else 1

def solution(beginning, target):
    hlen = len(beginning)
    wlen = len(beginning[0])
    answer = []
    
    flip = [[0 for _ in range(wlen)]for _ in range(hlen)]
    for h in range(hlen):
        for w in range(wlen):
            if beginning[h][w]:
                flip[h][w] = 0
            else:
                flip[h][w] = 1
                
    for i in range(2**hlen):
        count = 0
        copied = []
        n = i
        index = 0
        que = deque()
        for _ in range(hlen):
            cur = n % 2
            n = n // 2
            if cur:
                que.append(1)
            else:
                que.append(0)
        
        for i in range(hlen):
            index
            cur = que.pop()
            if cur:
                copied.append(flip[i][:])
                count += 1
            else:
                copied.append(beginning[i][:])
        
        
        for w in range(wlen):
            equal = True
            for h in range(hlen):
                if copied[h][w] != target[h][w]:
                    equal = False
                    break
            if not equal:
                width(copied,w)
                count += 1
        
        if copied == target:
            answer.append(count)
    
    return min(answer) if answer else -1from collections import deque

def width(board,n):
    for i in range(len(board)):
        board[i][n] = 0 if board[i][n] else 1

def solution(beginning, target):
    hlen = len(beginning)
    wlen = len(beginning[0])
    answer = []
    
    flip = [[0 for _ in range(wlen)]for _ in range(hlen)]
    for h in range(hlen):
        for w in range(wlen):
            if beginning[h][w]:
                flip[h][w] = 0
            else:
                flip[h][w] = 1
                
    for i in range(2**hlen):
        count = 0
        copied = []
        n = i
        index = 0
        que = deque()
        for _ in range(hlen):
            cur = n % 2
            n = n // 2
            if cur:
                que.append(1)
            else:
                que.append(0)
        
        for i in range(hlen):
            index
            cur = que.pop()
            if cur:
                copied.append(flip[i][:])
                count += 1
            else:
                copied.append(beginning[i][:])
        
        
        for w in range(wlen):
            equal = True
            for h in range(hlen):
                if copied[h][w] != target[h][w]:
                    equal = False
                    break
            if not equal:
                width(copied,w)
                count += 1
        
        if copied == target:
            answer.append(count)
    
    return min(answer) if answer else -1
