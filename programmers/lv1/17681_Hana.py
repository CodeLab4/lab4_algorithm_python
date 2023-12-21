def solution(n, arr1, arr2):
    answer = []

    secret_map = list()
    for x in range(0, n):
        row1 = bin(arr1[i])[2:].zfill(n)
        row2 = bin(arr2[i])[2:].zfill(n)

        found = ''
        for i in range(len(row1)):
            if row1[i] == '0' and row2[i] == '0':
                found += ' '
            else:
                found += '#'
        answer.append(found)

    return answer
