def solution(today, terms, privacies):
    answer = []

    int_today = int(today.replace('.', ''))

    parsed_terms = dict()
    for i in terms:
        parsed_terms[i.split(' ')[0]] = i.split(' ')[1]

    for index, privacy in enumerate(privacies):
        stored_period = int(parsed_terms.get(privacy.split(' ')[1]))
        year = int(privacy.split(' ')[0].split('.')[0])
        month = int(privacy.split(' ')[0].split('.')[1])
        day = int(privacy.split(' ')[0].split('.')[2])
        category = privacy.split(' ')[1]
        # print(month + stored_period)
        if month + stored_period > 12:
            changed_years = (month + stored_period) // 12
            year = year + 1 * changed_years

        day = (day + stored_period * 28)
        for _ in range(day // 28):
            day -= 28
        day -= 1
        if day == 0:
            day = 28
        elif day < 0:
            day = 28 + day

        month = month + stored_period
        if month > 12:
            for _ in range(month // 12):
                month -= 12

        str_delete_day = str(year) + str(month).zfill(2) + str(day).zfill(2)
        print(str_delete_day, int_today)
        if int(str_delete_day) < int_today:
            answer.append(index + 1)

    return answer
