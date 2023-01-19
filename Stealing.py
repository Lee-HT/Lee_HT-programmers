def find_money(money):
    n_max = []
    n_max.append(money[0])
    n_max.append(max(money[0],money[1]))
    for m in range(2,len(money)):                           #현재 집과 두 칸 이전의 집까지 최댓값과
        n_max.append(max(n_max[m-2]+money[m],n_max[m-1]))   #현재 집을 털지않고 한 칸 이전까지 최댓값을 비교해 높은값 기
    return n_max[-1]

def solution(money):
    fmax=find_money(money[:-1]) #마지막 집을 털지않은 경우
    lmax=find_money(money[1:])  #첫번째 집을 털지않은 경우
        
    answer = max(fmax,lmax)
    return answer
