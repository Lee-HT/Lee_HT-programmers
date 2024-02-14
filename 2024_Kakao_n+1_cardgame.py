# 중복 숫자 제거, 제거된 리스트 & 제거 쌍 +1 반환
def remove_all(lists):
    nums = list()
    for i in range(len(lists)):
        if lists[i] in lists[i+1:]:
            nums.append(lists[i])
    return [l for l in lists if l not in nums],len(nums)+1

# 리스트에 중복된 숫자 한 쌍 제거
def removed(lists):
    num = 0
    for i in range(len(lists)):
        if lists[i] in lists[i+1:]:
            num = lists[i]
            break
    if num != 0:
        return [i for i in lists if i != num] , True
    else:
        return [], False

# lists,checks 각각 요소중 같은 숫자 확인
# lists 에 중복된 수가 없어야 함
def pair_check(lists,checks):
    pairs = list()
    for l in lists:
        if l in checks:
            pairs.append(l)
            checks.remove(l)
    return len(pairs),checks

def solution(coin, cards):
    n = len(cards)
    # 합이 n+1인 숫자 쌍을 동일 숫자로 전처리
    cards = [n-c+1 if c > n//2 else c for c in cards]
    
    index = n // 3
    # 보유 카드
    saved = cards[:index]
    # 뽑기 가능한 카드
    selects = list()
    sets = set(saved)
    # 초기 카드 뭉치 카드 쌍
    saved,pair = remove_all(saved)
    rounds = 0
    
    while True:
        # 현재 카드 뽑기 가능한 라운드
        if pair != 0:
            index += pair * 2
            rounds += pair
            cur = cards[index-pair * 2:index]
            # 코인 1개로 뽑을 수 있는 수 확인
            pair, cur = pair_check(saved,cur)
            selects.extend(cur)
            if coin >= pair:
                coin -= pair
            else:
                rounds += coin
                break
        # 코인 1개로 불가능 할 시 2개 사용한 쌍 확인
        else:
            selects, check = removed(selects)
            if check and coin >= 2:
                pair = 1
                coin -= 2
            # 코인이 부족하거나 가능한 숫자 쌍 없을시 break
            else:
                break
    
    return min(rounds,n//3 + 1)
