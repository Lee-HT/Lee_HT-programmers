def pay(sell,parents,answer,amount):
    cost = 10001
    while cost != 0 and sell>=0:
        cost = amount // 10            #추천인에게 지급되는 이득
        answer[sell] += (amount-cost)  #현재 처리중인 조직원 이득
        amount = cost                  #amount 추천인의 이득으로 갱신
        sell = parents[sell]           #sell 추천인 인덱스로 갱신
        
    
def solution(enroll, referral, seller, amount):
    answer = []
    parents= []
    idx = {'-':-1}
    for i,r in enumerate(referral):
        idx[enroll[i]] = i      #seller 처리를 위해 추천인 인덱스 저장
        if r=='-':
            parents.append(-1)  #추천인이 센터일시 -1
        else:
            parents.append(idx[r])   #추천인 인덱스 저장
        answer.append(0)        #len(enroll) == len(referral)
    
    for s in range(len(seller)):
        pay(idx[seller[s]],parents,answer,amount[s]*100)   #판매자 인덱스와 판매액수 전달
    
    return answer
