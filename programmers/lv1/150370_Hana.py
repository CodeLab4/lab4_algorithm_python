def solution(today, terms, privacies):
    answer = []

    this_year = int(today.split('.')[0]) * (12 * 28)
    this_month = int(today.split('.')[1]) * 28
    this_date = int(today.split('.')[2]) + this_year + this_month

    terms_dic = dict()
    for term in terms:
        terms_dic[term.split(' ')[0]] = term.split(' ')[1]

    for index, privacy in enumerate(privacies):
        year = int(privacy.split('.')[0])
        month = int(privacy.split('.')[1])
        day = int(privacy.split('.')[2].split(' ')[0])

        year = year * (12 * 28)
        month = (month + int(terms_dic[privacy.split(' ')[1]])) * 28
        day = year + month + day

        print(day, this_date)
        if day <= this_date:
            answer.append(index + 1)

    return answer
