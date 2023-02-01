def get_parent(par,index):
    if par[index] == index:            #parent가 자기자신일 경우
        return index
    return get_parent(par,par[index])  #parents가 자기자신이 아닌 경우 재귀

def union(par,a,b):
    a_par = get_parent(par,a)
    b_par = get_parent(par,b)
    
    if a_par == b_par:          #a와 b의 부모가 같을 경우 0리턴
        return 0
    else:
        if a_par < b_par:       #작은 수를 부모로 변경(필요 x)
            par[b_par] = a_par
        else:
            par[a_par] = b_par
        return 1

def solution(n, costs):
    res = 0
    parents = [i for i in range(n)]
    costs = sorted(costs,key = lambda x : x[2])    #cost가 오름차순으로 정렬
    for c in costs:
        if union(parents,c[0],c[1]):   #parent가 같은지 확인 (이미 연결되었는지)
            res += c[2]                #결괏값에 cost +   
        
    return res
