def solution(n, arr1, arr2):
    answer = []

    lst1 = convert(n, arr1)
    lst2 = convert(n, arr2)

    for i in range(n):
        str = ''
        for j in range(n):
            if lst1[i][j] == '1' or lst2[i][j] == '1':
                str += '#'
            else:
                str += ' '
        answer.append(str)

    return answer


def convert(n, arr):
    lst = []
    for node in arr:
        bi = bin(node)[2:]
        while len(bi) < n:
            bi = '0' + bi
        lst.append(bi)
    return lst
