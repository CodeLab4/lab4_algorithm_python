def solution(s):
    answer = ''

    word = ''
    for index, j in enumerate(s):
        if j != ' ':
            word += j
            if index == len(s) - 1 or s[index + 1] == ' ':
                answer += word[0].upper() + word[1:].lower()
                word = ''
        else:
            answer += j

    return answer
