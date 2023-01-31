def cal(num1,num2):
    res = []
    for i in num1:             #num1과 num2의 요소간 모든 경우의 수 계산
        for j in num2:
            res.append(i*j)
            res.append(i+j)
            if i >= j:               #-인 경우 제외 number = 1~32000
                res.append(i-j)
                if j != 0:           #0으로 나누지 않도록
                    res.append(i//j)
            else:
                res.append(j-i)
                if i != 0:
                    res.append(j//i)
    return res

def need(num):  #N을 num만큼 사용할 때 경우의 수
    n = []
    numi = 0
    for i in range(num//2):   #num의 절반까지 
        num -= 1
        numi += 1
        n.append([num,numi])
    return n
        
def tensqu(num,n):          #num을 n만큼 연결해 표현한 숫자
    res = 0
    for i in range(n):
        res += num * (10**i)
    return res

def solution(N, number):
    if N == number:
        return 1
    mem = {i:{tensqu(N,i)} for i in range(1,9)} #N, NN, NNN... N*8 초깃값
    for i in range(2,9):            #가능한 경우 전체 순회
        for j in need(i):
            mem[i].update(cal(mem[j[0]],mem[j[1]])) #중복 제외를 위해 set에 update 수행
        if number in mem[i]:                        #해당 개수만큼 사용해서 만들 수 있다면 i 리턴
            return i
    return -1
