def find(lists,num):            #이진 탐색 변형
    left,right = 0,len(lists)-1
    mid = (left+right+1) //2    #리스트 요소가 짝수일시 오른쪽 것을 선택하도록 +1 // 2
    
    while left < right:         #right가 left보다 큰 동안
        if num <= lists[mid]:   #num가 mid 위치의 값 보다 크지 않으면
            right = mid-1       #right를 mid-1로 변경하여 mid보다 큰 값 제외
        else:
            left = mid          #mid가 num보다 작다면 num보다 작은 값중 가장 큰 값을 찾기위해 left를 mid로 변경
            
        mid = (left+right+1) // 2    #새 범위에서 mid 재 계산후 반복
        
    return mid                  #b보다 작은 a의 최대값 or b보다 작은 a가 없다면 a의 최소값 리턴

def solution(A, B):
    A.sort()
    ans = 0
    for b in B:           #B를 순회
        now = find(A,b)   #이진 탐색으로 b보다 작은 a중 가장 큰 index 선택 (작은 a가 없는 경우 최소 값의 index 리턴)
        if A[now] < b:    #a가 b보다 작은지 확인 한 후
            A.pop(now)    #현재 a 값을 리스트에서 pop
            ans += 1      #승점 1+
    return ans
