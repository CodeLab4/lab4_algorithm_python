from itertools import *


def solution(users, emoticons):
    answer = []
    rate = [0.4, 0.3, 0.2, 0.1]
    comb = []
    for rate_comb in product(rate, repeat=len(emoticons)):
        temp_lst = []
        for i in range(len(emoticons)):
            temp_lst.append([rate_comb[i], emoticons[i] - emoticons[i] * rate_comb[i]])
        comb.append(temp_lst)
    for discount_lst in comb:
        sum = 0
        join_count = 0
        for user in users:
            pay = 0
            for idx in range(len(emoticons)):
                if user[0] <= discount_lst[idx][0] * 100:
                    pay += discount_lst[idx][1]
            if pay >= user[1]:
                join_count += 1
            else:
                sum += pay

        answer.append([join_count, int(sum)])

    answer.sort(reverse=True)
    answer = answer[0]

    return answer


if __name__ == '__main__':
    solution([[40, 10000], [25, 10000]], [7000, 9000])
