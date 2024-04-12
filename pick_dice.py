from collections import defaultdict
from itertools import combinations

def solution(dice):
    n = len(dice)
    comp = [defaultdict(int) for _ in range(11)]
    comb = list(combinations(range(1,n+1),n//2))
    comb = [[comb[idx],comb[-1-idx]] for idx in range(len(comb)//2)]
    for i in range(len(dice)):
        for j in dice[i]:
            comp[i+1][j] += (1)
            
    win_counts = {}
    # 조합 순회
    for c in comb:
        # case 조합의 첫번째 주사위로 초기화
        cases = [comp[c[_][0]] for _ in range(2)]
        
        # case A,B
        for i in range(2):
            # 조합 내부 순회
            for j in range(1,n//2):
                cur = defaultdict(int)
                # 기존 케이스
                for k,v in cases[i].items():
                    # 현재 케이스
                    for nk,nv in comp[c[i][j]].items():
                        cur[k+nk] += v*nv
                cases[i] = cur
                
        win_a , win_b = 0,0
        # A 주사위 경우의 수
        for ak,av in cases[0].items():
            # B 주사위 경우의 수
            for bk,bv in cases[1].items():
                if ak > bk:
                    win_a += av*bv
                elif ak < bk:
                    win_b += av*bv
        win_counts[c[0]] = win_a
        win_counts[c[1]] = win_b
    
    # value(승리 수) 최대 값
    answer = max(win_counts,key = win_counts.get)
    return answer
