import re

# 프로그래머스 Lv.1 숫자 문자열과 영단어
def solution(s):
    answer = 0

    eng_words = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
        }

    word = ''
    answer_list = []
    for i in s:
        if re.match(r'[0-9]', i):
            answer_list.append(i)
        else:
            word += str(i)
            if word in eng_words.keys():
                answer_list.append(str(eng_words[word]))
                word = ''

    answer = int(''.join(answer_list))

    return answer
