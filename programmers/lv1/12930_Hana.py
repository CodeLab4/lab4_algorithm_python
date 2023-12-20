def solution(s):
    answer = ''

    words = list(s)

    i = 0
    for char in words:
        if char == ' ':
            answer += char
            i = 0
        else:
            if i % 2 == 0:
                answer += char.upper()
            else:
                answer += char.lower()

    return answer