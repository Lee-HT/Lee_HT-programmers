def cal(seq):   # 펄스 수열을 sequence에 곱해줌
    start = -1
    pulse = []
    for s in seq:         # sequence 순회
        start = -start
        pulse.append(s*start)
    return pulse

def solution(sequence):
    pulse = cal(sequence)
    acc_sum = [0 for _ in range(len(pulse)+1)]
    for i in range(len(pulse)):             # 펄스 수열이 곱해진 sequence의
        acc_sum[i+1] = acc_sum[i]+pulse[i]  # 누적합 저장
    

    res = max(acc_sum)-min(acc_sum)  # 인덱스 요소의 차가 구간합이므로 max값-min값

    return res
