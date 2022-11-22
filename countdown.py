from collections import defaultdict

def cal(num,fif,six):
    fif = [fif[0]+1,fif[1]+1]
    six = [six[0]+1,six[1]]
    if fif[0] != six[0]:
        return min([fif,six],key = lambda x : x[0])   #던질 다트 수가 다를 시 던질 다트수가 최소인 값 리턴
    else:
        return max([fif,six],key = lambda x : x[1])   #던질 다트 수가 같을 시 싱글,불 맞춘 횟수가 최대값 리턴

def div(num):       #70 이하의 최적의 점수 계산
    if num == 0:         #리턴값 [다트수,싱글or불 횟수]
        return [0,0]
    elif num <= 20:
        return [1,1]
    elif num <= 40:
        if num%2==0:
            return [1,0]
        if num%3==0:
            return [1,0]
        else:
            return [2,2]
    else:
        if num%3==0 and num<61:
            return [1,0]
        elif num==50:
            return [1,1]
        elif num>50:
            return [2,2]
        else:
            return [2,1]

def solution(target):
    dp = defaultdict(list)
    for i in range(1,71):
        dp[i] = div(i)
        
    for i in range(71,target+1):      #71 이후 50과 60을 맞추었을 때 최적의 값 계산
        dp[i] = cal(dp[i-50],dp[i-60])
    
    return dp[target]
