def solution(survey, choices):
    answer = ''

    # survey: 질문마다 판단하는 지표(비동의/동의에 대한 지표)
    # choices: 검사자가 각 질문마다 선택한 선택지(완전비동의~완전동의)

    category = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    result = dict.fromkeys(category, 0)

    score = dict()
    score[1] = 3
    score[2] = 2
    score[3] = 1
    score[4] = 0
    score[5] = 1
    score[6] = 2
    score[7] = 3

    for i, survey_category in enumerate(survey):
        first_category, second_category = survey_category[0], survey_category[1]
        choice_score = survey[i]

        if choices[i] < 4:
            result[first_category] += score[choices[i]]
        elif choices[i] > 4:
            result[second_category] += score[choices[i]]

    # 하나의 지표에서 각 성격 유형 점수가 같으면, 사전 순으로 판단
    # keys = list(result.keys())
    # print(keys)

    if result[category[0]] > result[category[1]]:
        answer += category[0]
    elif result[category[0]] < result[category[1]]:
        answer += category[1]
    else:
        answer += category[0]

    if result[category[2]] > result[category[3]]:
        answer += category[2]
    elif result[category[2]] < result[category[3]]:
        answer += category[3]
    else:
        answer += category[2]

    if result[category[4]] > result[category[5]]:
        answer += category[4]
    elif result[category[4]] < result[category[5]]:
        answer += category[5]
    else:
        answer += category[4]

    if result[category[6]] > result[category[7]]:
        answer += category[6]
    elif result[category[6]] < result[category[7]]:
        answer += category[7]
    else:
        answer += category[6]

    return answer
