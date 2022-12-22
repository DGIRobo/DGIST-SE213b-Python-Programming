# Transposed matrix

'''
Description
함수에 전달되는 m x n matrix에 대해서 transposed matrix (n x m)를 반환하는 함수 TP(mat)를 구현하시오.

함수동작
m x n 를 nested list의 형태로 입력 받음
행렬의 행과 열을 전치하여 n x m 형태의 nested list를 반환
매개변수
mat:(nested list) n개로 이루어진 list가 m개 들어있는 리스트
반환값
(nested list) m개로 이루어진 list가 n개 들어있는 리스트
   - k 행이 k열로 전치 된 행렬
'''

'''
함수 실행 예시

v1 = [ [1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12] ]
print(TP(v1))
'''

'''
실행 결과 예시

[ [1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
'''

# Code

def TP(mat) :
    TP_matrix=[]
    for column in range(len(mat[0])): #column의 수만큼 row(리스트 안의 리스트)만들기.
        TP_matrix.append([])
    for column in range(len(mat[0])): #TP_matrix의 row를 각각 확인함.
        for row in range(len(mat)): #TP_matrix의 각 row의 column을 각각 확인해서 해당하는 수를 mat에서 찾아 넣음.
            TP_matrix[column].append(mat [row][column])
    return TP_matrix

v1 = [   [1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12] ]
print(TP(v1))
