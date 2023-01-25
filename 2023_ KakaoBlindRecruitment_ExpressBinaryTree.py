def solution(numbers):
    answer = []
    
    for n in numbers:        #numbers 순회
        i = 1
        while 2**(i-1) <= n:         #이진 트리 노드 수만큼 2를 제곱하여
            i = i*2                  #n을 표현 가능한 포화 이진트리의 노드 수 탐색
        now = i-1
        n = bin(n).replace('0b','')  #n을 이진수로 변환
        binc = (now - len(n)) * '0'  #포화 이진트리에 맞도록 앞에 0을 추가
        binc += n

        
        mid = (now-1) // 2                 #포화 이진트리의 루트 노드 인덱스
        one = []                           #자식노드로 내려가며 비교를 위해 인덱스 저장
        res = ['0' for _ in range(now)]    #비교 할 결괏값
        
        if binc[mid] == '1':         #루트 노드가 1이라면
            one.append(mid)          #one에 append해 순회 시작
            res[mid] = '1'           #비교할 결과값 루트 노드를 1로 변경
        i=i//2                       #자식노드로 이동을 위한 값
        
        while i > 1:
            i = i//2                  #i를 2로 나누며 빼고 더한 값이 자식노드
            nexts = []
            for o in one:               #현재 저장된 자식노드들 순회
                om,op = o-i,o+i         #처리 중인 노드의 자식노드들
                if binc[om] == '1':     #해당 노드가 1이면
                    nexts.append(om)    #nexts에 append해 이어서 순회
                    res[om] = '1'       #비교할 결과값을 1로 변경
                if binc[op] == '1':
                    nexts.append(op)
                    res[op] = '1'
            one = nexts                 #처리 후 one에 nexts대입
        if binc == ''.join(res):        #res와 n의 이진변환 결과를 비교
            answer.append(1)            #같으면 1 다르면 0 answer에 
        else:
            answer.append(0)
    
    
    return answer
