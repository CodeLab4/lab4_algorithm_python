def solution(data, ext, val_ext, sort_by):
    answer = [[]]

    condition_dic = ['code', 'date', 'maximum', 'remain']
    answer = [item for item in data if item[condition_dic.index(ext)] < val_ext]
    answer = sorted(answer, key=lambda answer: answer[condition_dic.index(sort_by)])

    return answer
