def solution(n):
    # i가 6이상일 때
    # dp[i] = dp[i-1] + 2dp[i-2] + 5dp[i-3] + (2dp[i-4] + 2dp[i-5] + 4dp[i-6]) ...
    # dp[i-3] = (dp[i-4] + 2dp[i-5] + 5dp[i-6]) + (2dp[i-7] + 2dp[i-8] + 4dp[i-9]) ...
    # dp[i] = dp[i] + dp[i-3] - dp[i-3] 
    # dp[i] = dp[i-1] + 2dp[i-2] + 6dp[i-3] + dp[i-4] - 5dp[i-6]
    
    # Answer 1
    dp = [0 for i in range(n+1)]
    try:
        dp[0] = 1
        dp[1] = dp[0]
        dp[2] = dp[1] + 2*dp[0]
        dp[3] = dp[2] + 2*dp[1] + 5*dp[0]
        dp[4] = dp[3] + 2*dp[2] + 5*dp[1] + 2*dp[0]
    except:
        pass
    
    # 0으로 초기화되어 5일 때 i-6 = -1, dp [-1] == 0
    for i in range(5,n+1):
        dp[i] = (dp[i-1] + 2*dp[i-2] + 6*dp[i-3] + dp[i-4] - dp[i-6]) % 1000000007
        
    # Answer 2
    """
    # 다른 타일링의 결합이 아닌 타일링 수 * 나머지 길이의 타일링 수
    # 길이별 유일 타일링 수, 7이상 부터 반복이라 제외
    unq = [1,2,5,2,2,4]
    sum_unq = [0,0,0]
    
    # dp [0]과 [1]을 1로 초기화 (다른 인덱스 영향x)
    dp = [1 for i in range(n+1)]
    # 가로가 2~n일 때 가능한 타일링 수 계산
    for i in range(2,n+1):
        sumi = 0
        for j in range(min(i,6)):
            if j<3:
                sumi += dp[i-j-1] * unq[j]
            # 길이 4이상의 고유한 타일링을 묶어서 계산
            else:
            # 길이3의 간격으로 타일링 개수 누적
                if j-3 == (i-1)%3:
                    sum_unq[j-3] += dp[i-4]
                # i에 따라 unq 인덱스 순서 변경
                sumi += sum_unq[j-3] * unq[(i-j+2)%3+3]
        dp[i] = sumi % 1000000007
    """
    
    answer = dp[n]
    return answer
