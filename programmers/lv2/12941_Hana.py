def solution(A, B):
    answer = 0

    A.sort()
    B.sort(reverse=True)

    # for i in range(len(A)):
    #     answer += A[i]*B[i]

    # 리스트 컴프리헨션
    answer = sum(A[i] * B[i] for i in range(len(A)))

    return answer
