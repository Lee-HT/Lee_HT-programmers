def nroad(road,y,x,state):
    dic = {'u':'r','r':'d','d':'l','l':'u'}
    if road[y][x] == 0:        #해당 좌표가 비어있다면 저장
        road[y][x] = state
    else:
        if dic[state] == road[y][x]:     #시계 방향으로 돌도록 변경 value -> key
            road[y][x] = state

def makeroad(road,r):
    rx = [r[0],r[2]]   #x축 최소, 최대 값
    ry = [r[1],r[3]]   #y축 최소, 최대 값
    
    for y in range(ry[0],ry[1]):            #직관성을 위해 리스트 형태로 구현 (y축 뒤집은 상태)
        nroad(road,ry[1]+ry[0]-y,rx[0],'u') #up    #시작이 ry[0] 이므로 ry[0]을 더함
        nroad(road,y,rx[1],'d') #down
        
    for x in range(rx[0],rx[1]):
        nroad(road,ry[0],x,'r') #right
        nroad(road,ry[1],rx[1]+rx[0]-x,'l') #left  #시작이 rx[0]이므로 rx[0]를 더함

def search(pos,target,road,score):   #출발 -> 도착 시계 방향 거리 측정
    if pos == target:
        return score
    else:
        npos=[]
        state=road[pos[0]][pos[1]]
        if state == 'u':
            npos = [pos[0]-1,pos[1]]
        elif state == 'r':
            npos = [pos[0],pos[1]+1]
        elif state == 'd':
            npos = [pos[0]+1,pos[1]]
        else:
            npos = [pos[0],pos[1]-1]
        return search(npos,target,road,score+1)
        
    

def solution(rectangle, characterX, characterY, itemX, itemY):
    road = [[0 for i in range(51)] for i in range(51)]
    for r in rectangle:
        makeroad(road,r)
        
    cha = [characterY,characterX]
    item = [itemY,itemX]
    left = search(cha,item,road,0)   #캐릭터 위치 -> 아이템 위치
    right = search(item,cha,road,0)  #아이템 위치 -> 캐릭터 위치
    
    answer = min(left,right)
    return answer
