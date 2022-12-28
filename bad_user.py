import itertools as it
import re

def check(user_id,bid):
    user_list = []
    for i in user_id:
        if bid.fullmatch(i):
            user_list.append(i)
    return user_list
    
                        

def solution(user_id, banned_id):
    permu = set()
    fin = []
    ban_com = [re.compile(b.replace("*",".")) for b in banned_id]  #banned_id 정규식 컴파일
    
    for b in ban_com:                 #banned_id의 요소별
        fin.append(check(user_id,b))  #매칭 가능한 문자들 배열에 넣어 append
    
    for fi in fin:
        permu.update(fi)     #순열 생성을 위해 중복 제외 해줌
    
    permu = list(permu)
    res = set()
    
    permutation = list(it.permutations(permu,len(banned_id)))   #순서를 보장하지 못하기 때문에 순열
    
    for perm in permutation:
        ok = True
        for i,p in enumerate(perm):    #순열을 순회하며 banned_id 요소에 하나씩 매칭된다면
            if not p in fin[i]:
                ok = False
                break
        if ok == True:
            plist = sorted(list(perm)) #중복을 제거하기 위해 정렬하여
            res.add(tuple(plist))      #set에 저장
    
    print(res)
    answer = len(res)    #가능한 목록 개수 리턴
    return answer
