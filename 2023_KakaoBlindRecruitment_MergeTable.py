class Select:                       #셀 병합 용도로 객체 사용
    def __init__(self,h,w,value):
        self.res = []
        self.mergeList = [[h,w]]    #현재 객체로 병합된 셀 위치
        self.value = value          #현재 객체 저장된 값
    
    def append_(self,h,w):          #추가로 병합된 셀 위치 추가
        self.mergeList.append([h,w])
        
    def reset_merge(self,h,w):      #매개 변수의 위치만 유지하고
        self.mergeList.remove([h,w])
        self.res = self.mergeList   #병합 해제할 위치들 리턴
        self.mergeList = [[h,w]]
        return self.res
    
    def get_mer(self):              #현재 병합되어 있는 위치 값들 리턴
        return self.mergeList
        
    def set_(self,value):           #현재 객체 값 변경
        self.value = value
        
    def get_(self):                 #현재 객체 값 리턴
        if not self.value:          #존재하지 않을 시 EMPTY 리턴
            return "EMPTY"
        return self.value

def unMerge(Table,h,w):
    dels = Table[h][w].reset_merge(h,w)
    if dels:
        for hd,wd in dels:
            Table[hd][wd] = Select(hd,wd,None) #현재 위치 제외한 셀들 초기화
    
def merge(Table,h1,w1,h2,w2):
    if Table[h1][w1] == Table[h2][w2]:      #두 셀이 같다면 예외
        pass
    elif Table[h1][w1].get_() != "EMPTY":     #첫번째 셀이 EMPTY가 아니라면
        for h,w in Table[h2][w2].get_mer():   #두번째 셀의 병합된 셀 리스트 순회
            Table[h1][w1].append_(h,w)        #병합된 셀 하나를 첫번째 셀에 추가
            Table[h][w] = Table[h1][w1]       #병합된 셀을 첫번째 셀 객체로 변경
    else:
        for h,w in Table[h1][w1].get_mer():   #h2w2 를 h1w1 위치의 셀로 병합
            Table[h2][w2].append_(h,w)
            Table[h][w] = Table[h2][w2]
    
def updateValue(Table,value1,value2):         #셀 전체 순회하여 값 비교하고 변경
    for h in range(1,51):
        for w in range(1,51):
            if Table[h][w].get_() == value1:
                Table[h][w].set_(value2)
            
def update(Table,h,w,value):
    Table[h][w].set_(value)        #해당 위치 셀 객체 값 변경


def solution(commands):
    Table = [[Select(y,x,None) for x in range(51)] for y in range(51)]
    ans = []
    
    for c in commands:           #명령별로 맞는 함수에 인자 대입
        cs = c.split(" ")
        if cs[0] == "UPDATE":
            if len(cs) == 4:
                update(Table,int(cs[1]),int(cs[2]),cs[3])
            else:
                updateValue(Table,cs[1],cs[2])
        elif cs[0] == "MERGE":
            merge(Table,int(cs[1]),int(cs[2]),int(cs[3]),int(cs[4]))
        elif cs[0] == "UNMERGE":
            unMerge(Table,int(cs[1]),int(cs[2]))
        elif cs[0] == "PRINT":
            res = Table[int(cs[1])][int(cs[2])].get_()     #PRINT일시 결과 리스트에 append
            ans.append(res)
        
            
    return ans
