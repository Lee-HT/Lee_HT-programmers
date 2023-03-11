import math

def solution(matrix_sizes):
    lmat = len(matrix_sizes)
    new_mat = [[0 for i in range(lmat)] for i in range(lmat)]     #0으로 초기화, 행렬 하나는 행렬 곱 불가능 하기 때문에 연산 횟수 0
    for n in range(1,lmat):       #n+1개의 행렬 곱 1개는 연산이 없으니 2개부터 시작
        for i in range(lmat-n):   #0 ~ (0+n) ... (lmat-n-1) ~ (lmat-1)  i부터 n+1개의 행렬 곱 (i가 lmat-n-1일 때 lmat-1까지의 행렬 곱)
            new_mat[i][i+n] = math.inf    #최소 값을 구하므로 초기값 inf
            for j in range(i,i+n):        #j를 하나씩 늘려가며 i~j, i*j*(j+1), j+1~(i+n)
                new_mat[i][i+n] = min(new_mat[i][i+n],     #현재 저장된 최소 값
                                      new_mat[i][j]        #i~j 까지의 최소 값
                                      + new_mat[j+1][i+n]  #(j+1) ~ (i+n) 까지의 최소 값
                                      + matrix_sizes[i][0] * matrix_sizes[j][1] * matrix_sizes[i+n][1])  #i~j와 (j+1)~(i+n) 범위에 대한 행렬 곱의 결과로
                                                                                                         #i by j, j+1 by i+1의 행렬곱 j == j+1 이므로 i*j*i+n 값
    return new_mat[0][lmat-1]    #전체 범위의 최소 값 리턴
