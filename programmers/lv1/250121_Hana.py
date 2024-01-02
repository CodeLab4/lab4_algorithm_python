def solution(data, ext, val_ext, sort_by):
    answer = list()

    data_dic = dict()

    for i in range(len(data)):
        data_dic['code'] = data[i][0]
        data_dic['date'] = data[i][1]
        data_dic['maximum'] = data[i][2]
        data_dic['remain'] = data[i][3]

        if data_dic[ext] < val_ext:
            answer.append(list(data_dic.values()))

    index_dic = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}
    answer = sorted(answer, key=lambda answer: answer[index_dic[sort_by]])

    return answer
