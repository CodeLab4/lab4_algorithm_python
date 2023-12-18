def solution(N, stages):
    answer = []

    fail_dic = dict()
    max_stage = N + 1
    for i in range(1, max_stage):
        total_player = 0
        yet_player = 0
        for stage in stages:
            if stage >= i:
                total_player += 1
                if stage == i:
                    yet_player += 1
        if total_player == 0:
            fail_dic[i] = 0
        else:
            fail_dic[i] = yet_player / total_player

    print(fail_dic)
    sorted_lst = sorted(fail_dic.items(), key=lambda item: item[1], reverse=True)

    answer = list(item[0] for item in sorted_lst)

    return answer
