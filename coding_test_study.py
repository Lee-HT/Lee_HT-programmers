import math

def solution(alp, cop, problems):
    # 문제에 공부 추가
    problems.extend([[0,0,0,1,1],[0,0,1,0,1]])
    
    # 문제를 모두 풀기 위한 목표 값
    max_alp = max([i[0] for i in problems])
    max_cop = max([i[1] for i in problems])
    
    # 초기 값이 모든 문제보다 클 경우
    max_alp = max(max_alp,alp)
    max_cop = max(max_cop,cop)
    
    dp = [[math.inf for _ in range(max_cop+1)]for _ in range(max_alp+1)]
    # 시작 pos
    dp[alp][cop] = 0
    
    # 현재 값 ~ 목표 값 만큼 순회
    for a in range(alp,max_alp+1):
        for c in range(cop,max_cop+1):
            for p in problems:
                if a>=p[0] and c>=p[1]:
                    # max값 초과시 max 값으로 변경
                    alp_p, cop_p = min(a+p[2],max_alp), min(c+p[3],max_cop)
                    # 기존 경우와 해당 문제를 풀었을 경우 비교해 min값 저장
                    dp[alp_p][cop_p] = min(dp[alp_p][cop_p],dp[a][c]+p[4])

    answer = dp[max_alp][max_cop]
    return answer
