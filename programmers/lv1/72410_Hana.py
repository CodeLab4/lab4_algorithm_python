import re
from itertools import groupby


def solution(new_id):
    answer = ''

    # 아이디 길이: 3-15
    # 유효 문자: 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만
    # 마침표는 처음과 끝 x, 연속 x

    # 대문자 -> 소문자 치환
    new_id = new_id.lower()
    input_id_list = new_id[0:]

    # 유효 문자 외 제거
    set = {'~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '=', '+', '[', '{', ']', '}', ':', '?', ',', '<', '>',
           '/'}

    char_valid_list = [i for i in input_id_list if i not in set]

    # 마침표 2번 이상 연속 -> 1개
    result = []
    for char in char_valid_list:
        if char == '.' and result and result[-1] == '.':
            continue  # 현재 문자가 마침표이고, 이전 문자도 마침표라면 무시
        result.append(char)

    char_valid_list = result

    # 마침표 처음이나 끝에 위치하면 제거
    if char_valid_list and char_valid_list[-1] == '.':
        del char_valid_list[-1]
    if char_valid_list and char_valid_list[0] == '.':
        del char_valid_list[0]

    # 빈 문자열이면 "a" 대입
    if not char_valid_list:
        char_valid_list.append('a')

    # 길이가 16자 이상이면 15까지만 두고 제거
    # 제거후 마친표가 끝에 위치하면 마침표 제거
    if len(char_valid_list) > 15:
        while (len(char_valid_list) > 15):
            del char_valid_list[-1]

    if char_valid_list[-1] == '.':
        del char_valid_list[-1]

    # 길이가 2자 이하면, 마지막 문자를 길이 3 될때까지 반복해 붙이기
    if len(char_valid_list) < 3:
        while len(char_valid_list) < 3:
            char_valid_list.append(char_valid_list[-1])

    answer = ''.join(char_valid_list)

    return answer
