def solution(info, query):
    answer = []

    info_dic = {idx: {'lang': i.split()[0], 'major': i.split()[1], 'grade': i.split()[2], 'like': i.split()[3],
                      'score': int(i.split()[4])} for idx, i in enumerate(info)}

    info_size = len(info_dic)

    for idx in range(len(query)):
        cnt = 0
        q = query[idx].split(' and ')
        q1 = q[3].split()

        for s in range(info_size):
            if (info_dic[s]['lang'] == q[0] or q[0] == '-') and (info_dic[s]['major'] == q[1] or q[1] == '-') and (
                    info_dic[s]['grade'] == q[2] or q[2] == '-') and (info_dic[s]['like'] == q1[0] or q1[0] == '-') and \
                    info_dic[s]['score'] >= int(q1[1]):
                cnt += 1

        answer.append(cnt)

    return answer