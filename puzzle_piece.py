import numpy as np
import copy

def block(board,blist):
    res = 0
    for h in range(len(board)):
        for w in range(len(board)):
            if board[h][w] == 0:              #빈공간 발견시 dfs
                dlist = DFS(h,w,[],board)
                dlist = sorted(makemin(dlist))       #비교를 위해 정렬
                for b in blist:
                    if dlist in b:            #퍼즐 조각의 4가지 방향 중 같은게 있으면
                        blist.remove(b)       #발견시 발견한 조각 삭제
                        res += len(dlist)     #퍼즐 조각의 크기만큼 결과에 +
                        break
                        
    
    return res

def circuit(board):
    piece = []
    for h in range(len(board)):
        for w in range(len(board)):
            if board[h][w] == 0:
                one = []
                for r in rotate(DFS(h,w,[],board)):    #4방향 회전값
                    r = sorted(r)                      #비교를 위해 정렬
                    one.append(r)                      #회전된 값들의 중복을 피하기 위해 4가지를 묶어 리턴
                piece.append(one)
    return piece

def chn(board):                         #reverse
    for l in range(len(board)):
        for i in range(len(board[0])):
            if board[l][i]:
                board[l][i] = 0
            else:
                board[l][i] = 1
    return board
            

def cal(lists,mode):         #mode 0 min 리턴 , mode 1 max 리턴
    if mode == 0:
        return [min(lists)[0],min(lists,key = lambda x : x[1])[1]]   #[axis : 0, axis : 1] 리턴
    else:
        return [max(lists)[0],max(lists,key = lambda x : x[1])[1]]
    
def makemin(dlist):
    nparr = np.array(dlist) - cal(dlist,0)  #회전을 위해 모든값에 최소값을 빼줌
    arr = nparr.tolist()
    return arr

def rotate(dolist):
    res = []
    arr = makemin(dolist)
    nmax = max(cal(arr,1))     #회전할 퍼즐의 최대 길이
    
    res.append(arr)
    for n in range(3):
        rot = []
        arr = res[n]                         #이전 회전 결과
        for d in arr:
            rot.append([d[1],nmax-d[0]])     #시계방향 회전
        rot = makemin(rot)                   #회전 시에 최소값이 0이 아니게 되는경우 다시 최소화
        res.append(rot)
    
    return res          #90, 180, 270, 360도 회전값 

def DFS(y,x,dolist,board):
    if board[y][x] == 1:
        return None
    else:
        board[y][x] = 1
                
    global maxlen
    
    if x != 0:
        DFS(y,x-1,dolist,board)
    if x != maxlen:
        DFS(y,x+1,dolist,board)
    if y != 0:
        DFS(y-1,x,dolist,board)
    if y != maxlen:
        DFS(y+1,x,dolist,board)
    dolist.append([y,x])
    return dolist

            
maxlen = 0

def solution(game_board, table):
    table_c = chn(table)       #테이블 뒤집어서 퍼즐을 0으로
    global maxlen
    maxlen = len(game_board) -1
    
    blist = circuit(table_c)
    
    answer = block(game_board,blist)
    return answer
