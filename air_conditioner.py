import copy

def solution(temperature, t1, t2, a, b, onboard):
    # 온도 범위 정규화
    temp_range = max(t1,t2,temperature) - min(t1,t2,temperature) + 1
    reg = min(t1,t2,temperature)
    temp_reg = temperature - reg + 1
    vect = 1 if t1 - temperature > 0 else -1
    # 이전 시간, 현재 시간 온도
    dp = [-1 for _ in range(temp_range+2)]
    cur = [-1 for _ in range(temp_range+2)]
    #  실외 온도에 해당하는 인덱스 초기 설정
    cur[1 if vect == 1 else -2] = 0

    # 이전 시간의 인접한 온도 3가지 중 가능한 최소 온도
    def get_min(idx):
        adds = [b,a,0]
        numbers = [dp[idx], dp[idx-vect], dp[idx+vect]]
        nexts = []
        # -1 은 쾌적 온도가 불가능
        if numbers[0] != -1:
            # 실외 온도와 같다면 전력 소모 x
            if idx != temp_reg:
                nexts.append(numbers[0]+adds[0])
            else:
                nexts.append(numbers[0])
        for i in range(1,3):
            if numbers[i] != -1:
                nexts.append(numbers[i]+adds[i])
                
        return min(nexts) if nexts else -1
    
    for on in onboard+[]:
        dp = copy.deepcopy(cur)
        # 탑승 하지 않았을 시 모든 경우의 수 계산
        if not on:
            for i in range(1,temp_range+1):
                cur[i] = get_min(i)
        # 탑승 하였을 시 쾌적 온도 가능한 경우만 계산
        else:
            for i in range(1,temp_range+1):
                if i in range(t1-reg+1,t2-reg+2):
                    cur[i] = get_min(i)
                else:
                    cur[i] = -1

    # 탑승시의 경우를 모두 통과한 경우만 남아있으므로 최종 온도에 상관없이 최소 값
    answer = min([ans for ans in cur if ans != -1])
    return answer
