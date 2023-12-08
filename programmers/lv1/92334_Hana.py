def solution(id_list, report, k):
    answer = []

    ids = dict()
    for i in id_list:
        ids[i] = list()

    for i in report:
        if i.split(' ')[0] in ids:
            reported_ids = list()
            reported_ids.append(i.split(' ')[1])
            ids[i.split(' ')[0]] += reported_ids

    report_result = dict()
    for i in ids.values():
        for j in i:
            report_result[j] = 0

    for i in ids:
        for i in set(ids.get(i)):
            if i in report_result:
                report_result[i] += 1

    for i in ids:
        receive = 0
        for j in set(ids.get(i)):
            if report_result[j] >= k:
                receive += 1
        answer.append(receive)
    return answer
