def solution(today, terms, privacies):
    answer = []
    input_day = convert_days(today)

    dic = {}
    for i in terms:
        temp = i.split(' ')
        dic[temp[0]] = int(temp[1]) * 28

    for i in range(len(privacies)):
        split_pri = privacies[i].split(' ')
        start_day = convert_days(split_pri[0])
        plus_month = dic.get(split_pri[1])
        compare_day = start_day + plus_month

        if input_day >= compare_day:
            answer.append(i + 1)

    return answer


def convert_days(days):
    year, month, day = [int(i) for i in days.split('.')]
    return year * 12 * 28 + month * 28 + day
